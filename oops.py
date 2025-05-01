# Write a program to create a class that represents Complex numbers containing real and imaginary parts 
# and then use it to perform complex number addition, subtraction, multiplication and division.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def add(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def subtract(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def multiply(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    
    def divide(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(3, 2)
c2 = Complex(1, 7)

print("Addition:", c1.add(c2))
print("Subtraction:", c1.subtract(c2))
print("Multiplication:", c1.multiply(c2))
print("Division:", c1.divide(c2))

# 2. Write a program that implements a Matrix class and performs addition, multiplication and transpose 
# operations on 3x3 matrices.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def add(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)]
        print("Addition:", result)
    
    def multiply(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        print("Multiplication:", result)
    
    def transpose(self):
        result = [[self.matrix[j][i] for j in range(3)] for i in range(3)]
        print("Transpose:", result)

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m1.add(m2)
m1.multiply(m2)
m1.transpose()

# 3. Write a program to create a class that can calculate the surface area and volume of a solid. The class 
# should also have a provision to accept the data relevant to the solid.

class Solid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def surface_area(self):
        area = 2 * (self.length * self.width + self.width * self.height + self.height * self.length)
        print("Surface Area:", area)
    
    def volume(self):
        volume = self.length * self.width * self.height
        print("Volume:", volume)

cube = Solid(5, 5, 5)
cube.surface_area()
cube.volume()

# 4. Write a program to create a class that can calculate the perimeter/circumference and area of a regular 
# shape. The class should also have a provision to accept the data relevant to the shape.

class Shape:
    def __init__(self, side, shape_type):
        self.side = side
        self.shape_type = shape_type
    
    def perimeter(self):
        if self.shape_type == "square":
            print("Perimeter:", 4 * self.side)
        elif self.shape_type == "circle":
            print("Circumference:", 3.14 * 2 * self.side)
    
    def area(self):
        if self.shape_type == "square":
            print("Area:", self.side ** 2)
        elif self.shape_type == "circle":
            print("Area:", 3.14 * self.side ** 2)

square = Shape(4, "square")
circle = Shape(3, "circle")
square.perimeter()
square.area()
circle.perimeter()
circle.area()

# 5. Write a program that creates and uses a Time class to perform various time arithmetic operations.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def add(self, other):
        total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
        hours = total_minutes // 60
        minutes = total_minutes % 60
        print(f"Addition: {hours}:{minutes:02d}")
    
    def subtract(self, other):
        total_minutes = (self.hours * 60 + self.minutes) - (other.hours * 60 + other.minutes)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        print(f"Subtraction: {hours}:{minutes:02d}")

t1 = Time(5, 30)
t2 = Time(2, 45)
t1.add(t2)
t1.subtract(t2)

# 6. Write a program to create a class Date that has a list containing day, month and year attributes. Define 
# an overloaded == operator to compare two Date objects.

class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]
    
    def __eq__(self, other):
        print(self.date == other.date)

d1 = Date(15, 10, 2023)
d2 = Date(15, 10, 2023)
d3 = Date(20, 11, 2023)
d1.__eq__(d2)
d1.__eq__(d3)

# 7. Create a class Weather that has a list containing weather parameters. Define an overloaded in operator 
# that checks whether an item is present in the list.

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters
    
 dodecyl    def __contains__(self, item):
        print(item in self.parameters)

weather = Weather(["sunny", "rainy", "cloudy"])
weather.__contains__("sunny")
weather.__contains__("snowy")

# 8. Implement a String class containing the following functions:
# a. Overloaded += operator function to perform string concatenation
# b. Method toLower() to convert upper case letters to lower case.
# c. Method toUpper() to convert lower case letters to upper case.

class String:
    def __init__(self, text):
        self.text = text
    
    def __iadd__(self, other):
        self.text += other.text
        print(self.text)
    
    def toLower(self):
        print(self.text.lower())
    
    def toUpper(self):
        print(self.text.upper())

s1 = String("Hello")
s2 = String("World")
s1.__iadd__(s2)
s1.toLower()
s1.toUpper()