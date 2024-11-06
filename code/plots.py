import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure() # create a figure object
ax = fig.gca() # get current axes
ax.plot([1, 2, 3, 4,5], [9, 6, 7, 1, 3], 'ro-' , label='random1' ) # plot some data on the axes
ax.plot([1, 2, 3, 4,5], [9, 7, 12, 8, 4], 'yo--' , label='random2') 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title("simple plot")

ax.set_xlim([0, 6]) # set x-axis limits
ax.set_ylim([0, 15]) # set y-axis limits

ax.legend(loc='lower center', ncol=2 )

ax.figure.set_size_inches(6.3, 3.54)  # Die Größe wird in Zoll festgelegt; 1 cm / 2.54 = 1 Zoll
ax.figure.set_dpi(100)               # Punkte pro Zoll; Größe * dpi = Pixel
ax.figure.savefig("plot_export.png") 


