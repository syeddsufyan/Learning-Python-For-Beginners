# Define the parent classes
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        pass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        pass

class Electronics:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def power_on(self):
        pass

class Shape:
    def __init__(self, color):
        self.color = color
    def draw(self):
        pass

# Define the child classes
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Woof"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    def drive(self):
        return "Driving on the road"

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def greet(self):
        return "Hello students"

class Phone(Electronics):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def power_on(self):
        return "Booting up"

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)
    def draw(self):
        return "Drawing a circle"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        return "Meow"

class Truck(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)
    def drive(self):
        return "Hauling cargo"

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def greet(self):
        return "Hello teacher"

class Laptop(Electronics):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def power_on(self):
        return "Booting up"

# Instantiate objects of the child classes and print their properties and methods
d = Dog("Buddy")
print(f"My dog's name is {d.name} and he says {d.speak()}.")

c = Car("Toyota", "Camry")
print(f"My car is a {c.make} {c.model} and it is {c.drive()}.")

t = Teacher("Mr. Smith", 40)
print(f"My teacher's name is {t.name} and he says {t.greet()}.")

p = Phone("Apple", "iPhone 12")
print(f"My phone is a {p.brand} {p.model} and it is {p.power_on()}.")

ci = Circle("blue")
print(f"I'm drawing a circle that is {ci.color} and it looks like {ci.draw()}.")

ca = Cat("Fluffy")
print(f"My cat's name is {ca.name} and she says {ca.speak()}.")

tr = Truck("Ford", "F-150")
print(f"My truck is a {tr.make} {tr.model} and it is {tr.drive()}.")

# s = Student("Jane Doe", 20)
# print(f"My student's name is {s.name} and she says
