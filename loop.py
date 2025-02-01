import math
#Print all alphabets in upper case and in lower case.
def alfa():
  for i in range(65, 91):
    print(chr(i), end=" ")
  print()
  for i in range(97, 123):
    print(chr(i), end=" ")

#Print a multiplication table of a given number.
def table():
  a = int(input("Enter a number: "))
  for i in range(1,11):
    print(a, "x", i, "=", a*i)

#Count no. of alphabets and no. of digits in any given string.
def count():
  a = input("Enter a string: ")
  count = 0
  for i in a:
    count += 1
  print("The number of alphabets in the string is", count)
  
#Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.
def prime():
  a = int(input("Enter a number: "))
  prime=1
  if a == 1 or a == 0:
    print(a, "is neither prime nor composite")
  else:
    for i in range(2, a):
      if a % i == 0:
        prime = 0
    if prime == 1:
      print(a, "is prime")
    else:
      print(a, "is not prime")

def perfect():
  a = int(input("Enter a number: "))
  sum = 0
  for i in range(1,a):
    if a % i == 0:
      sum += i
  else:
    if sum == a:
      print(f"{a} is a perfect number")
    else:
      print(f"{a} is not a perfect number")

def armstrong():
  a = input("Enter a number: ")
  sum = 0
  for i in a:
    sum += int(i)**3
  if sum == int(a):
    print(a, "is an armstrong number")
  else:
    print(a, "is not an armstrong number")

def palindrome():
  a = input("Enter a number: ")
  if a == a[::-1]:
    print(a, "is a palindrome")
  else:
    print(a, "is not a palindrome")

def automorphic():
  a = int(input("Enter a number: "))
  square = a**2
  if str(square)[-len(str(a)):] == str(a):
    print(a, "is an automorphic number")
  else:
    print(a, "is not an automorphic number")
#Generate all Pythagorean Triplets with side length <= 30.
def pythagorean():
  for a in range(1,31):
    for b in range(1,31):
      for c in range(1,31):
        if a**2 + b**2 == c**2:
          print(a, b, c)

#Print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
def time():
  for i in range(0,25):
    if i == 0:
      print("00:00 Midnight")
    elif i >= 1 and i <= 11:
      if i >= 0 and i<= 9:
        print('0',end="")
        print(f"{i}:00 AM")
      else:
        print(f"{i}:00 AM")
    elif i >= 13 and i <= 23:
      print(f"{i}:00 PM")
    elif i == 12:
      print("12:00 Noon")

#Print factorial of a given number.
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

def factorial2():
  pass
#Print nCr and nPr.
def PnC():
  n = int(input("Enter n: "))
  r = int(input("Enter r: "))
  nPr = factorial(n) / factorial(n-r)
  nCr = factorial(n) / (factorial(r) * factorial(n-r))
  print(f"nPr = {nPr}")
  print(f"nCr = {nCr}")

#Print N natural nos. in reverse.
def reverse():
  n = int(input("Enter n: "))
  for i in range(n, 0, -1):
    print(i)

#Generate N numbers of Fibonacci series.
def fibo():
  n = int(input("Enter n: "))
  a = 0
  b = 1
  print(a, b, end=" ")
  for i in range(n-2):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

#Calculate sin(x); x is a radian value. The formula is as under: f(x) (hint: degrees can be converted into radians by 3.14159 / 180.)
def sin():
  x = (30 * math.pi) / 180
  flr = 0
  for n in range(0, 30):
      flr += ((x)**((2*n)+1) * ((-1)**n)) /    factorial(2*n+1)
