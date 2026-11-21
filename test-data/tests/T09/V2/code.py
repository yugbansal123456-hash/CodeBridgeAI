class Box:
    def __init__(self, value):
        self.v = value


def by_value(x):
    # Rebinding a local integer does not change the caller's integer.
    x += 10


def by_ref(cell):
    cell[0] += 10


def by_ptr(cell):
    cell[0] += 10


def box_by_value(box):
    # Simulate the copy made by passing a C++ struct by value.
    copied_box = Box(box.v)
    copied_box.v = 99
    print(f"inside boxByValue: {copied_box.v}")


def box_by_ref(box):
    box.v = 99


def vec_by_value(values):
    # Simulate the independent vector copy made by C++ pass-by-value.
    copied_values = values.copy()
    copied_values.append(4)


def vec_by_ref(values):
    values.append(4)


n = [1]  # A mutable cell lets the reference/pointer examples change the value.
by_value(n[0])
print(f"after byValue: {n[0]}")

by_ref(n)
print(f"after byRef: {n[0]}")

by_ptr(n)
print(f"after byPtr: {n[0]}")

b = Box(1)
box_by_value(b)
print(f"box after boxByValue: {b.v}")
box_by_ref(b)
print(f"box after boxByRef: {b.v}")

v = [1, 2, 3]
vec_by_value(v)
print(f"vector size after vecByValue: {len(v)}")
vec_by_ref(v)
print(f"vector size after vecByRef: {len(v)}")

b1 = Box(1)
b2 = Box(b1.v)
b2.v = 2
print(f"b1.v = {b1.v}, b2.v = {b2.v}")

orig = [1, 2, 3]
dup = orig.copy()
dup[0] = 100
print(f"orig[0] = {orig[0]}, dup[0] = {dup[0]}")

n[0] = 50  # Simulates writing through a pointer.
print(f"n via pointer: {n[0]}")
n[0] = 60  # Simulates writing through a reference.
print(f"n via reference: {n[0]}")
