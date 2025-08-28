# OOP Assignment – Python

**Submitted by:** [Thobile Mkhize]  
**Course:** [Object-Oriented Programming]  
**Assignment:**   OOP – Assignment 1 & Polymorphism Challenge   

---

## Description
This repository contains my solution for the OOP assignment.  
The program demonstrates the following concepts:
- Creating classes with attributes and methods
- Using constructors (`__init__`)
- Inheritance (subclasses extending parent classes)
- Polymorphism (same method behaving differently across classes)

---

## Assignment 1: Design Your Own Class
- **Theme:** Superheroes  
- **Base Class:** `Superhero` (attributes: `name`, `power`, `city`)  
- **Subclass:** `FlyingSuperhero` (adds `flying_speed`)  
- **Methods:**  
  - `introduce()` introduces the superhero  
  - `fight_crime()` shows polymorphism (different behavior in subclass)  

---

## Activity 2: Polymorphism Challenge
- **Theme:** Vehicles  
- **Classes:** `Car`, `Plane`, `Boat`  
- Each class has the same method `move()` but with different outputs:
  - `Car.move()` → "Driving on the road."  
  - `Plane.move()` → "Flying in the sky."  
  - `Boat.move()` → "Sailing on the water."  

---

## How to Run
1. Open the file `oop_assignment.py` in Python 3 (IDLE or terminal).  
2. Run the program.  

---

## Expected Output
When running the program, the output should look similar to this:

--- Assignment 1 Output ---
I am Shadow from Metro City, and my power is Invisibility.
Shadow is fighting crime!
I am SkyWing from Cloud City, and my power is Flight.
SkyWing is fighting crime while flying at 300 km/h!
--- Activity 2 Output ---
Driving on the road.
Flying in the sky.
Sailing on the water.

