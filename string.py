#Count how many vowels are there in a string. Accept the string from the user.
def vowels():
  user_string = input("Enter a string: ")
  vowels = "aeiouAEIOU"
  count = 0
  for i in user_string:
    if i in vowels:
      count += 1
  print(f"There are {count} vowels in the string")

#Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.
def lower_case():
  user_string = input("Enter a string: ")
  ans =''
  for i in user_string:
    if i>='A' and i<='Z':
      ans += chr(ord(i) + 32)
  print(ans)

def upper_case():
  user_string = input("Enter a string: ")
  ans =''
  for i in user_string:
    if i>='a' and i<='z':
      ans += chr(ord(i) - 32)
  print(ans)

def toggle():
  user_string = input("Enter a string: ")
  ans =''
  for i in user_string:
    if i>='A' and i<='Z':
      ans += chr(ord(i) + 32)
    elif i>='a' and i<='z':
      ans += chr(ord(i) - 32)
  print(ans)

#Accept two strings. Check whether one string is there in another string.
def str():
  str1 = input("Enter the first string: ")
  str2 = input("Enter the second string: ")
  if str1 in str2:
    print(f"{str1} is in {str2}")
  else:
    print(f"{str1} is not in {str2}")

#Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”.
def remove():
  str1 = input("Enter the first string: ")
  str2 = input("Enter the second string: ")
  a = str1.index(str2)
  print(str1[:a] + str1[a+len(str2):])
