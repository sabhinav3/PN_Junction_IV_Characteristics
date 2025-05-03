import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.602e-19          # Elementary charge (C)
epsilon_0 = 8.85e-14   # Vacuum permittivity (F/cm)
epsilon_s = 11.7 * epsilon_0  # Silicon permittivity (F/cm)
N_a = 2e15             # p-side doping (cm^-3)
N_d = 1e16             # n-side doping (cm^-3)
V_bi = 0.652           # Built-in potential (V)

# Depletion widths (from Question 1)
W = np.sqrt((2 * epsilon_s / q) * (1/N_a + 1/N_d) * V_bi)
x_p = (N_d / (N_a + N_d)) * W * 1e4  # Convert cm to μm
x_n = (N_a / (N_a + N_d)) * W * 1e4  # Convert cm to μm

# --------------------------------------------------
# Step 1: Generate Electric Field Profile
# --------------------------------------------------
x = np.linspace(-x_p, x_n, 1000)  # Position (μm)
E = np.zeros_like(x)

# Electric field equations
mask_p = (x >= -x_p) & (x <= 0)    # p-side
x_p_cm = x[mask_p] * 1e-4          # Convert μm to cm
E_p = (-q * N_a / epsilon_s) * (x_p_cm + (x_p * 1e-4))  # V/cm
E[mask_p] = E_p

mask_n = (x > 0) & (x <= x_n)      # n-side
x_n_cm = x[mask_n] * 1e-4          # Convert μm to cm
E_n = (q * N_d / epsilon_s) * (x_n * 1e-4 - x_n_cm)     # V/cm
E[mask_n] = E_n

# Convert E to V/μm for plotting
E_plot = E / 1e4  # 1 V/cm = 1e-4 V/μm

# --------------------------------------------------
# Step 2: Plot Electric Field Profile
# --------------------------------------------------
plt.figure(figsize=(10, 5))

# Plot electric field
plt.plot(x, E_plot, 'b', linewidth=2, label="Electric Field")

# Annotate regions
plt.axvspan(-x_p, 0, color='red', alpha=0.1, label='p-doped')
plt.axvspan(0, x_n, color='blue', alpha=0.1, label='n-doped')
plt.axvline(-x_p, color='gray', linestyle='--', linewidth=1, label='Depletion Edges')
plt.axvline(x_n, color='gray', linestyle='--', linewidth=1)

# Add numerical results (E_max)
E_max = np.max(np.abs(E_plot))
plt.gca().text(
    0.05, 0.95,  # Position: 5% from left, 95% from bottom (top-left)
    f"Max Electric Field: {E_max:.2f} V/μm",
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment='top',
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none')
)

# Add direction annotation
plt.annotate('', xy=(0, 0), xytext=(0, -E_max*0.8),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=2))

# Labels and styling
plt.title("Electric Field Profile in PN Junction", fontsize=14)
plt.xlabel("Position (μm)", fontsize=12)
plt.ylabel("Electric Field (V/μm)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper left', bbox_to_anchor=(0.05, 0.85))

# Add region labels
plt.text(-x_p/2, np.min(E_plot)*0.8, 'Space Charge Region', ha='center', fontsize=10)
plt.text(x_n/2, np.max(E_plot)*0.8, 'Space Charge Region', ha='center', fontsize=10)
plt.text(-x_p*1.5, 0, 'Neutral Region\n(p-doped)', ha='center', fontsize=10)
plt.text(x_n*1.5, 0, 'Neutral Region\n(n-doped)', ha='center', fontsize=10)

plt.show()