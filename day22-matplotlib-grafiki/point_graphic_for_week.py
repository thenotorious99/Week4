import matplotlib.pyplot as plt

day_of_week = ["Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday", "Sunday"]

steps = [1900, 5000, 2200, 7898, 10000, 8922, 15000]

plt.plot(day_of_week, steps, marker='o', color='blue')

plt.title("Steps for week")
plt.xlabel("Days of week")
plt.ylabel("Steps")

plt.show()