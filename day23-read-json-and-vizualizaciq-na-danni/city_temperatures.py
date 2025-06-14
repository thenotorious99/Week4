import json
import matplotlib.pyplot as plt

with open("temperatures.json", "r") as f:
    data = json.load(f)

city = list(data.keys())
temp = list(data.values())

plt.plot(city, temp, color='blue', marker='o')
plt.title("City Temperatures")
plt.xlabel("City")
plt.ylabel("Temperatures")

plt.show()