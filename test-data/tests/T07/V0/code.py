# Simulating C++ unsigned integer types using bit masks.

# unsigned int: 32-bit
u = 0
u = (u - 1) & 0xFFFFFFFF

print("0u - 1 =", u)

# uint8_t: 8-bit
b = 250
b = (b + 10) & 0xFF

print("250 + 10 as uint8_t =", b)

c = 65

print("uint8_t 65 printed directly:", chr(c))
print("uint8_t 65 printed with +:", +c)

# uint32_t: 32-bit
x = 4000000000
x = (x + 500000000) & 0xFFFFFFFF

print("4000000000 + 500000000 as uint32_t =", x)

# uint16_t: 16-bit
h = 65535
h = (h + 1) & 0xFFFF

print("uint16_t 65535 + 1 =", h)

# Unsigned character conversion
ch = ord('a')
ch = (ch - 32) & 0xFF

print("uppercase:", chr(ch))

# unsigned int multiplication
big = 3000000000
result = (big * 2) & 0xFFFFFFFF

print("3000000000u * 2 =", result)

# Unsigned subtraction
s = 5
t = 10

difference = (s - t) & 0xFFFFFFFF

print("5u - 10u =", difference)
print("(5u - 10u) > 0 is", difference > 0)
