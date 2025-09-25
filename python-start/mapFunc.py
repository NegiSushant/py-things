#map(): applies a function to all items in a input list(or any other iterable) and returns a map object(an iterator). 
# transforming data in a list comprehensively

#map(function_name, iterable)

num=[1,2,3,4,5,6]

def square(x):
    return x**2
print(list(map(square, num)))


#lambda function with map
print(list(map(lambda x: x**2, num)))

##map multiple iterables
num1=[1,2,3,4]
num2=[5,6,7,8]

added_numbers=list(map(lambda x,y:x+y, num1, num2))
print(added_numbers)