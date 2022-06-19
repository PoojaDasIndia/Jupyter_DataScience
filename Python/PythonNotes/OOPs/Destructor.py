"""
Just like a constructor is used to create and initialize an object
, a destructor is used to destroy the object and perform the final clean up.

"""
# where we have used the __init__ method to initialize our object, 
# while we have defined the __del__ method to act as a destructor.

class Foo():
    def __init__(self, bar):
        self.id = 45
        # saving reference of Bar object
        self.friend = bar
        print ('Foo', self.id, 'born')

    def __del__(self):
        print ('Foo', self.id, 'died')

# creating an object
myObj = Foo(7)
print(myObj.id)
print(myObj.friend)
 
# to delete the object explicitly

del myObj   # del keyword
print(myObj.id)
print(myObj.friend)