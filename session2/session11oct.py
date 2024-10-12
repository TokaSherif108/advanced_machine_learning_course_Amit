'''list1=["amit","learning","python","machine learning","data science","deep learning"]
print(list1)
r=input("what do u want to remove? ")
list1.remove(r)
print(list1)'''
'''tuple=[{"a",1},{"b",2},{"c",3}]
d=dict(tuple)
print(d)'''
'''print(5/2)
print(5//2)
print(5%2)
'''
'''l1=[2,3,4]*3
print(l1)'''
'''l2=[2,3,4]*[2]
print(l2)
l3=[2,3,4]+[2,3,4]
print(l3)'''
'''l4=[2,5,6]*[2,3]
print(l4)'''
'''x=float(input("write your first number "))
y=float(input("write your second number "))
sign=input("write your operation ")
if sign =="+":
    print(x+y)
elif sign==("-"):
    print(x-y)
elif sign=="*":
    print(x*y)
elif sign=="/":
    print(x/y)
else:print("please check your numbers ")
x1=[1,2,3,4]
x2=[1,2,3,4]
print(type(x1)is type(x2))
print(hex(id(x1)))
print(hex(id(x2)))'''
degree=float(input("please write your mark "))
if degree >=90 :
    print("A")
elif degree>=80:
    print("B")
elif degree>=70:
    print("C")
elif degree>=60:
    print("D")
else:
    print("F")