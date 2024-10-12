function_name=lambda x,y,z:x+y*z
print(function_name(5,10,2))
print(type(function_name))
def function1(n):
    return lambda a:a*n
function2=function1(2)
print(function2(11))
def standarddev(x):
    return  lambda y:(x**2)+(y**2)-3
print(standarddev())
