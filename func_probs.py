#Print largest and smallest values out of two.
def prob1():
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))
  if a > b:
    print(a, "is the largest number")
    print(b, "is the smallest number")
  else:
    print(b, "is the largest number")
    print(a, "is the smallest number")


#Print largest and smallest values out of three.
def prob2():
  a = int(input("Enter a number: "))
  b = int(input("Enter a number: "))
  c = int(input("Enter a number: "))
  if a > b:
    if a > c:
      print(a, "is the largest number")
      if b > c:
        print(c, "is the smallest number")
      else:
        print(b, "is the smallest number")
    else:
      print(c, "is the largest number")
      print(b, "is the smallest number")
  else:
    if b > c:
      print(b, "is the largest number")
      if a > c:
        print(c, "is the smallest number")
      else:
        print(a, "is the smallest number")
    else:
      print(c, "is the largest number")
      print(a, "is the smallest number")


# Check whether a given number is odd or even.
def prob3():
  a = int(input("Enter a number: "))
  if a % 2 == 0:
    print(a, "is an even number")
  else:
    print(a, "is an odd number")


#Check whether a given number is divisible by 10 or not.
def prob4():
  a = int(input("Enter a number: "))
  if a % 10 == 0:
    print(a, "is divisible by 10")
  else:
    print(a, "is not divisible by 10")


# Accept age of a person. If age is less than 18, print minor otherwise Major.
def prob5():
  a = int(input("Enter your age: "))
  if a < 18:
    print("You are a minor")
  else:
    print("You are a major")


# Accept a number from the user. And print number of digits in it.
def prob6():
  a = input("Enter a number: ")
  print(len(a))


# Accept a year value from the user. Check whether it is a leap year or not.
def prob7():
  a = int(input("Enter a year: "))
  if a % 4 == 0 or a % 400 == 0:
    print(a, "is a leap year")
  else:
    print(a, "is not a leap year")


# Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
def prob8():
  a = int(input("Enter the first angle: "))
  b = int(input("Enter the second angle: "))
  c = int(input("Enter the third angle: "))
  if a + b + c == 180:
    print("The triangle is valid")
  else:
    print("The triangle is not valid")

# Print absolute value of a given number.
def prob9():
  a = int(input("Enter a number: "))
  if a < 0:
    print(a * -1)
  else:
    print(a)

# Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter.
def prob10():
  a = int(input("Enter the length: "))
  b = int(input("Enter the breadth: "))
  if a * b > 2 * (a + b):
    print("The area of the rectangle is greater than its perimeter")
  else:
    print("The area of the rectangle is not greater than its perimeter")


# Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
def prob11():
  x1 = int(input("Enter the x-coordinate of the first point: "))
  y1 = int(input("Enter the y-coordinate of the first point: "))
  x2 = int(input("Enter the x-coordinate of the second point: "))
  y2 = int(input("Enter the y-coordinate of the second point: "))
  x3 = int(input("Enter the x-coordinate of the third point: "))
  y3 = int(input("Enter the y-coordinate of the third point: "))
  if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
    print("The three points fall on one straight line")
  else:
    print("The three points do not fall on one straight line")


# Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )
def prob12():
  x = int(input("Enter the x-coordinate of the center of the circle: "))
  y = int(input("Enter the y-coordinate of the center of the circle: "))
  r = int(input("Enter the radius of the circle: "))
  x1 = int(input("Enter the x-coordinate of the point: "))
  y1 = int(input("Enter the y-coordinate of the point: "))
  d = ((x1 - x)*2 + (y1 - y)2)*0.5
  if d < r:
    print("The point lies inside the circle")
  elif d == r:
    print("The point lies on the circle")
  else:
    print("The point lies outside the circle")

# Convert number 0 to 19 to its equivalent words. E.g. 0 → zero, 19→nineteen.
def prob13():
  a = int(input("Enter a number between 0 and 19: "))
  if a == 0:
    print("zero")
  elif a == 1:
    print("one")
  elif a == 2:
    print("two")
  elif a == 3:
    print("three")
  elif a == 4:
    print("four")
  elif a == 5:
    print("five")
  elif a == 6:
    print("six")
  elif a == 7:
    print("seven")
  elif a == 8:
    print("eight")
  elif a == 9:
    print("nine")
  elif a == 10:
    print("ten")
  elif a == 11:
    print("eleven")
  elif a == 12:
    print("twelve")
  elif a == 13:
    print("thirteen")
  elif a == 14:
    print("fourteen")
  elif a == 15:
    print("fifteen")
  elif a == 16:
    print("sixteen")
  elif a == 17:
    print("seventeen")
  elif a == 18:
    print("eighteen")
  elif a == 19:
    print("nineteen")
  else:
    print("Invalid input")


# Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail. If student secures <= 39 marks in any subject, consider him as fail. Also assigned a subject wise grade based on the following table:
'''
Marks Range Grade
Absent NA
0 – 39 F
40 – 44 P
45 – 49 C
50 – 54 B
55 – 59 B+
60 – 69 A
70 – 79 A+
80 – 100 O
'''

def prob14():
  a = int(input("Enter the marks of the first subject: "))
  b = int(input("Enter the marks of the second subject: "))
  c = int(input("Enter the marks of the third subject: "))
  total = a + b + c
  average = total / 3
  
  if a <= 39 or b <= 39 or c <= 39:
    print("\nYou have failed")

  else:
    print("\nYou have passed")
  
  print(total, "is your total marks")
  print(average, "is your average marks\n")
  
  # grading for subject a
  if a >= 80 and a <= 100:
    print("You have scored O grade in the first subject")
  elif a >= 70 and a <= 79:
    print("You have scored A+ grade in the first subject")
  elif a >= 60 and a <= 69:
    print("You have scored A grade in the first subject")
  elif a >= 55 and a <= 59:
    print("You have scored B+ grade in the first subject")
  elif a >= 50 and a <= 54:
    print("You have scored B grade in the first subject")
  elif a >= 45 and a <= 49:
    print("You have scored C grade in the first subject")
  elif a >= 40 and a <= 44:
    print("You have scored P grade in the first subject")
  else:
    print("You have scored F grade in the first subject")

  # grading for subject b
  if b >= 80 and b <= 100:
    print("You have scored O grade in the second subject")
  elif b >= 70 and b <= 79:
    print("You have scored A+ grade in the second subject")
  elif b >= 60 and b <= 69:
    print("You have scored A grade in the second subject")
  elif b >= 55 and b <= 59:
    print("You have scored B+ grade in the second subject")
  elif b >= 50 and b <= 54:
    print("You have scored B grade in the second subject")
  elif b >= 45 and b <= 49:
    print("You have scored C grade in the second subject")
  elif b >= 40 and b <= 44:
    print("You have scored P grade in the second subject")
  else:
    print("You have scored F grade in the second subject")

  # garding for subject c
  if c >= 80 and c <= 100:
    print("You have scored O grade in the third subject")
  elif c >= 70 and c <= 79:
    print("You have scored A+ grade in the third subject")
  elif c >= 60 and c <= 69:
    print("You have scored A grade in the third subject")
  elif c >= 55 and c <= 59:
    print("You have scored B+ grade in the third subject")
  elif c >= 50 and c <= 54:
    print("You have scored B grade in the third subject")
  elif c >= 45 and c <= 49:
    print("You have scored C grade in the third subject")
  elif c >= 40 and c <= 44:
    print("You have scored P grade in the third subject")
  else:
    print("You have scored F grade in the third subject")
