#1. Write a program to create three dictionaries and concatenate them to create fourth dictionary.
def prob1():
  dict1 = {"a":1, "b":2, "c":3}
  dict2 = {"d":4, "e":5, "f":6}
  dict3 = {"g":7, "h":8, "i":9}
  dict4 = {**dict1, **dict2, **dict3}
  print(dict4)
  # by update function 
  '''dict4.update(dict1)
  dict4.update(dict2)
  dict4.update(dict3)
  print(dict4)'''
#2. Write a program to check whether a dictionary is empty or not.
def prob2():
  dict1 = {"a":1, "b":2, "c":3}
  if not dict1:
    print("Dictionary is empty")
  else:
    print("Dictionary is not empty")

#3. Create a dictionary with dept no, employee roll no. and salary. Find out department wise min and maximum of salary.
def prob3():
  dict1 = {"dept1": {"emp1": 1000, "emp2": 2000, "emp3": 3000}, "dept2": {"emp4": 4000, "emp5": 5000, "emp6": 6000}
          }
  for i in dict1:
    print(f"Max salary in {i} department is {max(dict1[i].values())}")
    print(f"Min salary in {i} department is {min(dict1[i].values())}")

#4. Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occurring in the string.
def prob4():
  str1 = input("Enter the string: ")
  dict1 = {}
  for i in str1:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  print(dict1)

#5. Create two dictionaries – one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.
def prob5():
  dic1 = {'apple':99, 'banana':69, 'orange':89, 'mango':79, 'pineapple':99}
  dic2 = {'apple':2, 'banana':3, 'orange':4, 'mango':5, 'pineapple':6}
  total = 0
  for i in dic1:
    total += dic1[i] * dic2.get(i,0)
  print(total)