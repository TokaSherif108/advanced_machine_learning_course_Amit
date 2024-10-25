import random
from prettytable import PrettyTable
u = "Dimes"
p = "1111"
while True:
    x = input("Name: ")
    if x==u:
        y=input("password: ")
        if y==p:
            s=random.randrange(10000,1000000)
            print(f" verification code is : {s}")
            while True:
                l=int(input(" Enter your verification code : "))
                if l==s:
                    print(" Welcome ")
                    break
                else:
                    print("Incorrect Verification Code. Try again.")
                    break
        else:
            print( " In correct password ")
            break
    else:
        print(" In correct username ")           


