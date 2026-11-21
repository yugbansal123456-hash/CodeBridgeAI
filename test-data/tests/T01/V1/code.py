total = sum(range(1, 11))
print(f"Sum 1..10 = {total}")

evens = sum(i for i in range(1, 21) if i % 2 == 0)
print(f"Sum of evens up to 20 = {evens}")

n = 5
fact = 1
while n > 1:
    fact *= n
    n -= 1
print(f"5! = {fact}")

for i in range(1, 4):
    print(" ".join(str(i * j) for j in range(1, 4)))

countdown = 3
while True:
    print(f"T-{countdown}")
    countdown -= 1
    if countdown <= 0:
        break
