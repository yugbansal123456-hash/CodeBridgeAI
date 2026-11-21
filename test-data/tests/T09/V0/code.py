class Box:
    def __init__(self, v):
        self.v = v


# Python integers are immutable.
# This function changes only its local variable.
def by_value(x):
    x += 10


# Python has no direct C++ reference parameters.
# Return the modified value instead.
def by_ref(x):
    return x + 10


# Simulating pointer-like modification through a mutable container
def by_ptr(x):
    x[0] += 10


def box_by_value(b):
    # Simulate passing a copy of the object
    copied_box = Box(b.v)
    copied_box.v = 99
    print("inside boxByValue:", copied_box.v)


def box_by_ref(b):
    b.v = 99


def vec_by_value(v):
    # Simulate passing a copied list
    copied_vector = v.copy()
    copied_vector.append(4)


def vec_by_ref(v):
    v.append(4)


n = 1

by_value(n)
print("after byValue:", n)

n = by_ref(n)
print("after byRef:", n)

pointer = [n]
by_ptr(pointer)
n = pointer[0]
print("after byPtr:", n)

b = Box(1)

box_by_value(b)
print("box after boxByValue:", b.v)

box_by_ref(b)
print("box after boxByRef:", b.v)

v = [1, 2, 3]

vec_by_value(v)
print("vector size after vecByValue:", len(v))

vec_by_ref(v)
print("vector size after vecByRef:", len(v))

b1 = Box(1)
b2 = Box(b1.v)
b2.v = 2

print("b1.v =", b1.v, ", b2.v =", b2.v)

orig = [1, 2, 3]
dup = orig.copy()
dup[0] = 100

print("orig[0] =", orig[0], ", dup[0] =", dup[0])

# Simulating pointer and reference access
p = [n]
p[0] = 50
n = p[0]

print("n via pointer:", n)

r = [n]
r[0] = 60
n = r[0]

print("n via reference:", n)
