# #Write a Python function to find the maximum of three numbers
#
# def find_max(a,b,c):
#     if a>b & a>c:
#         return f"{a} is greater"
#     elif b>c:
#         return f"{b} is greater"
#     else:
#         return f"{c} is greater"
#
# a= int(input("Enter 1st Number:"))
# b= int(input("Enter 2nd Number:"))
# c= int(input("Enter 3rd Number:"))
# print(find_max(a,b,c))

# # 2 Write a Python function to multiply all the numbers in a list.
#
# def mul(list_num1):
#     result=1
#     length =len(list_num1)
#     for i in range(0,length):
#         result=result*list_num1[i]
#     return result
#
# list_num=[2,4,6,1,8,4]
# res=mul(list_num)
# print("Multiplication of Numbers in List:", res)

# 3 Write a Python program to reverse a string.
# def rev_str(name1):
#     return name1[::-1]
#
# name=input("Enter String to reverse: ")
# print("Reverse of string is:",rev_str(name))

# # 4 Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
#
# def factorial(num1):
#     result=1
#     num2=num1
#     for i in range(0,num1):
#         result=num2*result
#         num2=num2-1
#     return result
# num=abs(int(input("Enter no to get Factorial of:")))
# print("Factorial of :",num," is : ",factorial(num))

# # 5 Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def unique(num1):
#     num2=[]
#     length=len(num1)
#     j=0
#     for i in range(0,length):
#         if num1[i] in num2:
#             pass
#         else:
#             num2.insert(j, num1[i])
#             j += 1
#     return num2
#
# num=[1,2,3,3,3,3,4,5]
# num3=unique(num)
# print("Unique values in list",num3)

# # 6 Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# def prime(num1):
#     for i in range(2,num1):
#         if num%i==0:
#             return 0
#     return 1
# num=abs(int(input("Enter Number:")))
# value=prime(num)
# if value==1:
#     print("Entered number is Prime")
# else:
#     print("Entered number is not Prime")

# # 7 Write a Python program to print the even numbers from a given list.
# num=[1,2,3,4,5,6,7,8,9]
# even_num=list(filter(lambda x:x%2==0,num))
# print("Even Numbers in list:",even_num)

# # 8 Write a Python function that accepts a string and counts the number of upper and lower case letters.
# def func_lower_upper(string):
#     lower=0
#     upper=0
#     other=0
#     for i in string:
#         if i.islower():
#             lower+=1
#         elif i.isupper():
#             upper+=1
#         else:
#             other+=1
#     return lower,upper,other
# string=input("Enter a string to find Lower & Upper case letters:")
# lower,upper,other=func_lower_upper(string)
# print("Upper case letters in String:",upper)
# print("lower case letters in String:",lower)
# print("Extra letters in String:",other)

# # 9 Write a Python function to sum all the numbers in a list.
# def add(list_num1):
#     result=1
#     length =len(list_num1)
#     for i in range(0,length):
#         result=result+list_num1[i]
#     return result
#
# list_num=[2,4,6,1,-8,4]
# res=add(list_num)
# print("Addition of Numbers in List:", res)

# # 10 Write a Python function that checks whether a passed string is a palindrome or not.
# def rev_str(name1):
#     return name1[::-1]
#
# name=input("Enter String to check Palindrome: ")
# name1=rev_str(name)
# if name1==name:
#     print("String is Palindrome")
# else:
#     print("String is not Palindrome")