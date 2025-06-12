import matplotlib.pyplot as plt

# Students name
students = ["Georgi", "Ivo", "Kris", "Martin", "Tara"]

# Students grades
grades = [5.50, 4.23, 5.65, 3.00, 6.00]

# Create graphics
plt.plot(students, grades)

# Title on etiket
plt.title("Grades students")
plt.xlabel("Students")
plt.ylabel("Grades")

# Show on graphics
plt.show()