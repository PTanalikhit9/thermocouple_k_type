import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Reading the data
t, T = np.loadtxt('temptdatt.txt', unpack=True)

# Setting up rcParams for latex font and font size adjustments
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 2

# Plotting the scatter plot and connecting lines
plt.scatter(t, T, color='black')
plt.plot(t, T, color='black')

# Assuming last n data points represent the saturated part for linear fitting
n = 10
model = LinearRegression().fit(t[-n:].reshape(-1, 1), T[-n:])
predicted = model.predict(t.reshape(-1, 1))

# Initial value outside the range of the data
saturation_start = 1.0

# Finding the saturation start point
threshold = 0.01 # Adjust based on your data
for i in range(len(t) - n, 0, -1):
    if abs(T[i] - predicted[i]) > threshold:
        saturation_start = t[i + 1]
        break

# Plotting and annotation, based on the value of saturation_start
if saturation_start != 1.0:
    plt.axvline(x=saturation_start, color='red', linestyle='--')
    plt.annotate(f'Saturation starts at {saturation_start:.2f} s', 
                 xy=(saturation_start, plt.ylim()[0]),
                 xycoords='data',
                 xytext=(0.5, 0.2),
                 textcoords='axes fraction',
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
else:
    print("Could not determine the saturation start. Please adjust the threshold or consider another approach.")

# Plotting vertical dashed line at saturation start
plt.axvline(x=saturation_start, color='red', linestyle='--')

# Adding labels and title
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$T$ ($^{\circ}$ C)')
plt.title('Temperature vs. Time')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Annotate the saturation start point
plt.annotate(f'Saturation starts at {saturation_start:.2f} s', 
             xy=(saturation_start, plt.ylim()[0]),
             xycoords='data',
             xytext=(0.5, 0.2),
             textcoords='axes fraction',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))

plt.tight_layout()
plt.show()

