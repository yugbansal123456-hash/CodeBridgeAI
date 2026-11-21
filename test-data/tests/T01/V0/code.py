# Sum of numbers from 1 to 10
total = 0
for i in range(1, 11):
    total += i

print("Sum 1..10 =", total)

# Sum of even numbers up to 20
evens = 0
for i in range(1, 21):
    if i % 2 == 0:
        evens += i

print("Sum of evens up to 20 =", evens)

# Factorial using while loop
n = 5
fact = 1

while n > 1:
    fact *= n
    n -= 1

print("5! =", fact)

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" " if j < 3 else "")
    print()

# Countdown (do-while equivalent)
countdown = 3

while True:
    print("T-" + str(countdown))
    countdown -= 1

    if countdown <= 0:
        break
