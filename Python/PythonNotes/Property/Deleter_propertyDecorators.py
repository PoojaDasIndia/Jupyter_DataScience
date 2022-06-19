# Property Deleter
# @property-name.deleter 

class Student:

    def __init__(self, name):
        self.__name=name

    @property             #getter property decorator
    def fun_name(self):
        return self.__name

    @fun_name.setter
    def fun_name(self,value): #property-name.setter decorator
        self.__name=value

    @fun_name.deleter
    def fun_name(self): #property-name.deleter decorator
        print("Deleting.....")
        del self.__name


    
#Access Property decorator   

s=Student("Pooja")
print(s.fun_name)

#Access setter Property decorator 
s.fun_name="Das"
print(s.fun_name)

#Access Deleter Property decorator 
del s.fun_name
print(s.fun_name)



"""
The deleter would be invoked when you delete the property using keyword del, as shown below. 
Once you delete a property, you cannot access it again using the same instance.

"""