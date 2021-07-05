str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1]) #a
print(str[0:5]) # if you want to substring in python

print(str + str1) # concatenate

# check whether what we extracted is in the original str
print(str3 in str)

# split by dot
print(str.split('.')) # by default, split by white space " "

# strip
str4 = " great "
print(str4.strip())
print(str4.rstrip()) # only take care of right space