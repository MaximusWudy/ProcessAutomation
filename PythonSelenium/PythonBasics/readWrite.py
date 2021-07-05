file = open("test.txt") # assign to file object
print(file.read()) # read method: read ALL the contents of file
file.close() # close to avoid memory leak

file = open("test.txt")
print(file.read(2)) # read first 2 char/bytes of the file
file.close()

file = open("test.txt")
print(file.readline()) # whenever the method is called, the cursor will be moved to next line
print(file.readline())
file.close()

# read control
print("Start...")
file = open("test.txt")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

# Readlines() method: return a list of strs, each element a line
# ['a', 'b', 'c']
print("Start...")
file = open("test.txt")
for line in file.readlines():
    print(line)
file.close()

# using with()
'''
args:
r: read mode (default)
w: write mode
'''
with open('test.txt', 'r') as reader:
    content = reader.readlines() # return a list of string
    # our goal is to reverse the list
    reversed(content)

    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
