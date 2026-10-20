students = ["Suraj", "Rohit", "Anjali", "Priya", "Amit"]

with open("students.txt", "w") as file:
    for student in students:
        file.writelines(f"{student}\n")

with open("students.txt", "r") as file:
    students = file.readlines()
    students = [student.strip() for student in students]
    print("Students in the file:")
    for student in students:
        print(student)


import csv 


with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Name"])
    writer.writeheader()
    for student in students:
        writer.writerow({"Name": student})

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("\nStudents in the CSV file:")
    for row in reader:
        print(row["Name"])


import json

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

with open("students.json", "r") as file:
    students = json.load(file)
    print("\nStudents in the JSON file:")
    for student in students:
        print(student)