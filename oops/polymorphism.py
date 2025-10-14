# Polymorphism: that allows objects of different classes to be treated as objects of a common superclass.
# It provides a way to perform a single action in different form.
#Polymorphism is achieved through method overriding and interfaces


## Method Overriding: allows a child class to provide a specific implementation of a method that is already defined in its parent class

#Base class
class Animal:
    def speak(self):
        return 'Sound of the animal!'
    
#Drived class 1
class Dog(Animal):
    def speak(self):
        return "woof!"
    
#Drived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"
    

## Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat= Cat()

print(dog.speak())
print(cat.speak())
animal_speak(dog)


#Polymorphism with functions and methods

#base class
class Shape:
    def area(self):
        return "The area pf the figure"

#Drived class 1
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
#Drive class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius  = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
## FUnction that demonstrate polymorphism
def print_area(shape):
    print(f"the area is {shape.area()}")

rectangle = Rectangle(4, 5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)


## Polymorphism with Abstract Base Classes: used to define common methods for a group of related objects. They can enforce that derived classes implement particular methods, promoting consistancy across different implementations

from abc import ABC, abstractmethod

## Define an abstract class
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

#Derived class 1
class Cars(Vehicle):
    def start_engine(self):
        return "Car engine started!"
    

#Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engine started"
    
## Function that demonstates polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())

#Create objects of car and Motorcycle
car = Cars()
motorcycle = Motorcycle()

start_vehicle(car)
start_vehicle(motorcycle)