import matplotlib.pyplot as plt


school_subject = ["Outside Game", "English", "Spanish", "German", "Python"]

grades1 = [3, 4, 5, 3, 6] # Student1
grades2 = [5, 3, 6, 5, 4] # Student2

plt.plot(school_subject, grades1, label="Student1" ,marker='o', color='blue')
plt.plot(school_subject, grades2, label="Student2", marker='o', color='red')

plt.title("Grades by 5 subjects")
plt.xlabel("Subjects")
plt.ylabel("Grades")
plt.legend()

plt.show()