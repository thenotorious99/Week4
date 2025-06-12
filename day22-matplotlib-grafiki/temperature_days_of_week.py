import matplotlib.pyplot as plt

temperatures = [12, 34, 24, 28, 32, 40, 43]

days = ["Day1","Day2", "Day3", "Day4", "Day5",  "Day6", "Day7"]

plt.plot(days, temperatures)

plt.title("Days Temperatures")
plt.xlabel("Days")
plt.ylabel("Temperatures (C)")

plt.show()