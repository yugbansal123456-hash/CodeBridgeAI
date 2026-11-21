# Floating-point values
third = 1.0 / 3

print(third)
print(2.0)
print(100.0 / 7)
print(1234567.891)
print(0.00001234)
print(1e10)

# Python float is double precision.
# C++ float has lower precision.
f = 0.1
print(f"{f:.8g}")

# Integer division and floating-point division
print(5 // 2, 5 / 2.0)

# Fixed notation with 2 decimal places
print(f"{3.14159:.2f} {2.0:.2f}")

# Precision of 10 significant digits
print(f"{third:.10g}")

# Default floating-point notation, 6 significant digits
# Width and fill formatting
print(f"{42:*>8}")

# Left alignment
print(f"{'ab':<6}|")

# Right alignment
print(f"{'ab':>6}|")

# Scientific notation with 3 digits after decimal
print(f"{12345.6789:.3e}")
