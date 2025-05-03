# Charge Depletion in a PN Junction - Q1

import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.602e-19          # Elementary charge (C)
k_B = 1.38e-23         # Boltzmann constant (J/K)
T = 300                # Temperature (K)
epsilon_0 = 8.85e-14   # Vacuum permittivity (F/cm)
epsilon_s = 11.7 * epsilon_0  # Silicon permittivity (F/cm)
n_i = 1.5e10           # Intrinsic carrier concentration (cm^-3)

# Doping concentrations
N_a = 2e15             # p-side doping (cm^-3)
N_d = 1e16             # n-side doping (cm^-3)

# --------------------------------------------------
# Step 1: Calculate Built-in Potential (V_bi)
# --------------------------------------------------
V_bi = (k_B * T / q) * np.log((N_a * N_d) / (n_i ** 2))

# --------------------------------------------------
# Step 2: Calculate Depletion Widths (W, x_p, x_n)
# --------------------------------------------------
W = np.sqrt((2 * epsilon_s / q) * (1/N_a + 1/N_d) * V_bi)
W_micron = W * 1e4  # Convert cm to μm
x_p = (N_d / (N_a + N_d)) * W * 1e4  # μm
x_n = (N_a / (N_a + N_d)) * W * 1e4  # μm

# --------------------------------------------------
# Step 3: Generate Charge Profile
# --------------------------------------------------
x = np.linspace(-x_p, x_n, 1000)  # Position (μm)
rho = np.zeros_like(x)
rho[(x >= -x_p) & (x <= 0)] = -q * N_a  # p-side (C/cm³)
rho[(x > 0) & (x <= x_n)] = q * N_d      # n-side (C/cm³)

# --------------------------------------------------
# Step 4: Plot Charge Profile with Annotations
# --------------------------------------------------
plt.figure(figsize=(10, 5))

# Plot charge density
plt.plot(x, rho, 'k', linewidth=2, label="Charge Density")

# Annotate regions
plt.axvspan(-x_p, 0, color='red', alpha=0.1, label='p-doped')
plt.axvspan(0, x_n, color='blue', alpha=0.1, label='n-doped')
plt.axvline(-x_p, color='gray', linestyle='--', linewidth=1, label='Depletion Edges')
plt.axvline(x_n, color='gray', linestyle='--', linewidth=1)

# Add numerical results in top-left corner (axes coordinates)
textstr = f'Built-in Potential (V_bi): {V_bi:.3f} V\nTotal Depletion Width (W): {W_micron:.3f} μm'
plt.gca().text(
    0.05, 0.95,  # Position: 5% from left, 95% from bottom (top-left)
    textstr,
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none')
)

# Labels and styling
plt.title("Charge Profile of PN Junction", fontsize=14)
plt.xlabel("Position (μm)", fontsize=12)
plt.ylabel("Charge Density (C/cm³)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper left', bbox_to_anchor=(0.05, 0.85))  # Adjusted legend position

# Add region labels
plt.text(-x_p/2, np.min(rho)*0.8, 'Space Charge Region', ha='center', fontsize=10)
plt.text(x_n/2, np.max(rho)*0.8, 'Space Charge Region', ha='center', fontsize=10)
plt.text(-x_p*1.5, 0, 'Neutral Region\n(p-doped)', ha='center', fontsize=10)
plt.text(x_n*1.5, 0, 'Neutral Region\n(n-doped)', ha='center', fontsize=10)

plt.show()