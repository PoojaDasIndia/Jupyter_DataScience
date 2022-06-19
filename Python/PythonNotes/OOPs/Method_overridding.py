print("**************method overridiing*************\n")
class Add:
    def result(self,a,b):
         print( "Addition : ",a+b)


class multi(Add):
    def result(self,a,b):  # method overridiing hai 
        print("Multiplication : ",a*b)

print("****Creating son object***\n")
m=multi()
m.result(10,20)

print("\n*****Creating parents objec****t\n")
a=Add()
a.result(50,20)

print("**************method overridiing Solution With super()*************\n")

class Add:
    def result(self,a,b):
        print( "Addition : ",a+b)

class multi(Add):
    def result(self,a,b): 
        super().result(50,20) # solution calling parent method also
        print( "Multiplication : ",a*b)

m=multi()
m.result(10,20)