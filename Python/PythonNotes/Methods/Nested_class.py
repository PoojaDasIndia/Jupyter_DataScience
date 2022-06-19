
#a class within a class is calledd nested class

class Army:    #outer class

    #outer ka constructor
    def __init__(self):
       self.name="Pooja"
       self.gn=self.Gun()   #creating Inner class object
    
    #outer ka method
    def show (self):
        print("name :",self.name)


    class Gun:  #Inner class
        
        #inner ka constructor
        def __init__(self):
            self.name="AK47"
            self.capacity="75 Rounds"
            self.length= "34.3 IN"

        #inner ka method
        def display(self):
            print("Gun name :",self.name)
            print("Capacity :",self.capacity)
            print("Length :",self.length)

a=Army()
print(a.name)
a.show()

#print(gn.name) # cant do this go step by step inside
print("*******Before new valiable*********")
print(a.gn.name)
print(a.gn.capacity)
print(a.gn.length)

a.gn.display()

#that bit diffcult but we can give it vaiable namr

g=a.gn # varible name de diya

print("*******After new valiable*********")
print(g.name)
print(g.capacity)
print(g.length)
g.display()


