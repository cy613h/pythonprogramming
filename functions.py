# also called methods
# it is any name followed by a bracket


#1. Standard Library Functions/ Built-In Functions/ Predefined Function
# They already exist in python( have a name and know what they are doing
# min(): return the smallest number


x = min(45, 89, 90, 32, 67, 57)
print(x)

y = max(45, 89, 90, 32, 67, 57)
print(y)

#2. User-Defined Functions -  created and defined by users
# when creating a function always start with def
# you must always call them with their name

def school(): #def is a keyword
    print("eMobilis")
school() # You must always call them to do their job, always with their name

#parameter: passed inside the function bracket
#variable:
#arguments: the values you assign to parameters
def add(x, y):
    print(x + y)

add(10, 35)
add(5, 8)
add(4, 80)

