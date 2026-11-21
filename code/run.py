"""CodeBridge AI evaluator.  Run from the repository root:  python code/run.py
It reads the saved Claude replies in test-data/replies/, puts the code into each test folder, runs it,
compares it with the REAL C++ output, and prints what you should do next."""
import csv
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent   # repository root
TESTS = sorted(p.name for p in (ROOT / "test-data" / "tests").iterdir() if p.is_dir())
FAIL = ("WRONG", "ERROR", "TIMEOUT")
PLACEHOLDER = "PASTE CLAUDE'S REPLY HERE"


def norm(s):
    return s.replace("\r\n", "\n").replace("\r", "\n").strip()


def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8", errors="replace")


def parse(text):
    """Reply -> {'T01': (code, text_outside_code_blocks)} using the '### T01' headings."""
    parts = re.split(r"(?m)^#{1,4}\s*\**\s*(T\d\d)\b.*$", text)
    found = {}
    for i in range(1, len(parts), 2):
        body = parts[i + 1]
        blocks = re.findall(r"```(?:python|py|python3)[ \t]*\r?\n(.*?)```", body, re.S | re.I)
        if blocks:
            notes = re.sub(r"```.*?```", "", body, flags=re.S)
            notes = re.sub(r"\n{3,}", "\n\n", notes).strip()
            lines = notes.split("\n")
            while lines and lines[-1].strip().endswith(":"):   # drop a leftover label such as 'Expected output:'
                lines.pop()
            notes = "\n".join(lines).strip()
            found[parts[i]] = (max(blocks, key=len), notes)
    return found


def run_code(path):
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    try:
        r = subprocess.run([sys.executable, str(path)], capture_output=True, timeout=20, env=env,
                           stdin=subprocess.DEVNULL, cwd=str(path.parent))
    except subprocess.TimeoutExpired:
        return "TIMEOUT", "Timed out after 20 seconds"
    out, err = r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")
    return ("ERROR", err) if r.returncode else ("OK", out)


def first_difference(expected, actual):
    e, a = norm(expected).split("\n"), norm(actual).split("\n")
    for i in range(max(len(e), len(a))):
        x = e[i] if i < len(e) else "(nothing)"
        y = a[i] if i < len(a) else "(nothing)"
        if x != y:
            return f"line {i + 1}:  expected [{x}]   got [{y}]"
    return "outputs differ"


# ---------------------------------------------------------------- load replies
replies = {}
for v in ("V0", "V1", "V2"):
    f = ROOT / "test-data" / "replies" / f"{v}.txt"
    if not f.exists():
        continue
    text = read(f)
    parsed = parse(text)
    leftover = "\n".join(l for l in text.splitlines() if PLACEHOLDER not in l).strip()
    if parsed:
        replies[v] = parsed
        if v != "V2":
            miss = [t for t in TESTS if t not in parsed]
            if miss:
                print(f"!! {v}: no python code found for {', '.join(miss)}. Open test-data/replies/{v}.txt and check.")
    elif leftover:
        print(f"!! test-data/replies/{v}.txt has text but no '### T01' heading with a python code block. Check the reply.")

if not replies:
    print("NEXT STEP: do Paste test-data/prompts_used/V0_prompt_FULL.txt into a NEW Claude chat,")
    print("then save the whole reply as test-data/replies/V0.txt).")
    raise SystemExit

result, actual, code = {}, {}, {}
VERS = []


def process(v):
    VERS.append(v)
    for t in TESTS:
        folder = ROOT / "test-data" / "tests" / t / v
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "README.txt").unlink(missing_ok=True)
        notes = ""
        if v == "V2":
            if t in replies.get("V2", {}):
                code[(t, v)], notes = replies["V2"][t]
            elif (t, "V1") in code:
                code[(t, v)] = code[(t, "V1")]
                notes = ("Not sent for fixing: V1 already passed." if result.get((t, "V1")) == "PASS"
                         else "Not found in the V2 reply, so the V1 code is kept.")
        elif t in replies[v]:
            code[(t, v)], notes = replies[v][t]
        if (t, v) not in code:
            result[(t, v)] = "MISSING"
            (folder / "result.txt").write_text("MISSING (no code found in the reply)\n", encoding="utf-8")
            continue
        (folder / "code.py").write_text(code[(t, v)].rstrip() + "\n", encoding="utf-8")
        if notes:
            name = "cause_of_fix.txt" if v == "V2" else "differences_notes.txt"
            (folder / name).write_text(notes + "\n", encoding="utf-8")
        status, text = run_code(folder / "code.py")
        expected = read(ROOT / "test-data" / "tests" / t / "expected_output.txt")
        if status == "OK":
            status = "PASS" if norm(text) == norm(expected) else "WRONG"
        result[(t, v)], actual[(t, v)] = status, text
        (folder / "actual_output.txt").write_text(text, encoding="utf-8")
        (folder / "result.txt").write_text(status + "\n", encoding="utf-8")


for v in ("V0", "V1"):
    if v in replies:
        process(v)
