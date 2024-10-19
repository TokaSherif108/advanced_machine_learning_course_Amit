# check prime number 
'''Write a function that takes a number and return True if this number is prime 
and False if not.'''

def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
print(isprime(6))