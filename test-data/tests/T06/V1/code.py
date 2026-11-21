def cxx_div(a, b):
    """Integer division truncated toward zero, as in C++."""
    quotient = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        quotient = -quotient
    return quotient


def cxx_mod(a, b):
    """C++ remainder: a - trunc(a / b) * b."""
    return a - cxx_div(a, b) * b


a_values = [7, -7, 7, -7, 0, 1, -1]
b_values = [2, 2, -2, -2, 5, -3, 4]

for a, b in zip(a_values, b_values):
    print(
        f"{a} / {b} = {cxx_div(a, b)}, "
        f"{a} % {b} = {cxx_mod(a, b)}"
    )

print(cxx_div(-9, 4), cxx_mod(-9, 4))

x, y = -17, 5
identity = (cxx_div(x, y) * y + cxx_mod(x, y) == x)
print(f"identity holds: {int(identity)}")

big = -10000000000
print(cxx_div(big, 3), cxx_mod(big, 3))
