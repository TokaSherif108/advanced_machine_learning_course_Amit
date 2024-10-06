
'''print("this is a comment")
'''
print("this isnt a comment")
#this is also a comment
#how to declare variables (remove # to see the errors)
x=5
#  1x=5
#  !x=5
#format function .format or f"   ,    
name="toka"
age="26"
course='AI'
print("my name is {},I am {},I'm engaged in {}".format(name,age,course))
print("my name is {0},I am {1}".format(name,age))
print("my name is {x}".format(x=name))
print(f"my name is {name},my age is {age}")
#try to solve 
'''Create a Python script to display personalized information. Utilize variables to store the user's name, 
age, and the name of the course they are learning. Dynamically generate a message that includes this 
information and print the result. Ensure clarity in your code implementation without relying on user 
input.'''

#python data types
#list
x=[1,2.5,"amit",True]
print(type(x))
#tuple
y=(1,2.5,"amit",True)
#set
z={1,2.5,"amit",True}
#dictionary
a={"key1":"value1","key2":"value2"}
# string
name="amit learning"
print(name[0])
print(name[-3])
#string slicing
print(name[0:6:1])
#string functions
name="toka sherif mohamed"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.replace("toka","nejod"))
print(name.count("amit"))
print(name.split())
words=["my","name","is","Toka"]
sentence=''.join(words)
print(sentence)
print(name.startswith('toka'))
print(name.endswith("nejod"))