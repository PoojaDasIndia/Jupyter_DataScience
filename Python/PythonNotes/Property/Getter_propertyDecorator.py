"""
The @property decorator is a built-in decorator in Python for the property() function. Use @property decorator on any method in the class to use the method as a property.

You can use the following three decorators to define a property:

@property: Declares the method as a property.
@<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
@<property-name>.deleter: Specifies the delete method as a property that deletes a property.

"""


# Declare a Property (getter)

class Student:

    def __init__(self, name):
        self.__name=name

    @property             #getter property decorator
    def fun_name(self):
        return self.__name

#Access Property decorator   

s=Student("Pooja")
print(s.fun_name)



"""
Above, @property decorator applied to the name() method.
The name() method returns the private instance attribute value __name. 
So, we can now use the name() method as a property to get the value of the __name attribute, as shown below.

"""
