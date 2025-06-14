import json
import matplotlib.pyplot as plt

with open("store.json", "r") as f:
    data = json.load(f)

days = list(data.keys())
price = list(data.values())

plt.plot(days, price, color="green", marker='o', linestyle='-')
plt.title("Week Sales")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid(True)

plt.show()