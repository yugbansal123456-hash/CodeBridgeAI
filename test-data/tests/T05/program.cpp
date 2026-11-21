#include <iostream>
#include <string>
#include <vector>
using namespace std;

template <typename T>
T biggest(T a, T b) {
    return a > b ? a : b;
}

template <typename T>
T sumAll(const vector<T>& v) {
    T total = T();
    for (const T& x : v) total = total + x;
    return total;
}

template <typename T>
struct Stack {
    vector<T> items;
    void push(T x) { items.push_back(x); }
    T pop() {
        T t = items.back();
        items.pop_back();
        return t;
    }
    bool empty() const { return items.empty(); }
};

int main() {
    cout << biggest(3, 9) << endl;
    cout << biggest(2.5, 1.5) << endl;
    cout << biggest(string("pear"), string("apple")) << endl;

    cout << sumAll(vector<int>{1, 2, 3, 4}) << endl;
    cout << sumAll(vector<double>{1.5, 2.5, 3.0}) << endl;
    cout << sumAll(vector<string>{"a", "b", "c"}) << endl;

    Stack<int> st;
    st.push(10);
    st.push(20);
    st.push(30);
    while (!st.empty()) cout << st.pop() << " ";
    cout << endl;
    return 0;
}
