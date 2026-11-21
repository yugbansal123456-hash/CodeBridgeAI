# C++ integer division truncates toward zero.
# Python's // uses floor division, so we implement C++ behavior.

def cpp_div(a, b):
    return int(a / b)


def cpp_mod(a, b):
    return a - cpp_div(a, b) * b


as_values = [7, -7, 7, -7, 0, 1, -1]
bs_values = [2, 2, -2, -2, 5, -3, 4]

for i in range(7):
    a = as_values[i]
    b = bs_values[i]

    print(
        a, "/", b, "=", cpp_div(a, b),
        ",", a, "%", b, "=", cpp_mod(a, b)
    )

print(cpp_div(-9, 4), cpp_mod(-9, 4))

x = -17
y = 5

print(
    "identity holds:",
    cpp_div(x, y) * y + cpp_mod(x, y) == x
)

big = -10000000000

print(cpp_div(big, 3), cpp_mod(big, 3))
