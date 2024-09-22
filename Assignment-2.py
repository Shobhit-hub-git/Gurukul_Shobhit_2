# #  Find largest of 3 nos
# a=float(input("Enter 1st Number : "))
# b=float(input("Enter 2nd Number : "))
# c=float(input("Enter 3rd Number : "))
# if a>b and a>c:
#     print("1st number is greater : ",a)
# elif b>c:
#     print("2nd number is greater : ", b)
# else:
#     print("3rd number is greater : ", c)

# # Question 1: Write a Python program that takes two numbers as input from the user and performs the following operations:
# #
# # Addition
# # Subtraction
# # Multiplication
# # Division
# # Modulus
# # Display the results for each operation.
# a=float(input("Enter 1st Number : "))
# b=float(input("Enter 2nd Number : "))
# print("Sum of Numbers :", a+b)
# print("Subtraction of Numbers :", a-b)
# print("Multiplication of Numbers :", a*b)
# print("Division of Numbers :", a/b)
# print("Modulus of Numbers :", a%b)


# # Question 2: Write a Python program that checks whether a given number is even or odd using the modulus operator.
# a=int(input("Enter Number : "))
# if a%2 ==0:
#     print("Entered number is Even")
# else:
#     print("Entered number is Odd")

# # Question 3: Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero.
# a=int(input("Enter Number : "))
# if a>0:
#     print("Number is Positive")
# elif a<0:
#     print("Number is Negative")
# else:
#     print("Number is Zero")

# # Question 4: Write a Python program that calculates the grade of a student based on the marks entered by the user. The grading scale is as follows:
# #
# # 90 and above: A
# # 80 - 89: B
# # 70 - 79: C
# # 60 - 69: D
# # Below 60: F
# marks=int(input("Enter Marks of Student : "))
# if marks>=90:
#     print("Student scores-->",marks,"marks \nGrade of Student--> A")
# elif marks>=80 and marks<90:
#     print("Student scores-->",marks,"marks \nGrade of Student--> B")
# elif marks>=70 and marks<80:
#     print("Student scores-->",marks,"marks \nGrade of Student--> C")
# elif marks>=60 and marks<70:
#     print("Student scores-->",marks,"marks \nGrade of Student--> D")
# else:
#     print("Student scores-->",marks,"marks \nGrade of Student--> F")

# # Question 5: Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
# new=open("sample.txt","a")
# new.write("Hello, this is a Sample file.")
# new.close()
# new1=open("sample.txt","r")
# print(new1.read())
# new1.close()

# # Question 6: Write a Python program that reads a text file called data.txt and counts the number of words in the file.
# new1=open("sample.txt","r")
# new2=new1.read()
# print("No of Words in file :", new2.find(" "))
# new1.close()

# # Question 7: Write a Python program to print the numbers from 1 to 10 using a for loop.
# print("Numbers printing from 1 to 10:\n")
# for i in range(1,11,1):
#     print(i)

# # Question 8: Write a Python program to display the multiplication table of a number entered by the user using a for loop.
# print("Program to print Table of a Entered Number\n")
# num=int(input("Enter the required Table Number:"))
# print("\n Table of Number:",num,"\n")
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)
