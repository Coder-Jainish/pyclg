#1. A list contains names of boys and girls as its elements. Boys’ names are stored as tuples. Write a program to find out number of boys and girls in the list. (Hint: use isinstance(ele,tuple))
def tuple_count():
  lists = [("Jainish","Sumit"),"Geeta","Rani"]
  count_boy = 0
  count_girl = 0
  for i in lists:
    if isinstance(i, tuple):
      count_boy += len(i)
    else:
      count_girl += 1
  print(f"There are {count_boy} boys and {count_girl} girls in the list")

#2. A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age
def tuple_list():
  lists = [(1,"Jainish",19),(2,"Sumit",18),(3, "Geeta",20)]
  roll_no = [i[0] for i in lists]
  name = [i[1] for i in lists]
  age = [i[2] for i in lists]
  print(f"Roll no. = {roll_no}")
  print(f"Name = {name}")
  print(f"Age = {age}")

#3. Suppose a date is represented as a tuple (d, m, y). Create two date tuples and find the number of days between the two dates.
def tuple_days():
  pass

#4. Create a list of tuples containing a food item and its price. Sort the tuples in descending order by price.
def tuple_sort():
  food = [("Pizza", 10), ("Burger", 8), ("Sandwich", 6), ("Fries", 4)]
  prize = (i[1] for i in food)
  print(sorted(prize, reverse=True))

#5. Remove empty tuple(s) from the list of tuples.
def tuple_delete():
  lists = [(1, 2, 3), (), (4, 5, 6), (), (7, 8, 9)]
  #None as the first argument to filter() means it uses the default truthiness of each item.

  #Empty containers like [], (), {}, "", and 0 are all treated as False.
  print(list(filter(None, lists)))

#6. Modify an element of a tuple.
def modify():
  tuples = (1, 2, 3, 4, 5)
  new_tuples = list(tuples)
  new_tuples[1] = 10
  tuples = tuple(new_tuples)
  print(tuples)

#7. Delete an element of a tuple
def delete():
  tuples = (1, 2, 3, 4, 5)
  new_tuples = list(tuples)
  new_tuples.remove(3)
  tuples = tuple(new_tuples)
  print(tuples)