# List: List are order, mutable collections of items, they can contains items of different data types

lst = []
print(type(lst))

names = ['sushant', 'krish','jack', 1, 2,3, 4]
print(names)

mixed_list = ['some', 12, 12.35, True]
print(mixed_list)


## Accessing the list elements
fruits = ['apple', 'banana', 'orange', 'cherry', 'guava']
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])
print(fruits[-1])


print(fruits[1:]) # banana orange cherry guava
print(fruits[1:3]) # banana orange
print(fruits[-1:-3]) #[]

#modify the list elements
fruits[1] ='watermelon'
print(fruits) #['apple', 'watermelon', 'orange', 'cherry', 'guava']

fruits[2:]='someone'
print(fruits) # ['apple', 'watermelon', 's', 'o', 'm', 'e', 'o', 'n', 'e']

fruits = ['apple', 'banana', 'orange', 'cherry', 'guava']

# List methods
fruits.append('kiwi') ## add item to the end
print(fruits) # ['apple', 'banana', 'orange', 'cherry', 'guava', 'kiwi']

fruits.insert(2, 'watermelon')
print(fruits) # ['apple', 'banana', 'watermelon', 'orange', 'cherry', 'guava', 'kiwi']

fruits.remove('banana') # remove the first occurance of the item
print(fruits) #['apple', 'watermelon', 'orange', 'cherry', 'guava', 'kiwi']

poped_frutes = fruits.pop() #remove and return the last
print(poped_frutes) #kiwi
print(fruits) # ['apple', 'watermelon', 'orange', 'cherry', 'guava']

index_of_chery = fruits.index('cherry')
print(index_of_chery)

## sorting the items in list
fruits.sort() ## sort list in the accending order
fruits.reverse() #reverse the list

fruits.clear() ## remove all the items from the list


## Slicing the list
numbers = [1, 2, 3,4,5,6,7,8,9,10]
print(numbers[2:5]) # [3,4,5]
print(numbers[:5]) # [1,2,3,4,5]
print(numbers[2:]) # [3,4,5,6,7,8,9,10]
print(numbers[::2]) #[1, 3, 5, 7, 9]
print(numbers[::-1]) #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 


# iterating over List
for num in numbers:
    print(num)

for i, num in enumerate(numbers):
    print(f"index: {i}, number: {num}")


# List comprehension
lst=[]
for x in range(5):
    lst.append(x**2)

print(lst)
[x**2 for x in range(10)]
[print(x**2) for x in range(10)] #List comprehension
# Basic syntax: [expression for item in iterable]
#with conditional logic: [expression for item in iterable if condition]


#Basic list comphrension
square = [num**2 for num in range(10)]
print(square)

#List comprehension with condition
even_num =[]
for i in range(10):
    if i%2==0:
        even_num.append(i)
print(even_num)

even_num=[num for num in range(20) if num%2==0]
print(even_num)

#nested list comprehension
#syntex: [expression for item in iterabel for item2 in iterable2]
list1=[1,2,3,4]
list2=['a','b','c','d']

pair = [[i,j] for i in list1 for j in list2]
print(pair)

#List comprehension with function calls
words = ['hello', 'world', 'python', 'list', 'comprehension']
length = [len(word) for word in words]
print(length) # [5, 5, 6, 4, 13]