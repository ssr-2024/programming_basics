import numpy as np
import matplotlib.pyplot as plt

#%% Plotting functions
fig=plt.figure() # Create a figure object
ax=fig.gca() # Get current axes (gca)
ax.plot([ 1, 2, 3, 4, 5], [9, 6, 7, 1, 3])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Simple plot')
ax.set_xticks(np.arrange(0, 10, 0.2)) # Set x-ticks

ax.set_xlim(-3, 15)
ax.set_ylim(0, 5)
ax.autoscale()

ax.legend(loc='lower center', ncol=2) # Add legend

plt.show() # Show the plot

#%%
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.gca()
ax.plot([1,1,1,1,1,1], 'r:') # : heißt gepunktete Linie
ax.plot([2,2,2,2,2,2], 'g-.')  
ax.plot([3,3,3,3,3,3], 'b--')
ax.plot([4,4,4,4,4,4], 'k+-')
ax.grid() # Add grid in the background

plt.show() # Show the plot

# %%

# Aufgabe: Exportieren --> wo wird es hin exportiert? Ohne konkreten Pfad wird es in den Ordner gespeichert, in dem das Skript liegt. Hier also programming_basics
# Plotten mit Pandas
