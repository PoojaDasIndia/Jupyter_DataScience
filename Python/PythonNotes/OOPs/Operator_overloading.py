print(10+20)

# int.__add__(self,other)
print(int.__add__(10,20))

print("Pooja"+"Das")

# str.__add__(self,other)
print(str.__add__("Pooaj","Das"))


print("*************************************")

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        return self.x+other.x

    # if we not do this TypeError: unsupported operand type(s) for +: 'A' and 'B'

class B:
    def __init__(self,x):
        self.x=x

a=A(100)
b=B(200)
print(a+b)   #A.__add__(self,other)
