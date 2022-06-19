# Encapsulation: To enclose something in or as if in a capsule.

print("****************without Encapsulation****************************")

class Cat:

    #Attibute / method
    # self ko mat dekho   ye  bus aga aga object k leye hai 
    # __init__ constructor hai

    def __init__(self):
        self.sound="Meow"

    #method

    def speak(self):
        print(f"Cat say: {self.sound}")   

#calling class
c=Cat()
c.speak() 
print("After change value") 
c.sound = "bow-wow"
c.speak() 

print("***********with Encapsulation**************")

class Cat:

    #Attibute / method
    # self ko mat dekho   ye  bus aga aga object k leye hai 
    # __init__ constructor hai

    #_protect karna
    #__private karna

    def __init__(self):
        self.__sound="Meow"

    #method

    def speak(self):
        print(f"Cat say: {self.__sound}")   

#calling class
c=Cat()
c.speak() 
print("After change value") 
c.sound = "bow-wow"
c.speak()

