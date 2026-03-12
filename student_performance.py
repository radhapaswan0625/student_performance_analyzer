students = []

n = int(input("How many students?"))

for i in range (n):
    name = input("Enter student names: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks":marks})

#print all students 
print("\nStudent List:")
for student in students:
    print(student["name"], "->", student["marks"])

#Calculat average
total = 0
for student in students:
    total += student["marks"]

average = total/n
print("\nAverage Marks:", average) 

#Find topper
topper = students[0]
for student in students:
    if student["marks"] > topper["marks"]:
        topper = student
print("\nTopper is:", topper["name"], "with marks", topper["marks"])        

#Find lowest marks gain 
lowest = students[0]
for student in students:
    if student["marks"] < lowest["marks"]:
        lowest = student
print("\nlowest marks gain student is:", lowest["name"], "with marks", lowest["marks"])

#calculate grades according to their obtained marks:
print("\nStudents Grades:")

for student in students:
    marks = student["marks"]

    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade ="Fail"
    print(student["name"], "->", marks, "->Grade", grade) 

#sort students by marks (highest to lowest)
students.sort(key=lambda x: x["marks"], reverse=True)

print("\nStudent Ranking:")

rank = 1
for student in students:
    print(rank, ".", student["name"], "->", student["marks"])
    rank += 1


            


