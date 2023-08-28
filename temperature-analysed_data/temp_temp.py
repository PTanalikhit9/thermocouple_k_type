import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define linear function for fit
def linear_func(T, a, b):
    return a * T + b

# Read data
data = np.loadtxt("TT.txt", skiprows=1)  # skipping the header row
T = data[:, 0]
T_response = data[:, 1]

# Fit data with linear function
params, _ = curve_fit(linear_func, T, T_response)
a, b = params

# Interpolate the data
T_100_response = linear_func(100, a, b)
T_330_response = linear_func(330, a, b)

# Setting up rcParams for the look of the plot
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.linewidth'] = 2

# Plotting
plt.scatter(T, T_response, color='black', label='Data')
plt.plot(T, linear_func(T, a, b), color='blue', linestyle='--', 
         label=f'$T_{{response}} = {a:.3f} T + {b:.2f}$')
# Get axis limits to position annotations at bottom right
x_max, y_min = plt.gca().get_xlim()[1], plt.gca().get_ylim()[0]

# Annotate the interpolated values in the bottom right
vertical_offset = (plt.gca().get_ylim()[1] - y_min) * 0.05  # 5% of y-axis range

plt.annotate(r'$T_{response}(100^{\circ}C)$' + f' = {T_100_response:.2f}°C',
             (x_max, y_min + vertical_offset), 
             xycoords='data',
             textcoords="offset points", 
             xytext=(-10, 20),  # offset from the bottom right
             ha='right')

plt.annotate(r'$T_{response}(330^{\circ}C)$' + f' = {T_330_response:.2f}°C',
             (x_max, y_min), 
             xycoords='data',
             textcoords="offset points", 
             xytext=(-10, 10),  # offset from the bottom right
             ha='right')

# plt.annotate(r'$T_{response}(50^{\circ}C)$' + f' = {T_50_response:.2f}°C', 
#              (50, T_50_response), textcoords="offset points", xytext=(0,10), ha='center')
# plt.annotate(r'$T_{response}(100^{\circ}C)$' + f' = {T_100_response:.2f}°C', 
#              (100, T_100_response), textcoords="offset points", xytext=(0,10), ha='center')

# Additional plot settings
plt.xlabel('Temp ($^{\circ}$ C)')
plt.ylabel('Response Temp ($^{\circ}$ C)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

# Print the interpolated values
print(f'T_response(100°C) = {T_100_response:.2f}°C')
print(f'T_response(330°C) = {T_330_response:.2f}°C')
