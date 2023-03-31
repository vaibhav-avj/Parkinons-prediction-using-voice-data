import matplotlib.pyplot as plt
import numpy as np

# Define the number to visualize
num = 100

# Define the range of values
min_val = 0
max_val = 176

# Create a figure and axis object
fig, ax = plt.subplots()

# Create a scalar mappable object for the colormap
norm = plt.Normalize(min_val, max_val)
sm = plt.cm.ScalarMappable(cmap='cool', norm=norm)
sm.set_array([])

# Create a colorbar for the scalar mappable object
cbar = plt.colorbar(sm)

# Add a text label to the plot
ax.text(0.5, 0.5, str(num), fontsize=50, ha='center', va='center', color='white')

# Set the axis limits and hide the ticks
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])

# Set the background color using the colormap
ax.set_facecolor(sm.to_rgba(num))

# Show the plot
plt.show()
