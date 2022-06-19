"""
This method is used to access or read data of the variables.
 This method do not modify the data in the variable.
 This is also called as getter method
"""
class car:

    def __init__(self):
        self.model= "x20" # Instance Varible always wrriten inside __init__

    

    def getter(self): # Accessor Instance Method with parameter
        
        return f"Model :{self.model} " #accessing instance varible


Maruti=car()
m=Maruti.getter()
print(m)
