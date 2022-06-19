#passing member of one class to another class

class Student:

    #constructor
    def __init__(self,n,r):
        self.name=n
        self.roll=r
    
    #instance method
    def display(self):
        print("Student name :",self.name)
        print("Student name :",self.roll)


class User:

    #static method
    @staticmethod
    def show(s): #stu bhi lekh skte h
        print( f"User name: {s.name}") #s.name mtlb stu.name hai
        print( f"roll no: {s.roll}")
        s.display()

#creating object of student class
stu=Student("Pooja",7)
print(stu.name)
User.show(stu)

