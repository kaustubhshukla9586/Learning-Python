# Multiple Inheritence - Inherit from more than one parent Class
#                       C(A,B)

class Animal: #Multilevel Inheritance - Animal is Grandfather
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} eats")

class Prey(Animal): #Prey and Predator are Parent classes which are taking all methods from the Animal Class
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey): #Rabbit Hawk and Fish are Child Classes taking all the methods from predator and prey which are taking all methods from Animal Grandparent class
    pass
class Hawk(Predator):
    pass
class Fish(Prey,Predator):
    pass

rabbit = Rabbit("rabbits")
hawk = Hawk("Tony")
fish = Fish("Jhon")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
fish.eat()
hawk.eat()
# hawk.flee() //This won't work as hawk doesn't inherit from the Parent class of flee