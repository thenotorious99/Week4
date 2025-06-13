import matplotlib.pyplot as plt

kids_age = [13, 14, 21, 18, 17]
tall_in_centimeters = [1.50, 1.61, 1.70, 1.83, 2.00]

plt.plot(kids_age, tall_in_centimeters, marker='o', color='yellow', linestyle='-')
plt.title("Kids' Height by Age")
plt.xlabel("Age")
plt.ylabel("Height (cm)")
plt.grid(True)

plt.show()