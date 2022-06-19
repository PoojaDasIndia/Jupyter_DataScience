"""
This method is used to access or read and modify data of the variables.
This method modify the data in the variable.
This is also called as setter method.
"""

from pyexpat import model


class car:

    def __init__(self):
        self.model= "X20" # Instance Varible 
        
        
    def setter(self): # Mutator Instance Method 
        self.model="X45"  #Instance Varible
        


Maruti=car()
print("Before Setter :",Maruti.model)

# calling setter function
Maruti.setter()

print("\nAfter Setter :",Maruti.model)


print("********************************************************")

class car:

    def __init__(self,model):
        self.model= model # Instance Varible always wrriten inside __init__

    

    def setter(self,colour): # Mutator Instance Method with parameter
        self.colour=colour  #Instance Varible
        return f"Model :{self.model} and colour : {self.colour}"  #accessing instance varible


Maruti=car("x20")
Maruti.setter("Red")
print("Model :",Maruti.model)
print("Color :",Maruti.colour)



