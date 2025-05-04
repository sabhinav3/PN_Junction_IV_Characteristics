import numpy as np
import matplotlib.pyplot as plt


q = 1.602e-19          # Elementary charge (C)
epsilon_0 = 8.85e-14   # Vacuum permittivity (F/cm)
epsilon_s = 11.7 * epsilon_0  # Silicon permittivity (F/cm)
N_a = 2e15             # p-side doping (cm⁻³)
N_d = 1e16             # n-side doping (cm⁻³)
n_i = 1.5e10           # Intrinsic carrier concentration (cm⁻³)
k_BT_q = 0.0259        # Thermal voltage (V) at 300 K
E_g = 1.12             # Silicon bandgap (eV)


V_bi = k_BT_q * np.log((N_a * N_d) / (n_i ** 2))
print(f"Built-in Potential (V_bi): {V_bi:.3f} V")


 # Computing the Band Diagram

def plot_band_diagram(V_applied, title):

    W = np.sqrt((2 * epsilon_s / q) * (1/N_a + 1/N_d) * (V_bi - V_applied))
    x_p = (N_d / (N_a + N_d)) * W * 1e4  
    x_n = (N_a / (N_a + N_d)) * W * 1e4  


    x = np.linspace(-x_p - 0.5, x_n + 0.5, 1000)
    V = np.zeros_like(x)  

   
    mask_p = (x >= -x_p) & (x <= 0)
    x_p_cm = x[mask_p] * 1e-4  
    V_p = - (q * N_a / (2 * epsilon_s)) * (x_p_cm + (x_p * 1e-4)) ** 2
    V[mask_p] = V_p


    mask_n = (x >= 0) & (x <= x_n)
    x_n_cm = x[mask_n] * 1e-4  
    V_n = V_bi - (q * N_d / (2 * epsilon_s)) * ((x_n * 1e-4) - x_n_cm) ** 2
    V[mask_n] = V_n

  
    E_c = -V  
    E_v = E_c - E_g  

    # Plotting the band diagram
    plt.figure(figsize=(8, 6))
    plt.plot(x, E_c, 'b', linewidth=2, label="$E_c$ (Conduction Band)")
    plt.plot(x, E_v, 'r', linewidth=2, label="$E_v$ (Valence Band)")

   
    plt.axvline(-x_p, color='k', linestyle='--', linewidth=1, label="Depletion Edges")
    plt.axvline(x_n, color='k', linestyle='--', linewidth=1)
    plt.text(-x_p/2, E_c.max()/2, f'$qV_{{bi}}$ = {V_bi:.2f} eV', ha='center', fontsize=10)
    if V_applied != 0:
        delta_V = V_bi - V_applied if V_applied > 0 else V_bi + abs(V_applied)
        plt.text(x_n/2, E_c.min()/2, f'$q(V_{{bi}} {"-" if V_applied >0 else "+"} {abs(V_applied):.1f})$ = {delta_V:.2f} eV', ha='center', fontsize=10)

    plt.title(title, fontsize=14)
    plt.xlabel("Position (μm)", fontsize=12)
    plt.ylabel("Energy (eV)", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.show()

plot_band_diagram(0, "Zero Bias")
plot_band_diagram(0.5, "Forward Bias (V_F = 0.5 V)")
plot_band_diagram(-5, "Reverse Bias (V_R = -5 V)")