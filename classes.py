from distutils.archive_util import make_archive
from pyexpat import model
from re import A


print("=" * 50 )
# 3 types of methods in classes are class methods, static methods and __init__ method

# quick test
'''
class People():
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)
        
person1 = People("Gregory")
person2 = People("Mike")
person1.print_name()


class Test:
    def __init__(self, a):
        self.a = a
        
    def display(self):
        print(self.a)
        
obj = Test("abdul")
obj.display()
'''
'''
class Pokemon():
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def stringPokemon(self):
        print(f"Pokemon name is {self.name} and type is {self.type}")

class GrassType(Pokemon):
    # overrides the stringPokemon() function on 'Pokemon' class

    def stringPokemon(self):
        print(f"Grass type pokemon name is {self.name}")

poke1 = GrassType('Bulbasaur', 'Grass')
# poke1.stringPokemon
poke1.stringPokemon()

poke2 = Pokemon('Charizard', 'Fire')
# poke2.stringPokemon
poke2.stringPokemon()


class test:
    def __init__(self,a="'Welcome to Zuri'"):
        self.a=a
    def display(self):
        print(self.a)
obj=test()
obj.display()

'''
# OOP
# abstraction- shwoing only the relevant part of the object and hiding the rest
# inheritance - inheriting the properties of another class into a class 
# encapsulation - keeping the object private so other objects do not have access to its properties
# polymorpheism - ability of the object to change forms or states

# class variables are shared by all instance of a class. 
# instance variable are created inside a method and are used in only that instance of the class
# to call a class variable, we call the class and then the variable. And for the instance variable we use [self]
 
class Vehicle:
    color = "red"
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        move_forward = "going at 30 km/hr "
        print(f"{move_forward}")
        return f"{move_forward}"
     
    def stop(self):
        stop = f"stopping after {self.start()}"
        print(stop)
        # return stop

    def horn(self):
        print(f"honk honk")
        # return f"honk honk"
evil_spirit = Vehicle(make="Toyota", model="Camry", year = 2019)

soul = Vehicle(make="Toyota", model="Camry", year = 2020)

# print(evil_spirit.color)
# print(soul.color)
# print(soul.model)
# soul.start() 
evil_spirit.stop() # when this runs it calls the start method again bcos it is involved in its code [hence we don't run the start method again else it wil run two times]
evil_spirit.horn()
print("=" * 60)
# there are 3 types of methods, namely: instance method, class method and static method. 
# class method can be accessed by classes and the syntax is 
    # @classmethod
    # def can_see(cls):
        # print("we can see")
        
# static method is just like a normal fxn. syntax is @staticmethod

# encapsulation with enny
# we use [single or double underscore to encapsulate or make our variable private.] we cannot modify the values of an encapsulated code unless it is done with the encapsulated code again. Private attribute cannot be called/changed out of a class.
# even when a class inherits from another class it cannot get hold of the private attribute of the parent class.


class Bicycle:
    def __init__(self):
        self.__min_price = 300
    
    def sell(self):
        print(f"I am about to sell my bicycle for {self.__min_price} dollars")
    
    def bid(self, price):
        if price > self.__min_price:
            self.__min_price = price
            print(f"{self.__min_price} dollars is accepted for the bicycle")
        else:
            print("Your bid is too low")
    
b = Bicycle()
b.__min_price= 100
b.sell()
b.bid(400)





# inheritance is a relationship and cmposition has a relationship


# still has to cover exception and composition from the video