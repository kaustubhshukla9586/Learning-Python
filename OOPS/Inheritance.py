#Allows a class to inherif attrtibutes and methods from another class
#Helps with code reusability and extensibility
#Class Child(Parent)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
        # if self.is_alive:
        #     print(f"{self.name} is Alive")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def Speak(self):
        print(f"{self.name} barks")
#    def __init__(self,is_alive): //This will erase all parental classes objects
#       self.is_alive=False
class Cat(Animal):
    def Speak(self):
        print(f"{self.name} Meows")
class Mouse(Animal):
    def Speak(self):
        print(f"{self.name} ")

dog = Dog("Richie")
cat = Cat("Persian")
mouse = Mouse("Little")

# dog.eat()
# cat.eat()
# mouse.eat()
# print(dog.is_alive)
dog.Speak()
cat.Speak()
mouse.Speak()

# print(dog.is_alive)
# print(cat.is_alive)
# print(mouse.is_alive)