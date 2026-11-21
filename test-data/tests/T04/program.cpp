#include <iostream>
#include <memory>
#include <string>
#include <vector>
using namespace std;

class Shape {
public:
    virtual ~Shape() {}
    virtual double area() const = 0;
    virtual string name() const { return "Shape"; }
};

class Rectangle : public Shape {
protected:
    double w, h;
public:
    Rectangle(double w_, double h_) : w(w_), h(h_) {}
    double area() const override { return w * h; }
    string name() const override { return "Rectangle"; }
};

class Square : public Rectangle {
public:
    explicit Square(double s) : Rectangle(s, s) {}
    string name() const override { return "Square"; }
};

class Circle : public Shape {
    double r;
public:
    explicit Circle(double r_) : r(r_) {}
    double area() const override { return 3.14 * r * r; }
    string name() const override { return "Circle"; }
};

int main() {
    vector<unique_ptr<Shape>> shapes;
    shapes.push_back(make_unique<Rectangle>(3, 4));
    shapes.push_back(make_unique<Square>(5));
    shapes.push_back(make_unique<Circle>(2));

    double total = 0;
    for (const auto& s : shapes) {
        cout << s->name() << " area = " << s->area() << endl;
        total += s->area();
    }
    cout << "Total area = " << total << endl;
    return 0;
}
