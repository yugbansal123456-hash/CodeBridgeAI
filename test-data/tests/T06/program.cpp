#include <iostream>
using namespace std;

int main() {
    int as[] = {7, -7, 7, -7, 0, 1, -1};
    int bs[] = {2, 2, -2, -2, 5, -3, 4};
    for (int i = 0; i < 7; i++) {
        cout << as[i] << " / " << bs[i] << " = " << as[i] / bs[i]
             << ", " << as[i] << " % " << bs[i] << " = " << as[i] % bs[i] << endl;
    }
    cout << -9 / 4 << " " << -9 % 4 << endl;
    int x = -17, y = 5;
    cout << "identity holds: " << ((x / y) * y + (x % y) == x) << endl;
    long long big = -10000000000LL;
    cout << big / 3 << " " << big % 3 << endl;
    return 0;
}
