"""
In Python, Namespace represents a memory block where names are mapped to objects.

Class Namespace – A class maintains it’s own namespace known as class namespace. In the class namespace, the names are mapped to class variables. 

Instance Namespace – Every instance have it’s own namespace known as instance namespace. In the instance namespace, the names are mapped to instance variables. 
"""

class car:
    light="yess phale  tha class  var"

    @classmethod
    def is_light(cls):
        print("Light :",cls.light)



Maruti=car()
Tata=car()

print("Maruti",car.light) 
print("Tata",car.light)
print()

print("***************************************\n")
car.light="No after changing"      
 # no is class namespace
 #maruti and tata is instance namespace
print("Maruti",car.light) 
print("Tata",car.light)

print("***************************************\n")

Maruti.light="Tata Not working , Maruti work"       
print("Maruti",Maruti.light) 
print("Tata",Tata.light)

print("***************************************\n")
Tata.light="Maruti Not working , Tata work"
print("Maruti",Maruti.light) 
print("Tata",Tata.light) 
print("************************************\n")
print(car.light)

