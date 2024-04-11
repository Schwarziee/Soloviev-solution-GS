import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the range for x and y
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

inite= 0.33
initau=-0.5
initsigma=1

# Create a meshgrid for x and y
x, y = np.meshgrid(x, y)

# Function to calculate psi2(x, y) with parameters as variables
def psi2(x, y, e, tau, sigma):
    return (x - (e / 2) * (1 - x**2))**2 + (1 - (e**2 / 4)) * (1 + tau * e * x * (2 + e * x)) * (y**2 / sigma**2)

# Initialize contour plot
fig, ax = plt.subplots(figsize=(8, 6))
contour = None

# Function to update the plot based on slider values
def update(val):
    global contour
    e = slider_e.val
    tau = slider_tau.val
    sigma = slider_sigma.val
    
    # Calculate the function psi2(x, y)
    z = psi2(x, y, e, tau, sigma)
    
    # Update the contour plot
    if contour:
        for coll in contour.collections:
            coll.remove()
    contour = ax.contour(x, y, z, levels=50, colors='black')
    ax.figure.canvas.draw_idle()

# Create sliders for parameters
plt.subplots_adjust(bottom=0.25)
slider_ax_e = plt.axes([0.1, 0.1, 0.65, 0.03])
slider_ax_tau = plt.axes([0.1, 0.05, 0.65, 0.03])
slider_ax_sigma = plt.axes([0.1, 0.15, 0.65, 0.03])

slider_e = Slider(slider_ax_e, 'e', 0.1, 1.0, valinit=inite)
slider_tau = Slider(slider_ax_tau, 'tau', -1.0, 1.0, valinit=initau)
slider_sigma = Slider(slider_ax_sigma, 'sigma', 0.1, 2.0, valinit=initsigma)

slider_e.on_changed(update)
slider_tau.on_changed(update)
slider_sigma.on_changed(update)

# Calculate the initial function psi2(x, y)
z_initial = psi2(x, y, slider_e.val, slider_tau.val, slider_sigma.val)

# Plot the initial contour
contour = ax.contour(x, y, z_initial, levels=50, colors='black')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Contour plot of psi2(x, y)')
ax.grid(False)

plt.show()
