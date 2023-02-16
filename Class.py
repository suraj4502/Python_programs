
"""
Object-oriented programming (OOP) is a programming paradigm that revolves around the concept of objects,
which are instances of classes that encapsulate data and behavior.

In Python, everything is an object, and you can define your own classes to create custom objects.
"""

class Dog: 
    def __init__(self, name : str, age : int) :      # this takes name as a string and age as integer.  
        self.name = name
        self.age = age

    def bark(self)-> str:               # it means return strings
        print(f"{self.name} barks!")


# mydog = Dog("rocky",4)
# mydog.bark()


# Inheritence.
class Bulldog(Dog):
    def __init__(self, name: str, age: int):
        # We call the parent class's __init__ method using the super function to initialize the name and age instance variables
        super().__init__(name, age)            
        self.breed = 'Bulldog'

    def snore(self):
        print(f"{self.name} snores!")


my_Bulldog = Bulldog("izzy",4)
my_Bulldog.bark()
my_Bulldog.snore()