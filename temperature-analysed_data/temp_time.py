import numpy as np
import matplotlib.pyplot as plt

# Read data
data = np.loadtxt("temptdatt.txt")
t = data[:, 0]
T1 = data[:, 1]
T2 = data[:, 2]

print(len(t))
print(len(T1))
print(len(T2))

# Smooth the data using a moving average
window_size = 50
smoothed_T1 = np.convolve(T1, np.ones(window_size)/window_size, mode='valid')
smoothed_T2 = np.convolve(T2, np.ones(window_size)/window_size, mode='valid')
smoothed_t = t[(window_size - 1):]

# Calculate the saturation temperatures from the smoothed data
saturation_temp1 = np.mean(smoothed_T1[-10:])
saturation_temp2 = np.mean(smoothed_T2[-10:])

# Setting up rcParams for latex font and font size adjustments
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 2

# Plotting
plt.scatter(t, T1, color='black', label='Temp Data 1')
plt.scatter(t, T2, color='green', label='Temp Data 2')
plt.plot(t, T1, color='black')
plt.plot(t, T2, color='green')
plt.plot(smoothed_t, smoothed_T1, color='blue', linestyle='--', label='Smoothed Temp 1')
plt.plot(smoothed_t, smoothed_T2, color='cyan', linestyle='--', label='Smoothed Temp 2')
plt.axhline(y=saturation_temp1, color='r', linestyle='--', label=f'Saturation Temp 1: {saturation_temp1:.2f}°C')
plt.axhline(y=saturation_temp2, color='magenta', linestyle='--', label=f'Saturation Temp 2: {saturation_temp2:.2f}°C')
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$T$ ($^{\circ}$ C)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the saturation temperatures
print(f"Saturation Temperature 1: {saturation_temp1:.2f}°C")
print(f"Saturation Temperature 2: {saturation_temp2:.2f}°C")


