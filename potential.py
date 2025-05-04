import numpy as np
import matplotlib.pyplot as plt


q = 1.602e-19          # Elementary charge (C)
epsilon_0 = 8.85e-14   # Vacuum permittivity (F/cm)
epsilon_s = 11.7 * epsilon_0  # Silicon permittivity (F/cm)
N_a = 2e15             # p-side doping (cm⁻³)
N_d = 1e16             # n-side doping (cm⁻³)
n_i = 1.5e10           # Intrinsic carrier concentration (cm⁻³)
k_BT_q = 0.0259        # Thermal voltage (V) at 300 K

# Calculating built-in Potential 
V_bi = k_BT_q * np.log((N_a * N_d) / (n_i ** 2))

# Calculating Depletion Widths
W = np.sqrt((2 * epsilon_s / q) * (1/N_a + 1/N_d) * V_bi)
x_p = (N_d / (N_a + N_d)) * W * 1e4  
x_n = (N_a / (N_a + N_d)) * W * 1e4 


x = np.linspace(-x_p - 1.0, x_n + 1.0, 1000)  
V = np.zeros_like(x)


mask_p = (x >= -x_p) & (x <= 0)
x_p_cm = x[mask_p] * 1e-4  
V_p = - (q * N_a / (2 * epsilon_s)) * (x_p_cm + x_p * 1e-4) ** 2
V[mask_p] = V_p


mask_n = (x > 0) & (x <= x_n)
x_n_cm = x[mask_n] * 1e-4  
V_n = V_bi - (q * N_d / (2 * epsilon_s)) * (x_n * 1e-4 - x_n_cm) ** 2
V[mask_n] = V_n


V[x < -x_p] = 0      
V[x > x_n] = V_bi    


plt.figure(figsize=(12, 6))
ax = plt.gca()

# Plotting the potential
plt.plot(x, V, 'g-', linewidth=2, label="Electrostatic Potential")


ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


plt.xticks(np.arange(-x_p - 1, x_n + 1, 0.5))
plt.yticks(np.arange(-0.2, V_bi + 0.2, 0.1))


plt.axvline(-x_p, color='gray', linestyle='--', linewidth=1, label="Depletion Edges")
plt.axvline(x_n, color='gray', linestyle='--', linewidth=1)
plt.axvspan(-x_p, 0, color='red', alpha=0.1, label='p-doped')
plt.axvspan(0, x_n, color='blue', alpha=0.1, label='n-doped')


plt.text(0.1, 0.95, 
         f"△V (Built-in): {V_bi:.3f} V\nDepletion Width: {W*1e4:.3f} μm", 
         transform=ax.transAxes, 
         fontsize=10, 
         verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8))


plt.text(-x_p - 0.8, 0.05, 'Neutral\np-doped', ha='center', fontsize=10)
plt.text(x_n + 0.8, V_bi - 0.05, 'Neutral\nn-doped', ha='center', fontsize=10)
plt.text(-x_p/2, V_bi/2, 'Space Charge\nRegion', ha='center', fontsize=10, rotation=90)
plt.text(x_n/2, V_bi/2, 'Space Charge\nRegion', ha='center', fontsize=10, rotation=90)
plt.annotate('Voltage Increase →', xy=(x_n + 0.5, V_bi/2), ha='left', fontsize=10)


plt.title("Electrostatic Potential Profile (Full Negative Axes)", fontsize=14)
plt.xlabel("Position (μm)", fontsize=12)
plt.ylabel("Voltage (V)", fontsize=12)
plt.xlim(-x_p - 1, x_n + 1)
plt.ylim(-0.2, V_bi + 0.1)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()