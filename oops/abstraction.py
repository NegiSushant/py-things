#Abstractinon: hiding the complex implementation details and showing only the necessary feaures of an object. This helps in reducing programming complexity and effort


from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):
    def drive(self):
        print("The vehicle is used for driving!")

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Car engine started!"
    
def operate_vehicle(vehicle):
    vehicle.start_engine()
    vehicle.drive()

car = Car()
operate_vehicle(car)