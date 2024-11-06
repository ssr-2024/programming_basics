
import matplotlib.pyplot as plt
import numpy as np

# Generate random data
#np.random.seed(0)  # For reproducibility
x = np.random.rand(50) * 100  # 50 random x values between 0 and 100
y = np.random.rand(50) * 100  # 50 random y values between 0 and 100

# Create the scatter plot with smaller markers
plt.scatter(x, y, color='blue', marker='o', s=30, alpha=0.7)  # s=30 for smaller markers

# Set labels and title
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Scatter Plot with Random Data')

# Show grid
plt.grid(True)

# Show the plot
plt.show()



'''
import numpy as np
import matplotlib.pyplot as plt

# Create figure and axes
fig = plt.figure()
ax = fig.gca()

# Plot two lines with custom markers and styles
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], label='y=x^2', color='r', marker='o', linestyle='--',
        linewidth=2, markersize=12, markerfacecolor='b', markeredgewidth=2, markeredgecolor='g', alpha=0.5)
ax.plot([1, 2, 3, 4], [1, 2, 3, 4], label='y=x', color='b', marker='x', linestyle='-',
        linewidth=2, markersize=12, markerfacecolor='r', markeredgewidth=2, markeredgecolor='y', alpha=0.5)

# Set labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Simple plot')

# Add legend with specific settings
ax.legend(loc='upper left', ncol=2)

# Display grid
ax.grid()

# Adjust figure size and DPI, and save it to file before showing
fig.set_size_inches(10, 5)
fig.set_dpi(100)
fig.savefig('code/mathplotlib.pyplot.png')

# Display plot
plt.show()
'''