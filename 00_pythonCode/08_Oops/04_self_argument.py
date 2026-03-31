class Chaicup:
    size = 150 #ml
    
    #self refering to the all the property inside the class
    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup = Chaicup()
print(cup.describe())

print(Chaicup.describe) # <function Chaicup.describe at 0x000002747771E0C0>
# print(Chaicup.describe()) # TypeError: Chaicup.describe() missing 1 required positional argument: 'self'

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))