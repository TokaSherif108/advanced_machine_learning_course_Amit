# factorial function 

def factorial(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num*factorial(num-1)
print(factorial(5))

# class e7na 7atena self 3shan fe __init__
# ana 5alas 3rft el num fo2 f constructor f msh m7tag a7to tany f function el main 


class fact_num:
    def __init__(self,num):
        self.num = num
        
    def factorial(self):
        if self.num == 0:
            return 0
        if self.num == 1:
            return 1
        return self.num * factorial(self.num-1)
f1=fact_num(5)
print(f1.factorial())