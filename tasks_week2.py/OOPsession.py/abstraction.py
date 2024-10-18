'''chess game for example 
h3ml class l kol shkl 
msln l 7osan byt7rk kza 
abstract class el user hyd5lo tabya aw wazer 
w move 
abstract akny b7t shwyt rules aw instructions da ( polymerphism )
f ay 7d lazm yst5dm el gwa l abstract class
mynf3sh abny ay function f class el animal 
w kol function h7t ablha @abstractmethod 
'''
from abc import ABC , abstractmethod
class Animal(ABC):
    name="ay 7aga "
    @abstractmethod
    def move(self):
        pass
class Bird(Animal):
    #def move(self):
        pass
        print("move from bird")
class Cat(Animal):
    def move(self):
        print("move from cat")
b=Bird()  
b.move
a=Animal()
print(a.name)
'''a=Animal()
a.move      
mynf3sh anady move el f abstract'''