#Dictionary: unordered collections of items, they are store data in key-value pairs. keys must be unique and immutable(e.g. strings, numbers, or tuples) while values can be of any type.


#creating dictionary
dicts = {}
print(dicts)
print(type(dicts))

empty_dict = dict()

student ={
    'name': 'sushant',
    'profession': 'SDE'
}
print(student) # {'name': 'sushant', 'profession': 'SDE'}

stu = {'name': 'sushant', 'profession': 'SDE'}

#accessing Dictionary elements
print(stu['profession'])
print(stu.get('name'))
print(stu.get('grade')) #None
print(stu.get('last_name', 'default value')) #default value


#Modifying dictionary elements
#Dictionary are mutable, so you can add, update or delete elements
print(stu)

stu['profession'] ='Full stack AI engineer'
print(stu) #{'name': 'sushant', 'profession': 'Full stack AI engineer'}

stu['exp'] ="more than 1 year"
print(stu) #{'name': 'sushant', 'profession': 'Full stack AI engineer', 'exp': 'more than 1 year'}

#deleting key and value pairs
del stu['exp']
print(stu) #{'name': 'sushant', 'profession': 'Full stack AI engineer'}

# Dictionary methods
keys = stu.keys() ## get all the keys
print(keys) #dict_keys(['name', 'profession']) 
val = stu.values() #get all the values
print(val) #dict_values(['sushant', 'Full stack AI engineer'])


items=stu.items() #get all key value pairs
print(items) #dict_items([('name', 'sushant'), ('profession', 'Full stack AI engineer')])


## Shallow copy
stu_copy = stu.copy()
print(stu, stu_copy)
stu['exp'] ='1year'
print(stu, stu_copy)


#iterating over dictionary
#iterating over keys
for key in stu.keys():
    print(key)

#iterating over values
for val in stu.values():
    print(val)

#Iterating over key values
for key, val in stu.items():
    print(f"key: {key}, valus: {val}")



#Nested Dictionary
students ={
    'student1':{'name':'sushant', 'age':24, 'pro':'SDE'},
    'student2': {'name':'Negi','age':23, 'pro':'AI eng' }
}
print(students) #{'student1': {'name': 'sushant', 'age': 24, 'pro': 'SDE'}, 'student2': {'name': 'Negi', 'age': 23, 'pro': 'AI eng'}}

#Accessing nested dictionaries elements
print(students['student1']['name'])
print(students['student2']['age'])


#iterating over nested dictionary
for st_id, st_info in students.items():
    print(f"{st_id}: {st_info}")
    for key, val in st_info.items():
        print(f"{key}: {val}")

# student1: {'name': 'sushant', 'age': 24, 'pro': 'SDE'}
# name: sushant
# age: 24
# pro: SDE
# student2: {'name': 'Negi', 'age': 23, 'pro': 'AI eng'}
# name: Negi
# age: 23
# pro: AI eng




#Dictionary comprehensions
Squares={x:x**2 for x in range(5)}
print(Squares)  #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16} 

#conditional dictionary comprehension
evens = {x:x**2 for x in range(10) if x%2==0}
print(evens)

# Practical Examples
# -> counting the frequencies
# -> merging 2 dictionary into 1 ##(**dict1, **dict2)