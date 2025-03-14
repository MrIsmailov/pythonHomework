import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Task 1: Basic Plotting
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y, label='f(x) = x^2 - 4x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of f(x) = x^2 - 4x + 4')
plt.legend()
plt.grid(True)
plt.show()

# Task 2: Sine and Cosine Plot
x = np.linspace(0, 2 * np.pi, 400)
sin_y = np.sin(x)
cos_y = np.cos(x)

plt.figure()
plt.plot(x, sin_y, label='sin(x)', linestyle='-', marker='o', color='b')
plt.plot(x, cos_y, label='cos(x)', linestyle='--', marker='x', color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x) and cos(x)')
plt.legend()
plt.grid(True)
plt.show()

# Task 3: Subplots
x = np.linspace(0, 10, 400)
x_log = np.linspace(0, 10, 400)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, x**3, 'tab:blue')
axs[0, 0].set_title('f(x) = x^3')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

axs[0, 1].plot(x, np.sin(x), 'tab:orange')
axs[0, 1].set_title('f(x) = sin(x)')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

axs[1, 0].plot(x, np.exp(x), 'tab:green')
axs[1, 0].set_title('f(x) = e^x')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

axs[1, 1].plot(x_log, np.log(x_log + 1), 'tab:red')
axs[1, 1].set_title('f(x) = log(x+1)')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

plt.tight_layout()
plt.show()

# Task 4: Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, c='blue', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot of 100 Random Points')
plt.grid(True)
plt.show()

# Task 5: Histogram
data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normally Distributed Data')
plt.grid(True)
plt.show()

# Task 6: 3D Plotting
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(x, y, z, cmap='viridis')
fig.colorbar(surf)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Surface Plot of f(x, y) = cos(x^2 + y^2)')
plt.show()

# Task 7: Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure()
plt.bar(products, sales, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data for Five Products')
plt.show()

# Task 8: Stacked Bar Chart
categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.array([
    [3, 2, 5, 7],
    [4, 3, 6, 8],
    [5, 4, 7, 9]
])

fig, ax = plt.subplots()
ax.bar(time_periods, data[0], label=categories[0])
ax.bar(time_periods, data[1], bottom=data[0], label=categories[1])
ax.bar(time_periods, data[2], bottom=data[0] + data[1], label=categories[2])

ax.set_xlabel('Time Periods')
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart')
ax.legend()
plt.show()