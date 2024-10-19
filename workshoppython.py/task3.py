''' write two numbers & return a list of common dividors   '''
def dividors (num1,num2):
    mn=min(num1,num2)
    common_dividor=[]
    for i in range(1,mn+1):
        if num1 % i == 0 and num2 % i == 0:
            common_dividor.append(i)
    return common_dividor
print(dividors(20,10))       

# class

class dividor:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def cmn_div(self):
        mn=min(self.num1,self.num2)
        common_dividor=[]
        for i in range(1,mn+1):
            if self.num1%i==0 and self.num2%i==0:
                common_dividor.append(i)
        return common_dividor
d=dividor(20,10)
print(d.cmn_div())