v1_all_pass = "V1" in replies and all(result[(t, "V1")] == "PASS" for t in TESTS)
auto_v2 = v1_all_pass and "V2" not in replies
if "V2" in replies or v1_all_pass:
    process("V2")

# ---------------------------------------------------------------- per test summary
for t in TESTS:
    about = read(ROOT / "test-data" / "tests" / t / "about.txt").strip()
    lines = [f"{t}: {about}", ""] + [f"{v}: {result[(t, v)]}" for v in VERS]
    (ROOT / "test-data" / "tests" / t / "summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- results files
res_dir = ROOT / "test-data" / "results"
res_dir.mkdir(exist_ok=True)
with open(res_dir / "results.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["test"] + VERS)
    for t in TESTS:
        w.writerow([t] + [result[(t, v)] for v in VERS])
    w.writerow([])
    w.writerow(["version", "passed", "total", "percent"])
    for v in VERS:
        p = sum(result[(t, v)] == "PASS" for t in TESTS)
        w.writerow([v, p, len(TESTS), round(100 * p / len(TESTS))])

lines = []
for t in TESTS:
    for v in VERS:
        if result[(t, v)] in FAIL:
            exp = read(ROOT / "test-data" / "tests" / t / "expected_output.txt")
            what = (first_difference(exp, actual[(t, v)]) if result[(t, v)] == "WRONG"
                    else "error: " + (actual[(t, v)].strip().split("\n") or [""])[-1])
            lines.append(f"{t} {v} {result[(t, v)]}: {what}")
(res_dir / "failures.txt").write_text(
    "FAILURES (auto-generated: first place where the Python output differs from the real C++ output)\n\n"
    + ("\n".join(lines) if lines else "None. Every test passed.") + "\n", encoding="utf-8")

summary = ["SCORES (a test passes only if the output is identical to the real C++ output)", ""]
for v in VERS:
    p = sum(result[(t, v)] == "PASS" for t in TESTS)
    summary.append(f"{v}: {p}/{len(TESTS)} passed ({round(100 * p / len(TESTS))}%)  " + "#" * (2 * p))
(res_dir / "summary.txt").write_text("\n".join(summary) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- print table
print("\n" + "test".ljust(6) + "".join(v.ljust(10) for v in VERS))
for t in TESTS:
    print(t.ljust(6) + "".join(result[(t, v)].ljust(10) for v in VERS))
print("\n" + "\n".join(summary[2:]))

# ---------------------------------------------------------------- V2 prompt + next step
bad = [t for t in TESTS if result.get((t, "V1")) in FAIL]
v2_prompt = ROOT / "test-data" / "generated" / "V2_prompt.txt"
if "V1" in replies and bad:
    parts = [
        "Earlier you translated C++ programs to Python. I ran your Python code and compared it with the output of the "
        "real C++ program. The tests below FAILED. For each one I give the C++ code, your Python code, the expected "
        "output (from the real C++ program) and the actual output or error.\n\n"
        "For each test: first state the cause of the failure in 1 or 2 lines, then give the corrected Python program. "
        "Do not change what the program is meant to do. Standard library only, no input().\n\n"
        "Output format for each test: a heading like ### T05, then a line starting with \"Cause:\", then ONE python code "
        "block with the FULL corrected program. Only include the tests listed below.\n"]
    for t in bad:
        a = actual[(t, "V1")].strip()
        a = a[-2500:] if a else "(no output)"
        parts.append(
            f"\n=====\n### {t}  (status: {result[(t, 'V1')]})\n\nC++ code:\n```cpp\n{read(ROOT / 'test-data' / 'tests' / t / 'program.cpp').rstrip()}\n```\n\n"
            f"Your Python code:\n```python\n{code[(t, 'V1')].rstrip()}\n```\n\n"
            f"Expected output:\n```\n{norm(read(ROOT / 'test-data' / 'tests' / t / 'expected_output.txt'))}\n```\n\n"
            f"Actual output or error:\n```\n{a}\n```\n")
    v2_prompt.parent.mkdir(parents=True, exist_ok=True)
    v2_prompt.write_text("".join(parts), encoding="utf-8")
elif v2_prompt.exists():
    v2_prompt.unlink()

print("\n>>> NEXT STEP:", end=" ")
if "V1" not in replies:
    print("Paste test-data/prompts_used/V1_prompt_FULL.txt into a NEW Claude chat,")
    print("    then save the whole reply as test-data/replies/V1.txt).")
elif auto_v2:
    print("V1 passed everything, so V2 was filled automatically with the V1 code (no fix round needed).")
    print("    ")
elif "V2" in replies:
    print("Everything is done. See test-data/results/.")
elif bad:
    print(f"V1 failed on {', '.join(bad)}.")
    print("    Paste test-data/generated/V2_prompt.txt into a NEW Claude chat, then save the reply as test-data/replies/V2.txt.")
else:
    print("Some tests are missing in the V1 reply (see the !! warning above). Fix test-data/replies/V1.txt first.")
