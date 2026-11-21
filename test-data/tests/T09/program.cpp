#include <iostream>
#include <vector>
using namespace std;

struct Box {
    int v;
};

void byValue(int x) { x += 10; }
void byRef(int& x) { x += 10; }
void byPtr(int* x) { *x += 10; }
void boxByValue(Box b) { b.v = 99; cout << "inside boxByValue: " << b.v << endl; }
void boxByRef(Box& b) { b.v = 99; }
void vecByValue(vector<int> v) { v.push_back(4); }
void vecByRef(vector<int>& v) { v.push_back(4); }

int main() {
    int n = 1;
    byValue(n);
    cout << "after byValue: " << n << endl;
    byRef(n);
    cout << "after byRef: " << n << endl;
    byPtr(&n);
    cout << "after byPtr: " << n << endl;

    Box b{1};
    boxByValue(b);
    cout << "box after boxByValue: " << b.v << endl;
    boxByRef(b);
    cout << "box after boxByRef: " << b.v << endl;

    vector<int> v = {1, 2, 3};
    vecByValue(v);
    cout << "vector size after vecByValue: " << v.size() << endl;
    vecByRef(v);
    cout << "vector size after vecByRef: " << v.size() << endl;

    Box b1{1};
    Box b2 = b1;
    b2.v = 2;
    cout << "b1.v = " << b1.v << ", b2.v = " << b2.v << endl;

    vector<int> orig{1, 2, 3};
    vector<int> dup = orig;
    dup[0] = 100;
    cout << "orig[0] = " << orig[0] << ", dup[0] = " << dup[0] << endl;

    int* p = &n;
    *p = 50;
    cout << "n via pointer: " << n << endl;
    int& r = n;
    r = 60;
    cout << "n via reference: " << n << endl;
    return 0;
}
