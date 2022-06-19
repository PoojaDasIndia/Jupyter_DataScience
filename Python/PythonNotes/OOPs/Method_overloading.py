#method overload
"""class Myclass:
    def sum(self,a):
        print("Ist Sum method",a)

    def sum(self):
        print("IInd Sum method") # cant define 2 methos with same name
obj=Myclass()
obj.sum()
obj.sum(10)"""

print("\n1.***********************************\n")
class Myclass:
    def sum(self,a,b,c):
        s=a+b+c
        return s

obj=Myclass()
print(obj.sum(4,5,6))
# print(obj.sum(4,5)) # error c wala
# print(obj.sum(4)) # error b,c wala


print("\n2.***********************************\n")
class Myclass:
    def sum(self,a=None,b=None,c=None):
        s=a+b+c
        return s

obj=Myclass()
print(obj.sum(4,5,6))
# print(obj.sum(4,5)) # error type 
# print(obj.sum(4)) # error str type

print("\n3.***********************************\n")
class Myclass:
     def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a*b
        else:
            return "Provide atleast two Number"
            
        return s

obj=Myclass()
print(obj.sum(4,5,6))
print(obj.sum(4,5)) 
print(obj.sum(4)) 