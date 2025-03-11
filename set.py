import random
#1. Write a program that converts words present in a list into uppercase and stores them in a set.
def set1():
  list1 = ["hello", "world", "python"]
  for i in list1:
    print(i.upper())
  set1 = set(list1)
  print(set1)

#2. Write a program to create a set containing 10 random numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers that are greater than 35.
def set2():
  count = 0
  set2 = set()
  for i in range(10):
    set2.add(random.randint(15, 45))
  print(set2)
  for i in set2:
    if i > 35:
      set2.remove(i)
    elif i < 30:
      count += 1
  print(set2)

#3. Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.
def set3():
  set3 = set()
  set3.add("A")
  set3.add("B")
  set3.add("C")
  set3.add("D")
  set3.add("E")
  #modify
  list(set3)
  set3[1] = "F"
  set(set3)
  print(set3)
  #delete
  set3.remove("B")
  set3.remove("C")
  print(set3)
  
#4. A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.
def set4():
  set4 = {'Abhay', 'Abhishek','Aryan','Bob','Bhavya','Avinash'}
  a = set()
  b = set()
  for i in set4:
    if i[0] == "A":
      a.add(i)
    elif i[0] == "B":
      b.add(i)
  print(a)