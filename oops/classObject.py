# A class is a blue print for creating objects, Attributes, methods

class Car:
    pass

audi = Car() #Object of class car
bmw = Car()

print(dir(Car))
## Instance variable and methods
class Dog:
    ##constructor
    def __init__(self,name, age):
        self.name=name
        self.age = age
    

#create objects
dog1 = Dog('Buddy', 3)
print(dog1)
print(dog1.name)
print(dog1.age)

#Define a class with instance methods
class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Bark(self):
        print(f"{self.name} says woof!")


dog2 = Dogs("buddy", 5)
dog2.Bark()

## Object-Oriented programming(OOp) allow you to model real-world scenarios using calsses and objects. In this lesson, you learnied how to create classes and objects, define instance variables and methods, and use them to perform various operations. Understanding these concepts is fundamental to writing effective and maintainable Python code.