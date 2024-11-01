import random

from prettytable import PrettyTable

u = "Dimes"
p = "1111"
def login_user(u,p):
    while True:
        x = input("Name: ")

        if x == u:
            y = input("Password: ")

            if y == p:
                s = random.randrange(10000, 1000000)
                print("Verification code is:", s)

                while True:
                    l = int(input("Enter Verification Code: "))

                    if l == s:
                        print("Welcome")
                        
                    else:
                        print("Incorrect Verification Code. Try again.")

                break
            else:
                print("Incorrect password")
        else:
            print("Incorrect username") 
login_user('Dimes','1111')