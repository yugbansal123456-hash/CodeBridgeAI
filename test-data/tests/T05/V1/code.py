def biggest(a, b):
    return a if a > b else b


def sum_all(values):
    total = values[0] - values[0] if values else 0
    for value in values:
        total = total + value
    return total


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0


print(biggest(3, 9))
print(format(biggest(2.5, 1.5), ".6g"))
print(biggest("pear", "apple"))

print(sum_all([1, 2, 3, 4]))
print(format(sum_all([1.5, 2.5, 3.0]), ".6g"))
print(sum_all(["a", "b", "c"]))

st = Stack()
st.push(10)
st.push(20)
st.push(30)

while not st.empty():
    print(st.pop(), end=" ")
print()
