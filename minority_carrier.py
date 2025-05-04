import numpy as np
import matplotlib.pyplot as plt

# Constants
N_a = 2e15             # p-side doping (cm⁻³)
N_d = 1e16             # n-side doping (cm⁻³)
n_i = 1.5e10           # Intrinsic carrier concentration (cm⁻³)
x_p = 0.592            # p-side depletion width (μm)
x_n = 0.119            # n-side depletion width (μm)


n_p0 = (n_i ** 2) / N_a  
p_n0 = (n_i ** 2) / N_d  


x = np.linspace(-x_p - 0.5, x_n + 0.5, 1000) 


n_p = np.zeros_like(x)  # Electrons in p-side
p_n = np.zeros_like(x)  # Holes in n-side


n_p[x < -x_p] = n_p0    
p_n[x > x_n] = p_n0     

n_p[(x >= -x_p) & (x <= x_n)] = 0
p_n[(x >= -x_p) & (x <= x_n)] = 0


plt.figure(figsize=(10, 6))


plt.plot(x, n_p, 'b', linewidth=2, label="$n_p(x)$ (p-side electrons)")
plt.plot(x, p_n, 'r', linewidth=2, label="$p_n(x)$ (n-side holes)")


plt.hlines(n_p0, -x_p - 0.5, -x_p, color='blue', linestyle='--', linewidth=1)
plt.hlines(p_n0, x_n, x_n + 0.5, color='red', linestyle='--', linewidth=1)


plt.axvspan(-x_p, x_n, color='gray', alpha=0.2, label="Depletion Region")


plt.axvline(-x_p, color='k', linestyle='--', linewidth=1)
plt.axvline(x_n, color='k', linestyle='--', linewidth=1)
plt.axvline(0, color='k', linestyle=':', linewidth=1)


plt.text(-x_p - 0.4, n_p0 + 1e4, 'p-neutral\n$N_a = 2 \\times 10^{15} \, \mathrm{cm}^{-3}$', 
         ha='right', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
plt.text(x_n + 0.4, p_n0 + 1e4, 'n-neutral\n$N_d = 10^{16} \, \mathrm{cm}^{-3}$', 
         ha='left', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
plt.text(0, (n_p0 + p_n0)/2, 'Depletion Region\n$n_p, p_n \\approx 0$', 
         ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))


plt.text(-x_p - 0.5, n_p0, f'$n_{{p0}} = {n_p0:.1e} \, \mathrm{{cm}}^{{-3}}$', 
         ha='center', fontsize=10, color='blue')
plt.text(x_n + 0.5, p_n0, f'$p_{{n0}} = {p_n0:.1e} \, \mathrm{{cm}}^{{-3}}$', 
         ha='center', fontsize=10, color='red')


plt.title("Minority Carrier Distribution at Thermal Equilibrium", fontsize=14)
plt.xlabel("Position (μm)", fontsize=12)
plt.ylabel("Carrier Concentration (cm⁻³)", fontsize=12)
plt.xticks([-x_p, 0, x_n], [f'$-x_p$', '0', f'$x_n$'], fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

plt.xlim(-x_p - 0.5, x_n + 0.5)
plt.ylim(-1e4, 1.5e5)
plt.tight_layout()
plt.show()