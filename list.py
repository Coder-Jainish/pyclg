import random

#1. Create a list of 5 odd integers using random nos. Similarly create a list of 4 even integers using random nos. Replace the third element of odd integers with a list of 4 even integers. Flattern, sort and print the list. Provide appropriate message at each stage.
def odd_even():
  #expression for variable in iterable
  odd = [random.randint(0, 50) * 2 + 1 for _ in range(5)]
  print(f"Odd list: {odd}")

  even = [random.randint(0, 50) * 2 for _ in range(4)]
  print(f"Even list: {even}")

  odd.insert(2, even)
  print("List of odd numbers after insert list of even numbers: \n", odd)

  odd.pop(2)
  for i in range(2, len(odd) + 1):
    odd.insert(i, even[i - 2])

  print("List of odd numbers after insert list of even numbers: \n", odd)

  odd.sort()
  print("Sorted list of odd numbers: \n", odd)


#2. Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.
def occurrence():
  integer = [random.randint(0, 50) for _ in range(20)]
  print(f"List of 20 random integers: {integer}")

  user_integer = int(input("Enter a number: "))

  count = 0
  for i in integer:
    count += 1
    if i == user_integer:
      print(f"Position of {user_integer} in the list: {count}")


#3. Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
def remove_duplicate():
  integer = [random.randint(1, 30) for _ in range(50)]
  print(f"List of 50 random integers: {integer}")

  after_remove = []

  for i in integer:
    if i not in after_remove:
      after_remove.append(i)
  print(f"List of 50 random integers without duplicate values: {after_remove}")


#4. Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.
def positive_negative():
  integers = [random.randint(-50, 50) for _ in range(30)]
  print(f"List of 30 random integers: \n{integers}")

  positive = []
  negative = []


  for i in integers:
    if i > 0:
      positive.append(i)
    else:
      negative.append(i)

  print(f"List of positive integers:\n{positive}")
  print(f"List of negative integers:\n{negative}")

#5. A list contains 5 strings. Convert all these strings to uppercase.
def string_to_upper():
  string = ["hello", "world", "python", "programming", "language"]

  upper_string = []
  print(f"List of 5 strings: {string}")

  ''' 1 way
  for i in string:
    upper_string.append(i.upper())
  print(f"List of 5 strings in uppercase: {upper_string}")
  '''

  # 2nd way
  for i in range(len(string)):
    converse_string = []
    for j in string[i]:
      j = ord(j)
      if j>=97 and j<=122:
        j = j - 32
      j = chr(j)
      converse_string.append(j)
    upper_string.append("".join(converse_string))
  print(f"List of 5 strings in uppercase: {upper_string}")

#6. Convert list of temperatures in Fahrenheit degrees to equivalent Celsius degrees.
def fahrenheit_to_celsius():
  f_temp = [random.randint(0, 100) for _ in range(10)]
  print(f"List of 10 random temperatures in Fahrenheit:\n{f_temp}")

  c_temp = []

  for i in f_temp:
    ans = ((i - 32) * 5) / 9
    c_temp.append(round(ans))

  print(f"List of 10 random temperatures in Celsius:\n{c_temp}")

#7. Write a menu-driven program to implement the stack data structure.
def push(stack):
  item = input("Enter item to push: ")
  stack.append(item)
  print(f"Pushed {item} to stack")

def pop(stack):
  if stack:
      item = stack.pop()
      print(f"Popped {item} from stack")
  else:
      print("Stack is empty!")

def content1(stack):
  if stack:
      print("Stack contents (top to bottom):")
      for index, item in enumerate(reversed(stack), start=1):
          print(f"{index}: {item}")
  else:
      print("Stack is empty!")

def stack():
  stack = []
  while True:
      print("\nStack Operations:")
      print("1. Push")
      print("2. Pop")
      print("3. Display")
      print("4. Exit")

      choice = input("Enter your choice (1-4): ")

      if choice == '1':
          push(stack)
      elif choice == '2':
          pop(stack)
      elif choice == '3':
          content1(stack)
      elif choice == '4':
          print("Exiting stack operations.")
          break
      else:
          print("Invalid choice! Please enter a number between 1 and 4.")
stack()

#8. Write a menu-driven program to implement the Queue data structure.
def enqueue(queue):
    item = input("Enter item to enqueue: ")
    queue.append(item)
    print(f"Enqueued {item} to queue")

def dequeue(queue):
    if queue:
        item = queue.pop(0)  # Removes the first item (FIFO)
        print(f"Dequeued {item} from queue")
    else:
        print("Queue is empty!")

def content2(queue):
    if queue:
        print("Queue contents (front to rear):")
        for index, item in enumerate(queue, start=1):
            print(f"{index}: {item}")
    else:
        print("Queue is empty!")

def queue():
    queue = []
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            enqueue(queue)
        elif choice == '2':
            dequeue(queue)
        elif choice == '3':
            content2(queue)
        elif choice == '4':
            print("Exiting queue operations.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

#9. Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension).
def list_comprehension():
  list1 = [random.randint(0, 50) for _ in range(10)]
  print(f"List 1: {list1}")

  list2 = [random.randint(0, 50) for _ in range(10)]
  print(f"List 2: {list2}")

  list3 = [i for i in list1 if i not in list2]
  print(f"List 3: {list3}")
  
  list4 = []
  # 2nd way
  for i in list1:
    if i not in list2:
      list4.append(i)
  print(f"List 4: {list4}")
  # same as list3