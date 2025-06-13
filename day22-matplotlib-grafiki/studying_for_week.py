import matplotlib.pyplot as plt

day_of_week = ["Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday", "Sunday"]

hours = [2, 3, 1, 3, 2.30, 3, 1.30]

plt.plot(day_of_week, hours, marker='o', color='green')
plt.title("My studying for whole week")
plt.xlabel("Days")
plt.ylabel("Hours")

plt.show()