"""
Q2. Write a Python program to create a class named Animal
    with an abstract method named sound. Implement subclasses 
    for different animals, such as Dog, Cat, and Cow, and override 
    the sound method for each subclass. """

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
    
class Cow(Animal):
    def sound(self):
        return "Moo!"

print(f"Dog's sound: {Dog().sound()}\nCat's sound: {Cat().sound()}\nCow's sound: {Cow().sound()}\n")
