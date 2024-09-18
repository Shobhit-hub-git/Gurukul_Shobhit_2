# Page-12 Point-1 Exercise
a = 1
b = 1.0
c = '1'
print("Integer Variable: ", a , " | Variable Type : ", type(a))
print("Float Variable: ", b , " | Variable Type : ", type(b))
print("String Variable: ", c , " | Variable Type : ", type(c))

# Page-12 Point-2 Exercise
a = 2
b = 2.0
c = '2'
print("Integer Variable: ", a , " | Variable Type : ", type(a))
print("Float Variable: ", b , " | Variable Type : ", type(b))
print("String Variable: ", c , " | Variable Type : ", type(c))
# Observation--> Variable Values changed as per new allocated values as variable stores only last allocated value.

# Page-12 Point-3 Exercise
a=b=c=10
print("Value of a :",a)
print("Value of b :",b)
print("Value of c :",c)

# Page-12 Point-4 Exercise
a = float(input("Enter 1st Value : "))
b = float(input("Enter 2nd Value : "))
print("Sum of provided Numbers : ", a + b )

# Page-12 Point-5 Exercise
list_fruits = ["Apple","Banana","Orange","Strawberry","Pear"]
print("List Contents:", list_fruits)
print("Type : ",type(list_fruits))

# Page-12 Point-6 Exercise
print("2nd Element of List:", list_fruits[1])
print("4th Element of List:", list_fruits[3])

# Page-12 Point-7 Exercise
numbers = [10,20,30,40,50]
print("Original List : ",numbers)
numbers[2] = 35
print("Modified List : ",numbers)