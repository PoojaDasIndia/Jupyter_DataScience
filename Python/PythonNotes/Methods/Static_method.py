"""
Static Methods are used when some processing is related to the class
but does not need the class or its instances to perform any work. 

We use static method when we want to pass some values from outside 
and perform some action in the method.

Decorator @staticmethod need to write above the static method.

**************************************************************************************
@staticmethod Characteristics

1. Declares a static method in the class.
2. It cannot have cls or self parameter.
3. The static method cannot access the class attributes or the instance attributes.
4. The static method can be called using ClassName.MethodName() and also using object.MethodName().
5. It can return an object of the class.

"""



print("****************without  static varible *************")
class car:
    @staticmethod  #decorator
    def show_model(): #static method
        print("x45")

tata= car()
car.show_model()  #calling static method

print("****************with  static varible *************")
class car:
    model="x20"

    @staticmethod  #decorator
    def show_model(): #static method     cls ka need nhi h class k name se access hoga
        print("model :",car.model)  # class name se  access

tata= car()
car.show_model()  #calling static method

print("****************with Parameter *************")
class car:
    model="x20"

    @staticmethod  #decorator
    def show_model(color): #static method  parameter k sath self ka need nhi h 
        c=color
        print("model :",car.model,"color :",c)

tata= car()
car.show_model("red")  #calling static method  class se hi call hoga
print(car.model)