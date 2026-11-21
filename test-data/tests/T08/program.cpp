#include <iomanip>
#include <iostream>
using namespace std;

int main() {
    double third = 1.0 / 3;
    cout << third << endl;
    cout << 2.0 << endl;
    cout << 100.0 / 7 << endl;
    cout << 1234567.891 << endl;
    cout << 0.00001234 << endl;
    cout << 1e10 << endl;
    float f = 0.1f;
    cout << f << endl;
    cout << 5 / 2 << " " << 5 / 2.0 << endl;

    cout << fixed << setprecision(2) << 3.14159 << " " << 2.0 << endl;
    cout << setprecision(10) << third << endl;
    cout << defaultfloat << setprecision(6);

    cout << setw(8) << setfill('*') << 42 << endl;
    cout << setfill(' ') << left << setw(6) << "ab" << "|" << endl;
    cout << right << setw(6) << "ab" << "|" << endl;
    cout << scientific << setprecision(3) << 12345.6789 << endl;
    return 0;
}
