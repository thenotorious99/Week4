import matplotlib.pyplot as plt

classes = ["Class1", "Class2", "Class3", "Class4"]

students = [20, 25, 30, 35]

plt.bar(classes, students)

plt.title("Bar Graphics on students from classes")
plt.xlabel("Students")
plt.ylabel("Classes")

plt.show()