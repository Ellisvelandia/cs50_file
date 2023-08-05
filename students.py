# with open("students.csv") as file:
#   for line in file:
#    name, house = line.rstrip().split(",")
#    print(f"{name} is in {house}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        # student["name"] = name
        # student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")        
#     students.append(f"{name} is in {house}")

# for student in sorted(students):
#   print(student)
