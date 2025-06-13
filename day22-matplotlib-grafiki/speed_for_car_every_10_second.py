import matplotlib.pyplot as plt

time_in_second = [0.10, 0.20, 0.30, 0.40, 0.50]

speed_on_car = [10, 23, 31, 49, 55]

plt.plot(time_in_second, speed_on_car, marker='o', color="red", linestyle='-')
plt.title("Car Speed Every 10 Seconds")
plt.xlabel("Time (seconds)")
plt.ylabel("Speed (km/h)")
plt.grid(True)

plt.show()