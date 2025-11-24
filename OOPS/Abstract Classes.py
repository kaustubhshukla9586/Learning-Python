### Abstract Class - Abstraction means showing only the essential features and hiding the complex internal details.
#They can contain abstract methods which are declared but don't have any implementation
#Abstract Classes benefits -
#                    1 - Prevents the instantiation of the class itself
#                    2 - Requires children to use inherited abstract methods
#                    3 - Sensitive or unnecessary details are not exposed


from abc import ABC, abstractmethod #Very Important

class Vehicle(ABC):
    @abstractmethod #we need to define this in child classes
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def meow(self): #This wont give a error if we don't actually use this in the child classes but abstract methods are important to be defined in methods
        pass

class Toyota(Vehicle):
    def go(self):
        print("Toyota is fast asl")
    def stop(self):
        print("Toyota stop")

class Mercedes(Vehicle):
    def go(self):
        print("Mercedes goes 320kmph")
    def stop(self):
        print("Mercedes stop")

mercedes = Mercedes()
toyota = Toyota()

toyota.stop()
mercedes.go()


