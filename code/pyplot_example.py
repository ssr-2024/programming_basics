#%%
import numpy as np
import matplotlib.pyplot as plt


#%%
fig = plt.figure()
ax = fig.gca()
ax.plot([1,2,3,4,5], [9,6,7,1,3])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Simple Plot')

#%%
plt.show()

#%%
fig = plt.figure() # erstelle figure
ax = fig.gca() # get current axes (gca)
ax.plot([1, 2, 3, 4, 5], [9, 6, 7, 1, 3], label='random')
ax.plot([1, 2, 3, 4, 5], [3, 1, 4, 6, 9], label='random2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Simple Plot')
ax.set_xticks(np.arange(0, 10, 0.2))
ax.set_xlim(-3, 15) # x axis from -3 to 15
ax.set_ylim(0, 5) # y axis from 0 to 5
ax.autoscale() # reset to autoscale
ax. legend (loc='lower center', ncol=2) # up to 2 labels on a row

#%%
fig = plt.figure() # erstelle figure
ax = fig.gca() # get current axes (gca)
ax.plot([1, 1, 1, 1, 1], 'r-') # - für durchgezogene Linie
ax.plot([2, 2, 2, 2, 2],'g--') # -- für gestrichelte linie
ax.plot([3, 3, 3, 3, 3], 'b+-') # + datenpunkte als +
ax.plot([4, 4, 4, 4, 4], 'yo--') # datenpunkte als o
ax.grid() # add background grid

# %%
# export plots as .png or .svg files
ax.figure.set_size_inches(6.3, 3.54) # size must be set in inches; 1cm / 2.54 = 1 inch
ax.figure.set_dpi (1000) # dots per inch; size * dpi = pixels
ax.figure.savefig("plot_export.png") # portable network graphic
ax.figure.savefig("plot_export.svg") # scalable vector graphics



# %%
# Create plots from pandas files
import pandas as pd
df = pd.read_csv('data/sample_data.csv')
# Create a plot
plt.figure(figsize=(8, 5))
plt.plot(df['x_values'], df['y_values'], marker='o', label='Random Data')

# Add title and labels
plt.title('Sample Plot from CSV Data')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.legend()

# Show the plot
plt.grid()
plt.show()

# %%
# create a scatterplot
x = np.random.rand(50) * 100
y = np.random.rand(50) * 100

fig = plt.figure() # erstelle figure
ax = fig.gca()
ax.scatter(x,y, color = 'red')

# Add title and labels
ax.title('Sample Scatter Plot')
ax.xlabel('X Values')
ax.ylabel('Y Values')
ax.legend()

ax.figure.set_size_inches(6.3, 3.54) # size must be set in inches; 1cm / 2.54 = 1 inch
ax.figure.set_dpi (1000)
ax.figure.savefig("Scatterplot_example.png")

# %%
