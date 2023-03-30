from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def start(self):
        pass

class Dog(Animal):
    def start(self):
        print("Starting The Dog Barks...")

class Cat(Animal):
    def start(self):
        print("Starting The Cat Meows...")

class Cihuahua(Animal):
    def start(self):
        print("Starting The Cihuahua yaps...")

class Siames(Animal):
    def start(self):
        print("Starting The Siames purrs...")
        
vehicles = [Dog(), Cat(), Cihuahua(), Siames()]

for vehicle in vehicles:
    vehicle.start()
