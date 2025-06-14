import json
import matplotlib.pyplot as plt


students = {
    "Brayan": 5.60,
    "Ivo": 4.40,
    "Gabriela": 6.00,
    "Gergana": 3.45,
    "Ivailo": 5.65

}

with open("students.json", "w") as f:
    json.dump(students, f)

with open("students.json", "r") as f:
    data = json.load(f)

stu = list(data.keys())
gra = list(data.values())

plt.bar(stu, gra, color='blue')
plt.title("Students Grades")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.ylim(0, 6.5)

plt.show()
