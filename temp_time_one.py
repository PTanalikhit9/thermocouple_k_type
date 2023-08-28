import numpy as np
import matplotlib.pyplot as plt

# Read data
data = np.loadtxt("temptdatt.txt")
t = data[:, 0]
T = data[:, 1]

# Smooth the data using a moving average
window_size = 50
smoothed_T = np.convolve(T, np.ones(window_size)/window_size, mode='valid')
smoothed_t = t[int(window_size/2):-int(window_size/2)+1]

# Calculate the saturation temperature from the smoothed data
saturation_temp = np.mean(smoothed_T[-10:])

# Setting up rcParams for latex font and font size adjustments
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 2

# Plotting
plt.scatter(t, T, color='black')
# plt.plot(t, T, color='black', label='Original Data')
plt.plot(smoothed_t, smoothed_T, color='blue', linestyle='--', label='Smoothed Data')
plt.axhline(y=saturation_temp, color='r', linestyle='--', label=f'Saturation Temp: {saturation_temp:.2f}°C')
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$T$ ($^{\circ}$ C)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the saturation temperature
print(f"Saturation Temperature: {saturation_temp:.2f}°C")

