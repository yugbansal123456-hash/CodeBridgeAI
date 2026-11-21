#include <iostream>
using namespace std;

long long factorial(int n) { return n <= 1 ? 1 : n * factorial(n - 1); }
int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }

long long power(long long base, int exp) {
    if (exp == 0) return 1;
    long long half = power(base, exp / 2);
    return exp % 2 == 0 ? half * half : half * half * base;
}

int main() {
    cout << "10! = " << factorial(10) << endl;
    cout << "15! = " << factorial(15) << endl;
    cout << "Fibonacci:";
    for (int i = 0; i <= 10; i++) cout << " " << fib(i);
    cout << endl;
    cout << "gcd(48, 18) = " << gcd(48, 18) << endl;
    cout << "gcd(17, 5) = " << gcd(17, 5) << endl;
    cout << "2^30 = " << power(2, 30) << endl;
    cout << "3^13 = " << power(3, 13) << endl;
    return 0;
}
