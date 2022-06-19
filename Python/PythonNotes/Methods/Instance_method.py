class car:

    #constructor or initization method
    #self contain refernceof current object

    def __init__(self,model):
        self.model= model # Instance Varible always wrriten inside __init__

    

    def show(self,colour): #Instance Method with parameter
        self.colour=colour  #Instance Varible
        print(f"Model :{self.model} and colour : {self.colour}") #accessing instance varible


Maruti=car("x20")
Maruti.show("Red")
tata=car("45z",)
tata.show("Blue")



