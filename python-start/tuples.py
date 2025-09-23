# tuple: tuples are ordered collection of items tht are immutable, they are similar to list but their immutability makes them different.

#creating tupple
empty_tuple = ()
print(empty_tuple) #()
print(type(empty_tuple)) ##<class 'list'>


lst=list()
print(lst) #[]
print(type(lst)) #<class 'list'>

tpl = tuple()
print(tpl) #()
print(type(tpl)) #<class 'list'>

numbers =tuple([1,2,3,4,5,6])
print(numbers) #(1, 2, 3, 4, 5, 6)

mix_tuple = (1, 'hello world', 3.12, False)
print(mix_tuple)


#Accessing tuple elements
print(numbers)
print(numbers[2])
print(numbers[-1])


print(numbers[0:4])
print(numbers[::-1])

#Tuples operations

concat = numbers+mix_tuple
print(concat) #(1, 2, 3, 4, 5, 6, 1, 'hello world', 3.12, False)

print(mix_tuple*3) #(1, 'hello world', 3.12, False, 1, 'hello world', 3.12, False, 1, 'hello world', 3.12, False)
print(numbers*3) #(1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6)

#Immutable Nature of Tuples
# Tuples are immutable, meaning their elements cannot be changed once assigned

# numbers[3] = 'hello' #Error

#Tuples methods
print(numbers.count(1)) # 1
print(numbers.index(5)) # 4

#packing and unpacking tuples
packed_tuple = 1,'h1llo',3,4
print(type(packed_tuple))
print(packed_tuple)

a,b,c,d = packed_tuple
print(a,b,c) #1 h1llo 3

#Unpacking with *
numbers=(1,2,3,4,5,6)
first,*mid,last=numbers
print(first, mid, last) #1 [2, 3, 4, 5] 6


#Nested Tuples
nested_tpl = ((1,2,3),('a','b','c'),(True, False))
#accessing the elements inside a tuple
print(nested_tpl[0]) # (1, 2, 3)
print(nested_tpl[1][2]) # c


#iterating over nested tuples
for sub_tpl in nested_tpl:
    for item in sub_tpl:
        print(item)

#1 2 3 a b c True False