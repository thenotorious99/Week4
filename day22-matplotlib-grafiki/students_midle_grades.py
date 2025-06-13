import matplotlib.pyplot as plt

school_subject = ["Outside Game", "English", "Spanish", "German"]

grades = [6, 5, 5, 4]


plt.plot(school_subject, grades, marker='o', color='blue', linestyle='-')

plt.title("School Grades")
plt.xlabel("School Subject")
plt.ylabel("Grades")
plt.grid(True)

plt.show()