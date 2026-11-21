# CodeBridge AI: checking C++ to Python translations

Team ID PE-B37-09 | Team CodeBridge AI | Batch 41 | SCSE4041 Mini Project, Bennett University

## What this project is
We asked Claude to translate C++ programs into Python. A translated program can run fine and still print
something different from the C++ program. So we check every translation: we run the real C++ program and the
Python program and compare what they print. If the text is exactly the same, the test passes.

We tried 3 prompts on 10 test programs (4 ordinary ones and 6 tricky ones):

| Version | What we asked Claude | Tests passed |
|---|---|---|
| V0 | A plain request: translate this C++ program to Python | 4 of 10 (40%) |
| V1 | A better prompt: a role, rules, a checklist of 7 C++ habits, one example and a request for short notes | 9 of 10 (90%) |
| V2 | V1, then a repair prompt that shows Claude the failed test, the expected output and the real error | 10 of 10 (100%) |

This is a small sample: 10 programs and one run per version. Passing means the output is identical. It does not
prove the translation is a perfect rewrite.

## Try it (prototype)
Colab link: https://colab.research.google.com/drive/1FSYZFexydcGOgAgzGrLotA0c8HQMDdSy?usp=sharing

Open the link and click Runtime, then Run all. It takes about a minute and needs no login. The notebook calls no
AI. It loads Claude's saved translations and checks them, and it explains each step in plain words.

To run it on your own computer: install Python 3 and type `python code/run.py` in this folder.

## What is in each folder
```
README.md       this file
CHANGELOG.md    what we changed and when
prompts/
  V0/           the plain prompt
  V1/           the better prompt (P1)
  V2/           the repair prompt (P2)
  final/        the 2 final prompts: P1_translate.txt and P2_repair.txt
code/
  run.py        the script that runs and checks the translations
  CodeBridgeAI_Prototype.ipynb   the Colab notebook
test-data/
  tests/T01 to T10/   one folder per test: the C++ program, the correct output,
                      and V0, V1, V2 folders with the Python code, its output and PASS / WRONG / ERROR
  replies/            Claude's replies as we saved them (V0.txt, V1.txt, V2.txt)
  results/            results.csv, summary.txt, failures.txt
  prompts_used/       the full prompts we pasted into Claude
docs/           the 4 diagrams and the Milestone 2 PDF
```
Note: `V2_prompt_FULL_reconstructed.txt` was rebuilt by the script from the real V1 replies. Only the file paths inside
the error message are different from the prompt we pasted on our own computer.

## Team
- Yug Bansal (S24CSEU0261), team leader
- Ruchit (S24CSEU2645)

## Model and AI help
- Model used for the experiments:Claude Sonnet 5.5, using the High effort reasoning setting in the Claude web application
- Claude also helped us write the test programs, the prompts and the script. We ran all experiments ourselves in new
  Claude chats and saved the replies without changing them.
- The correct outputs come from compiling and running each C++ program with g++ 13.3.0 (C++17).

## Limits
We sent all 10 programs of a version in one chat. We only compare printed output, so a translation can pass without
being a faithful rewrite (for example, the T10 translations print the destructor messages directly). We ran each
version once, so the results may change on another run.
