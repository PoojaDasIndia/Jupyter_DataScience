class car:
    light="yess"

    @classmethod
    def is_light(cls):
        print("Light :",cls.light)



Maruti=car()
Tata=car()

print("Maruti",car.light) # calling class method
print("Tata",car.light)
print()

car.light="No"   #assign new value
print("Maruti",car.light) # calling class method
print("Tata",car.light)
       