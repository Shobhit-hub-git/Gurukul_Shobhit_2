# Assignment 1: Static Methods
# Create a class MathOperations that contains:
# A static method add_numbers that takes two arguments and returns their sum.
# A static method multiply_numbers that takes two arguments and returns their product.

# class MathOperations:
#     @staticmethod
#     def add_numbers(num1, num2):
#         return num1 + num2
#
#     @staticmethod
#     def multiply_numbers(num3, num4):
#         return num3 * num4
#
# num1=float(input("enter 1st number:"))
# num2=float(input("enter 2nd number:"))
# sum = MathOperations.add_numbers(num1,num2)
# print("sum of 2 numbers:",sum)
#
# num3=float(input("enter 1st number for multiplication:"))
# num4=float(input("enter 2nd number for multiplication:"))
# mul = MathOperations.multiply_numbers(num3,num4)
# print("multiplicaton of 2 numbers:",mul)

# Assignment 2: Class Methods
# Create a class Person that keeps track of the number of people created. The class should have:
# A class variable count to count instances of the class.
# A class method get_count that returns the current count.
#
# class Person:
#     count = 0
#     def __init__(self):
#         Person.count = Person.count + 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     def display_info(self, name, roll_number, marks):
#         self.name=name
#         self.roll_number=roll_number
#         self.marks=marks
#         print("Name of Student:", self.name)
#         print("Roll number:", self.roll_number)
#         print("Marks of Student:", self.marks)
#
# student1 = Person()
# student1.display_info("Shobhit",36,90)
# student2 = Person()
# student2.display_info("Shobhit2",37,92)
# print("Number of Students registered till now:",Person.get_count())
#
# Assignment 3: Using Both Static and Class Methods
# Create a class TemperatureConverter with the following:
# A static method celsius_to_fahrenheit that converts Celsius to Fahrenheit.
# A class method info that returns a message about temperature conversions.
#
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
#     @classmethod
#     def info(cls):
#         return "Temperature converted from Celsius and Fahrenheit."
#
# print("Temperature from Celsius to Fahrenheit:",TemperatureConverter.celsius_to_fahrenheit(25))
# print(TemperatureConverter.info())

# Assignment 4: Single Inheritance
# Create two classes:
# Animal with a method sound that prints "Animal sound".
# Dog that inherits from Animal and overrides the sound method to print "Bark".
#
# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound1(self):
#         print("Bark")
#
# animal = Animal()
# animal.sound()
# dog = Dog()
# dog.sound1()

# Assignment 5: Multiple Inheritance
# Create two classes:
# Bird with a method fly that prints "Flying".
# Fish with a method swim that prints "Swimming".
# A class Duck that inherits from both Bird and Fish.
#
# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     def __init__(self):
#         print("Master Class inheriting 2 classes")
#
# duck = Duck()
# duck.fly()
# duck.swim()

        # "Assignment 6: Abstract Class
        # Use the abc module to create an abstract class Shape that contains:
        # An abstract method area().
        # Two concrete classes Circle and Rectangle that inherit from Shape and implement the area method."

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         print("area")
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
#
# num1=float(input("Input Circle Radius:"))
# num2=float(input("Input Rectangle width:"))
# num3=float(input("Input Rectangle height:"))
# carea = Circle(num1)
# rectarea = Rectangle(num2, num3)
# print("Area of the circle: ",carea.area())
# print("Area of the rectangle: ",rectarea.area())

# Assignment 7: Encapsulation
# Create a class BankAccount that uses encapsulation:
# Private attributes _balance.
# Public methods deposit() and withdraw() that modify _balance safely.
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance = self._balance + amount
#             print("Amount Deposited: ",amount)
#         else:
#             print("Enter Positive amount")
#     def withdraw(self, amount):
#         # if 0 < amount <= self._balance:
#         if amount>0 and amount<self._balance:
#             self._balance = self._balance - amount
#             print("Withdrawal Amount: ", amount)
#         else:
#             print("Insufficient balance in account.")
#     def get_balance(self):
#         return self._balance
# amount1=float(input("Enter initial Account Balance:"))
# depamount=float(input("Enter Deposit Amount:"))
# widamount=float(input("Enter Withdrawal Amount:"))
# account = BankAccount(amount1)
# account.deposit(depamount)
# account.withdraw(widamount)
# print("Current balance:",account.get_balance())

# Assignment 8: Polymorphism with Method Overriding
# Create two classes Cat and Dog with a method speak().
# The Dog class should implement speak() to print "Woof".
# The Cat class should implement speak() to print "Meow".
#
# class Dog:
#     def speak(self):
#         print("Woof")
#
# class Cat:
#     def speak(self):
#         print("Meow")
# dog = Dog()
# cat = Cat()
# dog.speak()
# cat.speak()

# Assignment 9: Polymorphism with Method Overloading
# Create a class Calculator with a method add() that:
# Can accept 2 or 3 arguments and returns their sum.
# Hint: Use default parameters to handle method overloading in Python.
# class Calculator:
#     def add(self, a, b, c=0):
#         return a + b + c
#
# num1=float(input("Enter 1st no:"))
# num2=float(input("Enter 2nd no:"))
# num3=float(input("Enter 3rd no:"))
# cal = Calculator()
# print("Addition of 2 numbers:",cal.add(num1, num2))
# print("Addition of 3 Numbers:",cal.add(num1,num2,num3))

# Assignment 10: Multilevel Inheritance
# Create three classes:
# LivingBeing with a method breathe() that prints "Breathing".
# Mammal that inherits from LivingBeing and adds a method walk() that prints "Walking".
# Human that inherits from Mammal and adds a method think() that prints "Thinking".
#
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
# hum = Human()
# hum.breathe()
# hum.walk()
# hum.think()