"""
Class variables are the variables whose single copy is available to all the instance of the class. 
If we modify the copy of class variable in an instance, it will effect all the copies in the other instance.
"""

class car:

    light="yes"  #class varible

    def __init__(self):
        self.model="x20" # Instance Varible always wrriten inside __init__

    

    def show(self): #Instance Method
        print("Model :",self.model) #accessing instance varible

        
    @classmethod           #class method
    def is_light(cls):
        print("Light :",cls.light)  #accessing class varible
    
    """
    With Class Method
    To access class variable,
     we need class methods with cls as first parameter then we can access class variable using cls.variable_name

    """
       

Maruti=car()
Maruti.show()
car.is_light() # calling class method
print()
tata=car()
tata.show()
print()
car.light="No"
car.is_light()

