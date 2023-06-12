import re
## string handling
# 1 string
name="My name is Pete"
##print(name)

#multiple strings

##print("The answer is ", 42, "always", sep=':', end='')
#if \n instaed of colon would put on seperate lines \t larger gap

#name= " Fred " " Bloggs " " Peter "
#print(name + "test")

name= " Sky Glass "
#convert to lower case
print(name.lower())

#convert to upper case
print(name.upper())

#replace a string
name1=name.replace("y", "e")
print(name1)



#find a string
print(name.find("s"))
#counts from and including 0

print(name.endswith("s"))

if name.endswith("y"):
    print("name end with y")

#length of string
print(len(name))

#slicing start to end
print(name[2:5])

#strip empty spaces
print(name.strip())

#String format
age = 20
message= "Hello, my age is " +str(age)
print(message)

newMessage= "Hello, my age is {}"
print(newMessage.format(age))

newMessage1= "Hello, my age is {} and I work for {}"
print(newMessage1.format(20,"Sky"))

#string split
line="root::0:0:superuser:/root:/bin/sh"
elems=line.split(":")
print(elems[0])
print(elems[1])
print(elems[2])

line1= "Hello World,This is sunny"
elems1=line1.split(",")
print(elems1[0])
print(elems1[1])

#Regex python docs re resource
message="Sky Glass"
newMessage=re.search("^Sky.*Glass$",message)
print(newMessage)
if newMessage:
    print("Text Found")
else:
    print("Text Not Found")

text="hello world 123"
if re.match(r"^hello",text):
    print("its hell in there")

if re.match(r"^[0-9 A-Z a-z]+$",text):
    print("string is all alpha")














