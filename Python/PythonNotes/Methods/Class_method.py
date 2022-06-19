"""
Class methods are the methods which act upon the class variables or static variable of the class.
Decorator @classmethod need to write above the class method.
By default, the first parameter of class method is cls which refers to the class itself.

************************************************************************************

The @classmethod is an alternative of the classmethod() function.
It is recommended to use the @classmethod decorator instead of the function because it is just a syntactic sugar.

@classmethod Characteristics
1. Declares a class method.
2. The first parameter must be cls, which can be used to access class attributes.
3. The class method can only access the class attributes but not the instance attributes.
4. The class method can be called using ClassName.MethodName() and also using object.
5. It can return an object of the class.


"""
print("***************Without class variable**********************")

class car:
    @classmethod #decoator
    def show_method(cls): #class method
        return"X45"

tata=car()
print(tata.show_method()) #calling class method



print("***************with class variable**********************")

class car:

    model="X45" # calss varible

    @classmethod #decoator
    def show_method(cls): #class method
        print( "Model :",cls.model)

tata=car()
car.show_method() #calling class method

print("***************With parameter**********************")

class car:

    model="X45" # calss varible

    @classmethod #decoator
    def show_method(cls,color): #class method
        cls.color=color
        print( "Model :",cls.model,"color :",cls.color)

tata=car()
car.show_method("Red") #calling class method