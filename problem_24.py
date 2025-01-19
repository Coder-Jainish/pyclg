# This program adds numbers
def prob1():
    a = float(input("Enter one number to add:"))
    b = float(input("Enter another number to add:"))
    print(f"the sum of {a} and {b} is {a + b}")


# This program subtract numbers
def prob2():
    a = float(input("Enter one number:"))
    b = float(input("Enter another number:"))
    print(f"the subtraction of {a} and {b} is {a - b}")


# This program multiply numbers
def prob3():
    a = float(input("Enter one number:"))
    b = float(input("Enter another number:"))
    print(f"the multiplication of {a} and {b} is {a * b}")


# This program divide numbers
def prob4():
    a = float(input("Enter one number:"))
    b = float(input("Enter another number:"))
    print(f"the division of {a} and {b} is {a / b}")


# This is basic calculater
def prob5():
    a = float(input("Enter one number:"))
    b = float(input("Enter another number:"))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice:"))
    if choice == '1':
        print(f"the sum of {a} and {b} is {a + b}")
    elif choice == '2':
        print(f"the subtraction of {a} and {b} is {a - b}")
    elif choice == '3':
        print(f"the multiplication of {a} and {b} is {a * b}")
    elif choice == '4':
        print(f"the division of {a} and {b} is {a / b}")
    else:
        print("Invalid input")


# This program Convert hours into minutes
def prob6():
    hours = float(input("Enter hours: "))
    print(f"{hours} hours = {hours * 60} minutes")


# This program Convert minutes into hours
def prob7():
    minutes = float(input("Enter minutes: "))
    print(f"{minutes} minutes = {minutes / 60} hours")


# This program Convert dollars into Rs.
def prob8():
    dollars = float(input("Enter dollars: "))
    print(f"{dollars} dollars = {dollars * 48} Rs")


# This program Convert Rs. into dollars
def prob9():
    rupees = float(input("Enter Rupees: "))
    print(f"{rupees} Rs = {rupees / 48} dollars")


# This program Convert dollars into pounds
def prob10():
    dollars = float(input("Enter dollars: "))
    rupees = dollars * 48
    pounds = rupees / 70
    print(f"{dollars} dollars = {pounds} pounds")


# This program Convert gram into kg
def prob11():
    grams = float(input("Enter grams: "))
    print(f"{grams} grams = {grams / 1000} kg")


# This program Convert kg into gram
def prob12():
    kgs = float(input("Enter kilograms: "))
    print(f"{kgs} kg = {kgs * 1000} grams")


# This program Convert bytes into KB, MB, GB
def prob13():
    bytes_size = float(input("Enter bytes: "))
    kb = bytes_size / 1024
    mb = kb / 1024
    gb = mb / 1024
    print(f"{bytes_size} bytes = {kb} KB, {mb} MB, {gb} GB")


# This program Convert Celsius into Fahrenheit
def prob14():
    c = float(input("Enter temperature in Celsius: "))
    f = (9 / 5 * c) + 32
    print(f"{c}°C = {f}°F")


# This program Convert Fahrenheit into Celsius
def prob15():
    f = float(input("Enter temperature in Fahrenheit: "))
    c = 5 / 9 * (f - 32)
    print(f"{f}°F = {c}°C")


# This program Calculate interest
def prob16():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time in years: "))
    i = (p * r * t) / 100
    print(f"Interest = {i}")


# This program Calculate square area & perimeter
def prob17():
    len = float(input("Enter side length of the square: "))
    area = len**2
    p = 4 * len
    print(f"Area = {area}, Perimeter = {p}")


# This program Calculate rectangle area & perimeter
def prob18():
    len = float(input("Enter length of the rectangle: "))
    b = float(input("Enter breadth of the rectangle: "))
    area = len * b
    p = 2 * (len + b)
    print(f"Area = {area}, Perimeter = {p}")

# This program Calculate area of a circle
def prob19():
    r = float(input("Enter radius of the circle: "))
    area = 22 / 7 * r * r
    print(f"Area of the circle = {area}")


# This program Calculate area of a triangle
def prob20():
    h = float(input("Enter height of the triangle: "))
    b = float(input("Enter base length of the triangle: "))
    area = (h * b) / 2
    print(f"Area of the triangle = {area}")


# This program Calculate average of three numbers
def prob21():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    total = a + b + c
    print(f"Total = {total}")
    print(f"Average of {a}, {b} and {c} = {total / 3}")


# This program Swap numbers
def prob24():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Before swapping: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swapping: a = {a}, b = {b}")


# This program Calculate net salary
def prob23():
    a = float(input("Enter base salary: "))
    print(f"the net salary is {a + 0.1*a - 0.03*a}")


# This program Calculate net sales
def prob22():
    a = float(input("Enter base sale: "))
    print(f"the net sale is {a - 0.1*a}")