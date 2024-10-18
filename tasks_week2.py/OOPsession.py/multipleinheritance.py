'''
class A w Class B bywrs mn A  w class C 
class D bywrs mn B w C 
print do this hyro7 l meen ?
el bygy el awl hwa el byksb
'''
class A ():
    def do_this(self):
        print("I am in A")
class B(A):
    pass
class c():
    def do_this(self):
        print("I am in C")
class D (B,c):
    pass
x=D()
print(x.do_this())
