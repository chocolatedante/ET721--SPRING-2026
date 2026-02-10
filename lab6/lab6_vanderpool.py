"""
Dante Vanderpool 
Lab 6, classes, objects and methods
feb 10 2026
"""
#import matplotlib.pyplot as plt

print("\n --- Example 1: class ----")
# a class is like a blueprint of something
#using the class, we can create different instances of an object
#data attributes (properties) are values that represents an object
#methods are fucntions of an object

class Circle(object):
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    #method to add value to the radius
    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r

class Rectanlge(object):
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color
    
    #method to calcluate and retuen the area of the rectanlge
    def area(self):
        return self.h * self.w
    
    #method to calculate the perimeter of a rectangle
    def perimeter(self):
        return 2*self.w + 2*self.h
    #method to draw the rectangle
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectagle(0,0), self.w, self.h, fc=self.c)
        plt.axis("scaled")
        plt.show()     

#create an instance of an object
circle1 = Circle(5,"yellow")       
circle2 = Circle(2,"red")

rectangle1 = Rectanlge(2, 3, "green")
rectangle2 = Rectanlge(5, 4, "blue")

#accessing to data in an object
print(f"color of circle 2 = {circle2.c}")
print(f"The area of rectangle 1 = {rectangle1.w*rectangle1.h}")
print(f"The area of rectangle 2 = {rectangle2.w*rectangle2.h}")

#modify data of an object
circle2.c = "orange"
print(f"color of cirlce 2 after modification = {circle2.c}")

print(f"radius of circle 2 = {circle2.r}")
#call method add_radius in circle 2 and pass 6
circle2.add_radius(6)
print(f"radius of circle 2 after method add_radius = {circle2.r}")

#call methods in class Rectangle
print(f"The area of rectangle 1 = {rectangle1.area()}")
print(f"The area of perimeter 1 = {rectangle1.perimeter()}")

#draw rectangle
#rectangle2.drawRectangle()

print("\n EXERCISE ")

class BankAccount(object):
    def __init__(self, account_number, account_holder):
        self.an = account_number
        self.ah = account_holder
        self.b = 250.50

    def deposit(self, amount):
        self.b += amount

    def withdraw(self, amount):
        if self.b >= amount:
            self.b -= amount
        else:
            print("Withdrawal cannot be made. Insufficient funds.")

    def balance(self):
        print("Final balance $", self.b)


useraccount = BankAccount(123456789, "Dante Vanderpool")

useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)
useraccount.balance()
       



