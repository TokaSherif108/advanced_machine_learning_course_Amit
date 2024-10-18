class calculator:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def sum(self):
        return self.n1+self.n2
    def subs(self):
        return self.n1-self.n2
    def mult(self):
        return self.n1*self.n2
    def div(self):
        return self.n1/self.n2
    def power(self):
        return self.n1**self.n2
c1=calculator(5,2)
print(c1.power())