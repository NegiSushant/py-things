# everything in python is object

# defining or creating the class
class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))  # <class 'type'>

# creating the object of the class
ginger_tea = Chai()

print(type(ginger_tea)) # <class '__main__.Chai'>
print(type(ginger_tea) is Chai) # True

