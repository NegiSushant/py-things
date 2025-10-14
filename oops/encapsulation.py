#Encapsulation is the concept of wrapping data(variable) and methods(function) together as a single unit. It restrict direct access to some of the object's components, which is a means of preventing accidental interference and missuse of data

#Encapsulation with Getter and Setter Methods
#Public, protected, private variables or access modifiers

class Person:
    def __init__(self, name, age, gender, address):
        self.name = name # public variables
        self.age = age # public variables
        self.__gender = gender # private variables
        self._address = address #protected variable

person = Person("Someone", 34, 'male','Earth')
print(person.name)

##Encapsulation with Getter And Setter
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    ##getter method for name
    def get_name(self):
        return self.__name
    
    ## setter method for name
    def set_name(self, name):
        self.__name = name
    


