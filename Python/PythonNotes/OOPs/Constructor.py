"""
The constructor function in python is called __new__ and __init__ is the initializer function.

 __new__ is used when you need to control the creation of a new instance .
while __init__ is used when you need to control the initialization of a new instance.

__new__ is the first step of instance creation.
 It's called first and is responsible for returning a new instance of your class.

In contrast, __init__ doesn't return anything; it's only responsible for initializing the instance 
after it's been created.

"""

#Example 1: Using __init__

class Point:

    def __init__(self, data):
        self.num = data

    def print_num(self):
        print(self.num)



obj = Point(100)

obj.print_num()

"""
Note: The self parameter is a reference to the current instance of the class and is used to access variables that belong to the class.

"""

# Example 2:
class Person:

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.instance_method()

    def instance_method(self):
        print('success!')

Obj = Person()

"""
Notice that __init__ receives the argument self, while __new__ receives the class (cls). Since self is a reference to the instance, this should tell you quite evidently that the instance is already created by the time __init__ gets called, since it gets passed the instance. It's also possible to call instance methods precisely because the instance has already been created.


"""