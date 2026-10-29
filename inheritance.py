# process of acquiring sth
#class is public if other classes can access its members
# class is private if other classes cannot access its members

class Animal: #parent-class/ superclass/ baseclass: gives what it has to other classes

    isMammal = True
    age = 3
    def movement(self):
        print("Animal is moving")

class Dog(Animal): # child class/ sub-class/ derived class: inherits from parent class

    def bark(self):
        print("Woof!! Woof!! Woof!!")

class Cat(Animal):
    def meow(self):
        print("Meow!! Meow!!")


dog1 = Dog()
dog1.movement()
print(dog1.isMammal, dog1.age)

cat1 = Cat()
cat1.meow()
print(cat1.isMammal, cat1.age)




