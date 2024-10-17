'''x=input("do you want to perform another calculation ? yes or no ")
while x=="yes"or"Yes":
    
    
def fun(x):
    if x >= 1:
        return x
    print( x + fun(x-1))
fun(5)'''
def sum(x,y):
    print (x+y)
def subs(x,y):
    print(x-y)
def mult(x,y):
    print(x*y)
def div(x,y):
    print(x/y)

list=["addition","substraction","multiplication","division","exit"]

while True:
    print(list)
    operation=input(" choose operation from the list ")
    if operation=="exit":
        break
    elif operation!="addition"or"substraction"or"multiplication"or"division":
        print("invalid")
    else:
        first_num=float(input(" please enter first number "))
        second_num=float(input(" please enter second number "))
        if operation == "addition":
            '''sum(first_num,second_num)'''
            result=first_num+second_num
            print("the result of the ",list[0]," of ",first_num," and ",second_num," is ", result)
        elif operation =="substraction":
            subs(first_num,second_num)
        elif operation == "multiplication":
            mult(first_num,second_num)
        elif operation=="division":
            div(first_num,second_num)
        else:
            print("invalid")
print("thank you")