import matplotlib.pyplot as plt
import numpy as np
import random
import os
from datetime import datetime

# Generate folder name based on current date
folder_name = datetime.now().strftime('%Y-%m-%d')
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Generate random data
x = np.random.randn(1000)
y = np.random.randn(1000)

# Generate random colors
colors = np.random.rand(1000)

# Randomly choose the type of plot
plot_type = random.choice(['scatter', 'plot', 'hist'])

# Draw the plot based on the chosen type
if plot_type == 'scatter':
    plt.scatter(x, y, c=colors, alpha=0.5)
elif plot_type == 'plot':
    plt.plot(x, y, '-o', markersize=2, color=random.choice(['r', 'g', 'b', 'y', 'm', 'c']))
elif plot_type == 'hist':
    plt.hist(x, bins=50, color=random.choice(['r', 'g', 'b', 'y', 'm', 'c']), alpha=0.7)

# Save the plot to an image file inside the date-named folder
output_path = os.path.join(folder_name, 'art.png')
plt.savefig(output_path)
