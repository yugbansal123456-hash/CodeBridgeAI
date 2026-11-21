#include <iostream>
#include <string>
using namespace std;

struct Tracker {
    string name;
    explicit Tracker(const string& n) : name(n) { cout << "construct " << name << endl; }
    ~Tracker() { cout << "destruct " << name << endl; }
};

void work() {
    Tracker w1("W1");
    Tracker w2("W2");
    cout << "work() body" << endl;
}

int main() {
    Tracker a("A");
    {
        Tracker b("B");
        Tracker c("C");
        cout << "inner scope end" << endl;
    }
    work();
    Tracker d("D");
    cout << "main end" << endl;
    return 0;
}
