# Page-13 Point-1 Exercise
ex_tuple = ('Red','Green','Blue')
print("Tuple Elements : ", ex_tuple)
print("Type : ", type(ex_tuple))

# # Page-13 Point-2 Exercise
colors = ('Red',"Green",'Blue','Yellow')
print("Original List : ",colors)
print("First Element of Tuple : ", colors[0])
print("Last Element of Tuple : ", colors[-1])


# # Page-13 Point-3 Exercise
# colors = ('Red',"Green",'Blue','Yellow')
# colors[1] = 'White'
#  Error will come tuple dont support item assignment

# Page-13 Point-4 Exercise
coordinates = (10,20,30)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
print("Original List : ",coordinates)
print("First Element of Tuple in x Variable: ", x)
print("Second Element of Tuple in y Variable: ", y)
print("Third Element of Tuple in z Variable: ", z)

# Page-13 Point-5 Exercise
colors = ('Red','Green','Blue')
if 'Blue' in colors:
    print("Blue present in list")
else:
    print("Blue not present in list")

# Page-13 Point-6 Exercise
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("Original List : ",days)
print("Length of Tuple : ", len(days))