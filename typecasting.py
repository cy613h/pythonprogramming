# Typecasting
# Process of converting a value of one data type to another.(string, integer, float, boolean)
# explicit and implicit


# explicit typecasting: manually converting a value or variable into a different data type

name = "cy613h"
age = 18
gpa = 1.9
student = True


print(type(name))
print(type(age))
print(type(gpa))

#convert int to float
age = float(age)
print(type(age))

#convert float to int
gpa = int(gpa)
print(gpa)

#convert a value into a string
student = str(student)
print(student)

#convert a value into a boolean
age = bool(age)
print(age) #will always print true if value is anything but not 0


#implicit typecasting: when a value or variable is converted into a different data type automatically
x = 2
y = 2.0
x = x/y
print(x) #prints x as a float now

