import random
from prettytable import PrettyTable
u="Toka"
p='123'
def ver_code(u,p):
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
                        break
                    else:
                        print("Incorrect Verification Code. Try again")       
                break
            else:
                print(" In correct password ")
        else:
            print(" In correct username ")        

