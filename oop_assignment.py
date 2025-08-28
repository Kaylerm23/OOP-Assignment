"""
OOP Assignment
Submitted by: [Your Name]
Description: This assignment demonstrates Object-Oriented Programming (OOP) concepts in Python:
1. Designing my own class with inheritance.
2. Demonstrating polymorphism with multiple classes.
"""

# -------------------------------
# Assignment 1: Design Your Own Class
# -------------------------------

# Base class: Superhero
class Superhero:
    """
    Represents a generic superhero.
    Attributes:
        name (str): Name of the superhero.
        power (str): Special power of the superhero.
        city (str): City where the superhero operates.
    Methods:
        introduce(): Prints a short introduction of the superhero.
        fight_crime(): Simulates the superhero fighting crime.
    """
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name} from {self.city}, and my power is {self.power}.")

    def fight_crime(self):
        print(f"{self.name} is fighting crime!")

# Subclass: FlyingSuperhero (demonstrates inheritance & polymorphism)
class FlyingSuperhero(Superhero):
    """
    Represents a superhero that can fly.
    Inherits from Superhero and adds flying_speed attribute.
    Overrides fight_crime() method to include flying.
    """
    def __init__(self, name, power, city, flying_speed):
        super().__init__(name, power, city)  # Initialize parent attributes
        self.flying_speed = flying_speed

    # Overriding method
    def fight_crime(self):
        print(f"{self.name} is fighting crime while flying at {self.flying_speed} km/h!")

# Creating objects
hero1 = Superhero("Shadow", "Invisibility", "Metro City")
hero2 = FlyingSuperhero("SkyWing", "Flight", "Cloud City", 300)

# Demonstrating functionality
print("\n--- Assignment 1 Output ---")
hero1.introduce()
hero1.fight_crime()

hero2.introduce()
hero2.fight_crime()

# -------------------------------
# Activity 2: Polymorphism Challenge
# -------------------------------

# Vehicle classes demonstrating polymorphism
class Car:
    """Represents a car."""
    def move(self):
        print("Driving on the road.")

class Plane:
    """Represents a plane."""
    def move(self):
        print("Flying in the sky.")

class Boat:
    """Represents a boat."""
    def move(self):
        print("Sailing on the water.")

# Demonstrate polymorphism
vehicles = [Car(), Plane(), Boat()]

print("\n--- Activity 2 Output ---")
for vehicle in vehicles:
    vehicle.move()
