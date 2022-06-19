import weakref


class car:
    def __init__(self,w):
        self.wheel=w

    def getWheels(self):
        return self.wheel


c1=car(4)
print("c1 memory location:",hex(id(c1)))
r=weakref.ref(c1)

print("Before :",r)
c1=None

print("After :",r)
print("Garbage Collected Immediately")