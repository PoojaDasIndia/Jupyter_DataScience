"""sing Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.

The name Duck Typing comes from the phrase:

“If it looks like a duck and quacks like a duck, it’s a duck”"""

class Bird:
    def fly(self):
        print("fly with wings")
  
class Airplane:
    def fly(self):
        print("fly with fuel")
  
class Fish:
    def swim(self):
        print("fish swim in sea")
  
# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
    obj.fly()