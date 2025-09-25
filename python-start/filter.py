#filter: function constructs an iterator from an elements of an iterable for which returns true. 
# used to filter out items from a list( or any other iterable) based on a condition

lst = [1,2,3,4,5,6,7,8,9,10,11,12]
def even(num):
    if num%2==0:
        return True
    
print(list(filter(even, lst)))

#filter with lambda function
greater_then_five = list(filter(lambda x:x>5, lst))
print(greater_then_five)

# filter with a lambda function and multiple conditions

even_and_greater_then_five = list(filter(lambda x:x>5 and x%2==0, lst))
print(even_and_greater_then_five)