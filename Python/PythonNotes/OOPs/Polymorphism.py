#Polymorphism: The condition of occurrence in several different forms.

"""To understand the polymorphism pillar, let’s use the cartoon character Ben 10 as an example.
 He is one person, but he serves the world in multiple forms.

So, in programming terms, polymorphism refers to the use of a single method/operator to represent different types in different scenarios."""

class Class1():

    def pt(self): 
        print("This function determines class 1") 


class Class2(): 
    def pt(self): 
        print("This function determines class 2.") 

obj1 = Class1() 
obj2 = Class2() 
obj1 = Class1()

for type in (obj1, obj2,obj1): 
# creating a loop to iterate through the obj1, obj2
    type.pt()


"""
This works similarly for operators.
 Let’s look at the + operator.

> print(1+2)
3
> print ("a"+"b")
> ab
As you see, the + operator behaves in a different way with different datatypes.


""" 
