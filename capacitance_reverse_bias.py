import numpy as np
import matplotlib.pyplot as plt


q = 1.602e-19          # Elementary charge (C)
epsilon_0 = 8.85e-14   # Vacuum permittivity 
epsilon_s = 11.7 * epsilon_0  # Silicon permittivity (F/cm)
N_a = 2e15             # p-side doping 
N_d = 1e16             # n-side doping
V_bi = 0.652           # Built-in potential (V)

# --------------------------------------------------
# calculating the Capacitance vs Reverse Bias
# --------------------------------------------------
def depletion_width(V_R):
    """Compute depletion width for a given reverse bias voltage."""
    return np.sqrt(
        (2 * epsilon_s / q) * (1/N_a + 1/N_d) * (V_bi + V_R)
    )

# generating the reverse bias voltages (0 to 10 V)
V_R = np.linspace(0, 10, 100)
C_j = epsilon_s / depletion_width(V_R)  # F/cm²
C_j_nF = C_j * 1e9  # Convert to nF/cm²

# --------------------------------------------------
# Plotting the Capacitance vs Reverse Bias
# --------------------------------------------------
plt.figure(figsize=(10, 6))


plt.plot(V_R, C_j_nF, 'b-', linewidth=2, label="Junction Capacitance")


plt.title("Junction Capacitance vs Reverse Bias Voltage", fontsize=14)
plt.xlabel("Reverse Bias Voltage (V)", fontsize=12)
plt.ylabel("Capacitance (nF/cm²)", fontsize=12)
plt.xticks(np.arange(0, 11, 1), fontsize=10)
plt.yticks(np.arange(0, 16, 2), fontsize=10) 
plt.grid(True, linestyle='--', alpha=0.6)


plt.text(0.5, C_j_nF[0] + 0.5, 
         f"C_j(0 V) = {C_j_nF[0]:.2f} nF/cm²", 
         fontsize=10, 
         bbox=dict(facecolor='white', alpha=0.8))

plt.legend()
plt.tight_layout()
plt.show()