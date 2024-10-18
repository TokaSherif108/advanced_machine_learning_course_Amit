'''chess game for example 
h3ml class l kol shkl 
msln l 7osan byt7rk kza 
abstract class el user hyd5lo tabya aw wazer 
w move 
'''
from abc import ABC , abstractmethod
class Animal(ABC):
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
'''a=Animal()
a.move      '''