# Recursive factorial
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


# Recursive Fibonacci
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


# Recursive GCD
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


# Recursive power using exponentiation by squaring
def power(base, exp):
    if exp == 0:
        return 1

    half = power(base, exp // 2)

    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base


print("10! =", factorial(10))
print("15! =", factorial(15))

print("Fibonacci:", end="")
for i in range(11):
    print(f" {fib(i)}", end="")
print()

print("gcd(48, 18) =", gcd(48, 18))
print("gcd(17, 5) =", gcd(17, 5))

print("2^30 =", power(2, 30))
print("3^13 =", power(3, 13))
