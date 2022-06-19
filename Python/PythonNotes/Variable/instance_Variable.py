"""Instance variables are the variables whose separate copy is created in every object.
If we modify the copy of Instance variable in an instance,
 it will not effect all the copies in the other instance.
"""
class car:

    #constructor or initization method
    #self contain refernceof current object

    def __init__(self):
        self.model="x20" # Instance Varible always wrriten inside __init__

    

    def show(self): #Instance Method
        print("Model :",self.model) #accessing instance varible

    def __str__(self):
        return "checkingggg: x20"   

Maruti=car()
print(Maruti)
Maruti.show()
tata=car()
tata.show()
print(tata.__str__())

tata.model='x45'
tata.show()
Maruti.show()
