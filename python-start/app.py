print('hello world')
# in python datatype decide at run time by the python kernal

#Type inference
variable = 10
print(type(variable))
variable = 'someone'
print(type(variable))

## Name error
# a = b
#-----------------------Variables------------------

#In python, variables are created when you assign a value to them and they do not need explicit declaration to reserve memory space. the declaration happens automatically when you assign a value to a variable.

#Declaring and Assigning variables
age = 22
height =5.6
name='sushant singh negi'
is_student = True


#printing the variables
print('age ',age)
print('height: ', height)
print('name: ',name)


# Naming conventions
## Variable namse should be descriptive
# They must start with a letter or an '_' and contains letter, numbers and underscroes
## variables names case sensitive

first_name = 'Sushant'
last_name='Negi'


#Python is dynamically typed means type of a variable is determined at runtime


## Type Checking and conversion
type(first_name)

#Type conversion
age_str = str(age)

# Dynamic typing: python allows the type of a variable to change as the program executes


#input
age1 = input('What is the age: ')
print(age1, type(age1))

## Simple calculator
num1 = float(input('Enter first number: '))
num2 = float(input('Enter the second number: '))
sum = num1+num2
multi = num1 * num2
diff = num1 - num2

print("sum :", sum)
print("multiply: ", multi)
print("difference: ", diff)

#Datatypes: str, int, float, bool
# Comparision operator: ==, >=, <=, !=, 
# logical operators: AND -> and, NOT -> not, OR -> or

#----------------------Flow Control --------------------

# if, else and elif statement
age = 20
if age >= 18:
    print('You are allowed to vote in the election!')
else:
    print('You are minor!')


#------------------Loops------------------
for i in range(1, 11):
    print(2 * i)

for i in range(1, 20, 2):
    print(i) #1, 3, 5, 7, 9, 11, 13, 15, 17, 19

str = "some one"
for i in str:
    print(i) # s o m e   o n e

count = 0
while count <5:
    print(count)
    count=count+1

# Loop control statement: break, continue, pass