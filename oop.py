#Object Oriented Programming
#class: a blueprint of an object
#object: an instance of a class. We create an object out of a class
# a class has: 1st member:variables/attributes, 2nd member:Behavior: the functions/methods

class Employee:
    def __init__(self, name, gender, position, age): #method that allows you to initialize your variables to have diff inputs
        self.name = name #self refers t a specific object
        self.gender = gender
        self.position = position
        self.age = age

    def drive(self):
        print("Employee is driving")


    def eat(self):
        print("Employee is eating")


#Creating an Object
employee1 = Employee("Mark", "Male", "Managing Director", 34)
print(employee1.name, employee1.gender, employee1.position) #when printing mention the object first then what you want displayed
employee1.drive() #we dont print functions, we call them
employee1.eat()
employee2 = Employee("Jane", "Female", "Administrator", 22)
print(employee2.name, employee2.gender, employee2.age)
employee2.drive()
employee2.eat()

employee3 = Employee("Joe", "Male", "HR", 23)
print(employee3.name, employee3.gender, employee3.age)
employee3.drive()
employee3.eat()



