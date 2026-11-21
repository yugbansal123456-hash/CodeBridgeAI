def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def power(base, exp):
    if exp == 0:
        return 1
    half = power(base, exp // 2)
    return half * half if exp % 2 == 0 else half * half * base


print(f"10! = {factorial(10)}")
print(f"15! = {factorial(15)}")

print("Fibonacci:", end="")
for i in range(11):
    print(f" {fib(i)}", end="")
print()

print(f"gcd(48, 18) = {gcd(48, 18)}")
print(f"gcd(17, 5) = {gcd(17, 5)}")
print(f"2^30 = {power(2, 30)}")
print(f"3^13 = {power(3, 13)}")
