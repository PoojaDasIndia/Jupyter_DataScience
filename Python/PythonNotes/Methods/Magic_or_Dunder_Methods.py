"""
__new__() method

Languages such as Java and C# use the new operator to create a new instance of a class. 

In Python the __new__() magic method is implicitly called before the __init__() method.
The __new__() method returns a new object, which is then initialized by __init__().

"""
# Magic methods in Python are the special methods that start and end with the double underscores.
#  They are also called dunder methods.

class Employee:
    def __new__(cls):
        print ("__new__ magic method is called")
        inst = object.__new__(cls)
        return  inst

    def __init__(self):
        print ("__init__ magic method is called")
        self.name='Satya'

emp = Employee()


"""
https://www.tutorialsteacher.com/python/magic-methods-in-python

https://rszalski.github.io/magicmethods

"""