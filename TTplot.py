import matplotlib.pyplot as plt
import numpy as np

# Reading the data
x, y = np.loadtxt('ttdatt.txt', unpack=True)

# Setting up rcParams for latex font and font size
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 2

# Plotting the scatter plot and connecting lines
plt.scatter(x, y, color='black')
plt.plot(x, y, color='black')

# Interpolating y value at x=100
y_100 = np.interp(100, x, y)

# Drawing the vertical dashed line at T1 = 100 degrees Celsius
plt.axvline(x=100, color='black', linestyle='--')
# plt.plot([100, 100], [0, y_100], color='black', linestyle='--')


# Drawing the horizontal dashed line from the interpolated point to the y-axis
# plt.axhline(y=y_100, color='black', linestyle='--', xmax=(100 - plt.xlim()[0]) / (plt.xlim()[1] - plt.xlim()[0]))
plt.axhline(y=y_100, color='black', linestyle='--')

# Adding labels
plt.xlabel(r'$T_1$ ($^{\circ}$ C)')
plt.ylabel(r'$T_2$ ($^{\circ}$ C)')

# Adding tick label at y_100
plt.yticks(list(plt.yticks()[0]) + [y_100])

# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
