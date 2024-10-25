import random
from prettytable import PrettyTable
def ver_code():
    u="Toka"
    p=123
    while True:
        x=input(" Enter Name : ")
        if x==u:
            y=int(input("password: "))
            if y==p:
                s=random.randrange(10000,1000000)
                print(f" verification code is : {s}")
                while True:
                    l=int(input(" Enter your verification code : "))
                    if l==s:
                        print(" Welcome ")
                        continue
                    else:
                        print("Incorrect Verification Code. Try again.")
                        continue
            else:
                print(" In correct password ")
                continue
        else:
            print(" In correct username ")         
ver_code()
