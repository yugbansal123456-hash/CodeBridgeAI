class Tracker:
    def __init__(self, name):
        self.name = name
        print("construct", self.name)

    def destroy(self):
        print("destruct", self.name)


def work():
    w1 = Tracker("W1")
    w2 = Tracker("W2")

    print("work() body")

    # C++ destroys local objects in reverse construction order
    w2.destroy()
    w1.destroy()


a = Tracker("A")

# Simulating an inner scope
b = Tracker("B")
c = Tracker("C")

print("inner scope end")

# Destruction in reverse order
c.destroy()
b.destroy()

work()

d = Tracker("D")

print("main end")

# Destruction in reverse order at end of main
d.destroy()
a.destroy()
