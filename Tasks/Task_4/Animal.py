from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        "Abstract method for making a sound"
        pass

    def describe(self):
        "General description of the class"
        print("This is an animal.")

class Dog(Animal):
    def make_sound(self):
        print("Haw haw haw")

class Cat(Animal):
    def make_sound(self):
        print("Meow meow meow")

class Cow(Animal):
    def make_sound(self):
        print("Moo moo moo")

if __name__ == '__main__':
    dog = Dog()
    cat = Cat()
    cow = Cow()

    dog.make_sound()
    cat.make_sound()
    cow.make_sound()

    dog.describe()
    cat.describe()
    cow.describe()
