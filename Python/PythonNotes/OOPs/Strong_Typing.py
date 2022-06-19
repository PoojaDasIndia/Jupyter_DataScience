# hasattr(obj,"method_name") for checking

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
    if hasattr(obj,"fly"):  # strong type for checking 
        obj.fly()
    else:
        obj.swim()