
#constractor overiding
class Father:
    def __init__(self):
        self.money=1000
        print("Father classs constructor")

    def show(self):
        return "Father class Instance method",self.money

class Son(Father):
    def __init__(self):
        self.money=5000
        print("Son classs constructor")

        
    def disp(self):
        return "Son class Instance Method",self.money

print("After crerating Son ka object\n")
s=Son()
print(s.money)
print(s.show()) # father ka constructor initilazied nhi hua
print(s.disp())

print("After crerating Parent ka object\n")
f=Father()
print(f.money)
print(f.show()) # father ka constructor initilazied nhi hua

print("\n*************************SOULTION BY CALLING SUPER*********************************\n")


#constractor overiding ko save karne k leye super()
class Father:
    def __init__(self):
        self.money=1000
        print("Father classs constructor")

    def show(self):
        return "Father class Instance method",self.money

class Son(Father):
    def __init__(self):
        super().__init__() #calling parents constructor
        self.bag=45

        
    def disp(self):
        return "Son class Instance Method",self.money,self.bag

print("After crerating  super () in Son ka object\n")
s=Son()
print(s.money)
print(s.show()) # father ka constructor initilazied nhi hua
print(s.disp())

print("After crerating Parent ka object\n")
f=Father()
print(f.money)
print(f.show()) # father ka constructor initilazied nhi hua
print(s.disp())