# Read a whole file

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


## Read a file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  ## .strip() removes the newline character

# Writing a file(overWriting)
with open('example.txt', 'w') as file:
    file.write('Hellow World!\n')
    file.write('This is a new Line')

#Writing a file without overwriting
with open('example.txt', 'a') as file:
    file.write('Append operation taking place!\n')

##wrting a list of lines to a file
lines = ['first line \n, Second line \n third line\n']

with open('example.txt', 'a') as file:
    file.writelines(lines)

## Binaryfiles
data =b'\x00\x01\x02\x03\x04'

with open('binaryfiles.bin', 'wb') as file:
    file.write(data)

## Reading a binary file
with open('binaryfiles.bin', 'rb') as file:
    content = file.read()
    print(content)

# w+ mode in python is used to open a file for both reading and writing. If the file does not exist, it will be created. if the file exists, its content is truncated(i.e overwritng file)
