MASK8 = (1 << 8) - 1
MASK16 = (1 << 16) - 1
MASK32 = (1 << 32) - 1

u = (0 - 1) & MASK32
print(f"0u - 1 = {u}")

b = (250 + 10) & MASK8
print(f"250 + 10 as uint8_t = {b}")

c = 65
print(f"uint8_t 65 printed directly: {chr(c)}")
print(f"uint8_t 65 printed with +: {c}")

x = (4000000000 + 500000000) & MASK32
print(f"4000000000 + 500000000 as uint32_t = {x}")

h = (65535 + 1) & MASK16
print(f"uint16_t 65535 + 1 = {h}")

ch = ord("a")
ch = (ch - 32) & MASK8
print(f"uppercase: {chr(ch)}")

big = 3000000000
product = (big * 2) & MASK32
print(f"3000000000u * 2 = {product}")

s, t = 5, 10
difference = (s - t) & MASK32
print(f"5u - 10u = {difference}")
print(f"(5u - 10u) > 0 is {int(difference > 0)}")
