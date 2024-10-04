# # 1. Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# class Car:
#     brand="Maruti"
#     model="Brezza"
#     year=2024
#
# mycar=Car()
# print("Brand of Car:",mycar.brand)
# print("Model of Car:",mycar.model)
# print("Year of Car:",mycar.year)

# # 2. Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# class Student:
#     def display_info(self,name,roll_number,marks):
#         self.name=name
#         self.roll_number=roll_number
#         self.marks=marks
#         print("Name of Student:", self.name)
#         print("Roll number:", self.roll_number)
#         print("Marks of Student:", self.marks)
#
# S1=Student()
# S1.display_info("Shobhit",36,90)

# 3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?
# class Rectangle:
#     def area1(self,length,br):
#         self.length=length
#         self.br=br
#         return self.length*self.br
#     def perimeter(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#         return 2*(self.length + self.breadth)
#
# len=abs(float(input("Enter length of Rectangle:")))
# breadth=abs(float(input("Enter breadth of Rectangle:")))
# my_rec1=Rectangle()
# print("Area of Rectangle 1-->",my_rec1.area1(len,breadth))
# print("Perimeter of Rectangle 1-->",my_rec1.perimeter(len,breadth))
# len=abs(float(input("Enter length of Rectangle:")))
# breadth=abs(float(input("Enter breadth of Rectangle:")))
# my_rec2=Rectangle()
# print("Area of Rectangle 2-->",my_rec2.area1(len,breadth))
# print("Perimeter of Rectangle 2-->",my_rec2.perimeter(len,breadth))

# # 4. Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
# class Circle:
#     global pi
#     pi=3.14
#     def get_area1(self, radius):
#         self.radius=radius
#         return pi*(self.radius**2)
#     def get_circumference(self, radius):
#         self.radius=radius
#         return pi*self.radius*2
#
# radius=abs(float(input("Enter radius of Circle:")))
# my_cir1=Circle()
# print("Area of Circle 1-->",my_cir1.get_area1(radius))
# print("Circumference of Circle 1-->",my_cir1.get_circumference(radius))

# 5. Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance.
# class Account:
#     balance = 20000
#     Account_no= 234567
#     def debit(self,d_amount):
#         self.d_amount=d_amount
#         if self.balance-d_amount>0:
#             return self.balance-d_amount
#         else:
#             return "Insufficient balance"
#     def credit(self,c_amount):
#         self.c_amount=c_amount
#         self.balance+=c_amount
#         return self.balance
# cre_amt=abs(int(input("Enter Amount to Credit:")))
# deb_amt=abs(int(input("Enter Amount to Debit:")))
# my_acc=Account()
# print("Amount after Credit:",my_acc.credit(cre_amt))
# print("Amount after Debit:",my_acc.debit(deb_amt))

# # 6. Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count()
# # to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.
# class Employee:
#     employee_count=0
#     def increment_employee_count(self):
#         Employee.employee_count+=1
#     def __init__(self,name,designation,joining_yr):
#         self.name=name
#         self.designation=designation
#         self.joining_yr=joining_yr
#         self.increment_employee_count()
#     def show(self):
#         print("Employee Name:", self.name)
#         print("Employee Designation:", self.designation)
#         print("Employee Joining Year:",self.joining_yr)
#         print("Number of Employees:",Employee.employee_count)
# e1=Employee("Shobhit","RF",2017)
# e1.show()
# e2=Employee("Kapil","RF",2018)
# e2.show()
# e3=Employee("Rahul","RF",2019)
# e3.show()


# # 7. Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either
# # initialize all three attributes or just the title and author (in which case the price should be set to a default value).
# # Display the details of the book using an instance method.
#
# class Book:
#     def __init__(self,title,author,price=600):
#         self.author=author
#         self.title=title
#         self.price=price
#     def show(self):
#         print("Author of Book:",self.author)
#         print("Title of Book:",self.title)
#         print("Price of Book:",self.price)
# b1=Book("RF","XYZ")
# b1.show()
# b2=Book("RF","ABC",700)
# b2.show()

# # 8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in
# # Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# class TemperatureConverter:
#     def celsius_to_fahrenheit(self,celsius):
#         self.celsius=celsius
#         return (self.celsius*(9/5)+32)
# temp=TemperatureConverter()
# far=temp.celsius_to_fahrenheit(30)
# print("Temperature in Celsius:",temp.celsius)
# print("Temperature in Farenheit",far)


# 9. Create a class Time with attributes hours and minutes. Add a method add_time() that takes another Time object,
# adds its values to the current object, and returns a new Time object with the resulting sum.
# class TimeAdd:
#     def __init__(self,hour=0,min=0):
#         self.hour=hour
#         self.min=min
#         self.minconversion()
#     def minconversion(self):
#         ehour=self.min//60
#         self.hour+=ehour
#         self.min=self.min-ehour*60
#     def show(self):
#         print(self.hour,":",self.min)
#     def timeadd(self,newhour,newmin):
#         self.newhour=newhour
#         self.newmin=newmin
#         self.totalmin=self.min+self.newmin
#         ehour1=self.totalmin//60
#         self.totalhour=self.hour+self.newhour+ehour1
#         self.finalmin=self.totalmin-ehour1*60
#         return self.totalhour,self.finalmin
# t1=TimeAdd(10,75)
# t1.show()
# t2=TimeAdd(10,80)
# t2.show()
# h,m=t1.timeadd(10,30)
# print(h,":",m)
# 10.Create a class EmployeeSalary with class variables basic_salary and bonus_percentage. Write a class method
# set_bonus_percentage() to change the bonus percentage for all employees. Create an instance method
# calculate_total_salary() to calculate and return the total salary (basic + bonus) for a specific employee.
# class EmployeeSalary:
#     basic_salary=10000
#     bonus_per=10
#     def set_bonus_per(self,per):
#         self.bonus_per=per
#     def calculate_total_salary(self):
#         return self.basic_salary+(self.basic_salary*self.bonus_per/100)
# e1=EmployeeSalary()
# print("Employee 1 Salary:",e1.calculate_total_salary())
# e2=EmployeeSalary()
# e2.set_bonus_per(20)
# print("Employee 2 Salary:",e2.calculate_total_salary())