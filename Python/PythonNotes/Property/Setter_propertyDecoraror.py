# Property Setter

#using @property-name.setter

class Student:

    def __init__(self, name):
        self.__name=name

    @property             #getter property decorator
    def fun_name(self):
        return self.__name

    @fun_name.setter
    def fun_name(self,value): #property-name.setter decorator
        self.__name=value

#Access Property decorator   

s=Student("Pooja")
print(s.fun_name)

#Access setter Property decorator 
s.fun_name="Das"
print(s.fun_name)

