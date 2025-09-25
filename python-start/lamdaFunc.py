#Lambda functions: small anonymous functions defined using the lanbda keyword. 
# can have any number of arguments but only one expression. 
# commonly used for short operations or as arguments to higher-order functions

#Syntex: lambda arguments: expression

addition = lambda a,b: a+b
print(type(addition))
print(addition(2,3))


def even(num):
    if num%2==0:
        return True
    return False

print(even(24))

lambda_even = lambda num:num%2==0
print(lambda_even(23))

addition_lam = lambda x,y,z:x+y+z

print(addition_lam(2,3,4))