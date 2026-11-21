# Generic equivalent: biggest()
def biggest(a, b):
    return a if a > b else b


# Generic equivalent: sumAll()
def sum_all(v):
    total = v[0] * 0 if v else 0

    for x in v:
        total = total + x

    return total


# Stack implementation using a list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0


print(biggest(3, 9))
print(biggest(2.5, 1.5))
print(biggest("pear", "apple"))

print(sum_all([1, 2, 3, 4]))
print(sum_all([1.5, 2.5, 3.0]))
print(sum_all(["a", "b", "c"]))

st = Stack()
st.push(10)
st.push(20)
st.push(30)

while not st.empty():
    print(st.pop(), end=" ")

print()
