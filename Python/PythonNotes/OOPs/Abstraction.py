"""
To understand this pillar better, let’s use the example of a car. 
People do not see a car as thousands of individual parts.
 Instead, they see it as a well-defined object with unique behavior. 
 They do not need to understand the complexity of those parts and how they collaborate.

In simple terms, abstraction hides the internal implementations of a process or method from the user.
 In this way, the user knows what they do but not how it is done.

In simple terms, abstraction hides the internal implementations of a process or method from the user.
 In this way, the user knows what they do but not how it is done.



Abstraction is a bit different from the other pillars. Python does not grant abstract classes by default.
 Instead, Python comes with a module that fits the base for Abstract Base classes (ABC).
 A method becomes abstract when decorated with the keyword @abstractmethod.

"""
 
# abstract base class work 

from abc import ABC,abstractmethod

#abstract class
class Car(ABC):

    #abstract method
    @abstractmethod  
    def mileage(self):
        pass

    def color(self):
        self.color="Red"
        print("Color : ",self.color)


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")

class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")  

class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")

class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")      


# Driver code   
t= Tesla ()   
t.mileage()
t.color()   
print("\n************************************\n")
r = Renault()   
r.mileage()   
r.color() 
print("\n************************************\n")  
s = Suzuki()   
s.mileage()  
s.color() 
print("\n************************************\n")
d = Duster()   
d.mileage() 
d.color() 

print("\n************************************\n")

class Company(ABC):

    def work(self):
        pass

class Manager(Company):

    def work(self):
        print("I assign work to and manage team")

class Employee(Company):

    def work(self):
        print("I complete the work assigned to me")

# Driver code
R = Manager()
R.work()

K = Employee()
K.work()
