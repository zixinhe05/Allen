import matplotlib.pyplot as plt
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn-v0_8-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, color='red', s=10)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)
ax.axis([0, 5230, 0, 1_100_0000000])

plt.show()