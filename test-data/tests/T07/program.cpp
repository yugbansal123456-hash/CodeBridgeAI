#include <cstdint>
#include <iostream>
using namespace std;

int main() {
    unsigned int u = 0;
    u -= 1;
    cout << "0u - 1 = " << u << endl;

    uint8_t b = 250;
    b += 10;
    cout << "250 + 10 as uint8_t = " << static_cast<int>(b) << endl;

    uint8_t c = 65;
    cout << "uint8_t 65 printed directly: " << c << endl;
    cout << "uint8_t 65 printed with +: " << +c << endl;

    uint32_t x = 4000000000u;
    x += 500000000u;
    cout << "4000000000 + 500000000 as uint32_t = " << x << endl;

    uint16_t h = 65535;
    h++;
    cout << "uint16_t 65535 + 1 = " << h << endl;

    unsigned char ch = 'a';
    ch = static_cast<unsigned char>(ch - 32);
    cout << "uppercase: " << ch << endl;

    unsigned int big = 3000000000u;
    cout << "3000000000u * 2 = " << big * 2 << endl;

    unsigned int s = 5, t = 10;
    cout << "5u - 10u = " << s - t << endl;
    cout << "(5u - 10u) > 0 is " << (s - t > 0) << endl;
    return 0;
}
