# Arithmetic
# ctrl+d duplicated the line
x = 90
y = 5

print(x + y) #addition
print(x * y) #multiplication
print(x / y) #division
print(x - y) #subtraction
print(x % y) #modulus: gives a remainder

#comparison operators compare values and return a boolean
num1 = 45
num2 = 20

print(num1 < num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 >= num2)
print(num1 == num2) #equal to
print(num1 != num2) #not equal to


#assignment operators - used to store values in variables, they always happen first before any other operator
number = 80
print(number)

number += 2 #addition assignment
print(number)

number *= 2 #multiplication assignment
print(number)

number -= 2 #subtraction assignment
print(number)

number /= 2 #division assignment
print(number)

#logical operators - and, or, not:  they are used where we have more than 1 condition to determine the answer
print(100 == 50 and 60<80) #returns true if all conditions are true
print(100 == 50 or 60<80) #returns a true if any condition is a true
print(not (100 == 50 and 60<80) ) #gives opposite of the result



