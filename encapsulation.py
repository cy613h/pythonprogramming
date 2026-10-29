# key feature is OOP
# Bundling of attributes and methods inside a single class
# it prevents outer classes from accessing and changing methods/attributes of a class
#It helps achieve data hiding
#private attributes are denoted by an underscore as a prefix.

class Computer:
    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

comp1 = Computer()
comp1.sell()

comp1.__maxprice = 500
comp1.sell()

comp1.setMaxprice(500)
comp1.sell()