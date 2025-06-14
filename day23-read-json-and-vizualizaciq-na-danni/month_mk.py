import json
import matplotlib.pyplot as plt

with open("km.json", "r") as f:
    data = json.load(f)

month = list(data.keys())
km = list(data.values())

plt.plot(month, km, marker='o', color='gray', linestyle='-')
plt.title("Months Kilometers")
plt.xlabel("Month")
plt.ylabel("Kilometers")
plt.grid(True)

plt.show()