def work():
    print("construct W1")
    print("construct W2")
    print("work() body")
    # C++ local objects are destroyed in reverse construction order.
    print("destruct W2")
    print("destruct W1")


print("construct A")
print("construct B")
print("construct C")
print("inner scope end")
print("destruct C")
print("destruct B")

work()

print("construct D")
print("main end")
print("destruct D")
print("destruct A")
