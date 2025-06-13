import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June"]

income = [15000, 6000, 24333, 30000, 21087, 13228]

plt.plot(months, income, marker='o', color='blue')

plt.title("6 months income for store")
plt.xlabel("Months")
plt.ylabel("Income")

plt.show()