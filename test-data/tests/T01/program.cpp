#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    for (int i = 1; i <= 10; i++) {
        sum += i;
    }
    cout << "Sum 1..10 = " << sum << endl;

    int evens = 0;
    for (int i = 1; i <= 20; i++) {
        if (i % 2 == 0) evens += i;
    }
    cout << "Sum of evens up to 20 = " << evens << endl;

    int n = 5, fact = 1;
    while (n > 1) {
        fact *= n;
        n--;
    }
    cout << "5! = " << fact << endl;

    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << i * j;
            if (j < 3) cout << " ";
        }
        cout << endl;
    }

    int countdown = 3;
    do {
        cout << "T-" << countdown << endl;
        countdown--;
    } while (countdown > 0);
    return 0;
}
