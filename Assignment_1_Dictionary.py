# Page-14 Point-1 Exercise
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Elements of Students : ", students)

# Page-14 Point-2 Exercise
print("Bobs Grade : ", students['Bob'])

# Page-14 Point-3 Exercise
students["David"] = 92
print("Elements of Students : ", students)
del students["Charlie"]
print("Elements of Students : ", students)

# Page-14 Point-4 Exercise
students["Bob"]=95
print("Bobs Grade : ", students['Bob'])

# Page-14 Point-5 Exercise
if 'Alice' in students:
    print("Alice available in Dictionary")
else:
    print("Alice not available in Dictionary")

# Page-14 Point-6 Exercise
print("Length of Dictionary : ", len(students))

