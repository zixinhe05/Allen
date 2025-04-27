import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 0.01  # Inductance in Henry
C = 0.01e-6  # Capacitance in Farad

# Frequency range (w = 2*pi*f)
w = np.linspace(0, 2e5, 1000)  # Angular frequency range from 0 to 200,000 rad/s

# Function to calculate Vin/Vout
def vin_over_vout(w):
    return 1 - w**2 * L * C

# Calculate Vin/Vout for each w
y = vin_over_vout(w)

# Plot
plt.plot(w, y, label=r'$\frac{V_{\text{in}}}{V_{\text{out}}}$')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)  # Add a horizontal line at y=0
plt.xlabel('Angular Frequency (w) [rad/s]')
plt.ylabel(r'$\frac{V_{\text{in}}}{V_{\text{out}}}$')
plt.title(r'$\frac{V_{\text{in}}}{V_{\text{out}}}$ vs Angular Frequency in LC Circuit')
plt.grid(True)
plt.legend()
plt.show()

