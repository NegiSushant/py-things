# allows a class to inherit attributes and methods from another class. 


class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors= doors
        self.enginetype = enginetype

    def drive(self):
        print(f"The person will drive the {self.enginetype} car!")

    
car1 = Car(4, 5, 'Petrol')
car1.drive()

class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors, enginetype)
        self.is_selfdriving = is_selfdriving

    def selfDriving(self):
        print(f"Tesla support self driving {self.is_selfdriving}")

tesla1 = Tesla(4, 5, 'electric', True)
tesla1.selfDriving()
tesla1.drive()

## Multiple Inheritance: When a class inherits from more than one base class

#Base class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Subclass must implement this method")

#Base class 2
class Pet:
    def __init__(self, owner):
        self.owner = owner


#Drived class 
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):
        return f"{self.name} say woof!"
    
#Create an object
dog = Dog("Buddy", "Krish")
print(dog.speak())
print(f"Owner: {dog.owner}")