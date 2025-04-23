#1.Write a program to create a csv file that we can directly open in MS-Excel.
import csv

data = [
    ["RollNo", "Name", "Maths", "Science", "English"],
    [1, "John", 85, 90, 88],
    [2, "Alice", 78, 82, 80],
    [3, "Bob", 92, 87, 85]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

2. Read the data stored in MS-Excel file and convert it into a dictionary. The record contains rollno, 
name of student, marks of three subjects. Also calculate total. Display the dictionary data on the 
monitor.

students = {}
with open("students.csv", "r") as file:
    reader = csv.reader(file) # read line wise and store in list
    header = next(reader) # go to header or 1st row
    for row in reader:
        rollno = row[0]
        name = row[1]
        marks = [int(row[2]), int(row[3]), int(row[4])]
        total = sum(marks)
        students[rollno] = {"Name": name, "Maths": marks[0], "Science": marks[1], "English": marks[2], "Total": total}

for rollno, details in students.items():
    print(rollno, details)

3. Accept contact details from the user and create a vcard that we can directly store in our mobile.

f = open("1.vcf", "w+")
name = input("Enter Name:")
mob = input("Enter Mobile No.:")
email = input("Enter Email id:")
f.write("BEGIN:VCARD\n")
f.write("VERSION:3.0\n")
f.write("FN:"+name+'\n')
f.write("TEL; TYPE-CELL:"+mob+'\n')
f.write("EMAIL:"+email+'\n')
f.write("END:VCARD\n")
f.close()
#darshit shah
#9825874525
#darshit.shah@spt.pdpu.ac.in

4. Create a specific subdirectory and copy one file from another subdirectory to this newly created 
subdirectory.

import os
import shutil

os.mkdir("new_folder")
shutil.copy("old_folder/sample.txt", "new_folder/sample.txt")

#This copies the file sample.txt from the folder old_folder into the newly created new_folder.
#The copied file in new_folder will also be named sample.txt.

5. Write a program to copy contents of one file to another. While doing so, replace all lowercase 
characters into uppercase characters.

with open("input.txt", "r") as file1:
    content = file1.read()

uppercase_content = content.upper()

with open("output.txt", "w") as file2:
    file2.write(uppercase_content)

6. Write a program that merges lines alternatively from two files and writes the results to new file. If 
one file has less number of lines than the other, the remaining lines from the larger file should be 
simply copied into the target file.

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_len = max(len(lines1), len(lines2))
    
    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

7. If an Employee object contains following details:
empcode, empname, Date of Joining, Salary
Write a program to serialize and deserialize this data.

import json;

class Employee: pass;

e = Employee();
e.empcode, e.empname, e.doj, e.salary = 101, "John", "2022-01-01", 50000;

json.dump(e.__dict__, open("emp.json", "w"));

d = json.load(open("emp.json"));

print(d)

8. Given a text file, write a program to create another text file deleting the words ‘a’, ‘the’, ‘an’ and 
replacing each one of them with a blank space.

with open("input.txt", "r") as infile:
    content = infile.read()

words = content.split()
filtered_words = [" " if word.lower() in ["a", "the", "an"] else word for word in words]
new_content = " ".join(filtered_words)

with open("output.txt", "w") as outfile:
    outfile.write(new_content)