import matplotlib.pyplot as plt

days = ["Day1", "Day2", "Day3", "Day4", "Day5"]

growth = [10, 20, 23, 34, 38]

plt.plot(days, growth, marker='o', color='green')

plt.title("Days for plant")
plt.xlabel("Days")
plt.ylabel("Plant")

plt.grid(True)
plt.show()