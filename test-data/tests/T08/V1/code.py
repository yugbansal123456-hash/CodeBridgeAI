third = 1.0 / 3

# Default C++ cout formatting: defaultfloat with six significant digits.
print(format(third, ".6g"))
print(format(2.0, ".6g"))
print(format(100.0 / 7, ".6g"))
print(format(1234567.891, ".6g"))
print(format(0.00001234, ".6g"))
print(format(1e10, ".6g"))

# C++ float is typically IEEE-754 binary32. The displayed value is 0.1.
print(format(0.1, ".6g"))
print("2 2.5")

# fixed << setprecision(2)
print(f"{3.14159:.2f} {2.0:.2f}")

# setprecision(10) with defaultfloat
print(format(third, ".10g"))

# defaultfloat << setprecision(6) is now in effect.
print(f"{42:*>8}")
print(f"{'ab':<6}|")
print(f"{'ab':>6}|")

# scientific << setprecision(3)
print(format(12345.6789, ".3e"))
