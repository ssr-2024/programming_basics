import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure() # Create a figure
ax = fig.gca() # Get the current axes
ax.plot([1, 2, 3, 4], [1, 4, 9, 16]) # Plot some data on the axes
ax.set_xlabel('X') # Set the label for the x-axis
ax.set_ylabel('Y') # Set the label for the y-axis
ax.set_title('Simple plot') # Set the title of the plot

plt.show() # Display the plot

# Example 2
fig = plt.figure()
ax = fig.gca()
ax.plot([1, 2, 3, 4], [1, 4, 9, 16], label = 'random')
ax.plot([1, 2, 3, 4], [1, 2, 3, 4], label = 'random2')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Simple plot')
ax.set_xticks(np.arange(0, 5, 1)) # Set the ticks for the x-axis

ax.set_xlim(0, 5) # Set the limits for the x-axis
ax.set_ylim(0, 20) # Set the limits for the y-axis
ax.autoscale() # Automatically scale the axes

ax.legend(loc= 'lower center', ncol=2) # Display the legend with 2 columns at the lower center of the plot

plt.show()

# Example 3

fig = plt.figure()
ax = fig.gca()
ax.plot([1, 1, 1, 1], 'r-') # Plot a red line with a solid line style
ax.plot([2, 2, 2, 2], 'g--') # Plot a green line with a dashed line style
ax.plot([3, 3, 3, 3], 'b+-.') # Plot a blue line with a dash-dot line style
ax.plot([4, 4, 4, 4], 'yo--') # Plot a yellow line with a circle marker and dashed line style
 

ax.figure.set_size_inches(6.3, 3.54) # size must be set in inches; 1cm / 2.54 = 1 inch
ax.figure.set_dpi(1000) # dots per inch

ax.figure.savefig("plot_export.png") #portable network graphics
ax.figure.savefig("plot_export.svg") #scalable vector graphics



# Boxplots

# Creating dataset
np.random.seed(10)
data = np.random.normal(100, 20, 200)

fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.boxplot(data)

# show plot
plt.show()




