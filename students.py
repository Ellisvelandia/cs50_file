# import csv

# # with open("students.csv") as file:
# #   for line in file:
# #    name, house = line.rstrip().split(",")
# #    print(f"{name} is in {house}")

# students = []

# with open("students.csv") as file:
#     # for line in file:
#     #     name, home = line.rstrip().split(",")
#     #     student = {"name": name, "home": home}
#     #     # student["name"] = name
#     #     # student["house"] = house
#     #     students.append(student)
#     reader = csv.DictReader(file)
#     for row  in reader:
#         students.append({"name": row["name"], "home": row["home"]})

# # def get_name(student):
# #     return student["house"]
    
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} from {student['home']}")        
# #     students.append(f"{name} is in {house}")

# # for student in sorted(students):
# #   print(student)

import csv

name = input("whats your name?")
home = input("where your name?")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({ "home": home,"name": name})