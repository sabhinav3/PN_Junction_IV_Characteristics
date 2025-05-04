import numpy as np
import matplotlib.pyplot as plt


V_T   = 0.0259    # Thermal voltage at 300 K [V]
I0_Si = 1e-12     # Reverse saturation current for Si [A]
I0_Ge = 1e-6      # Reverse saturation current for Ge [A]
n     = 1         # Ideality factor

def diode_current(V, I0, V_knee):
    if V >= V_knee:
        return 1e-3           
    elif V > 0:
        return I0 * (np.exp(V/(n*V_T)) - 1)
    else:
        return -1e-3         

V = np.linspace(-1.0, 1.0, 1000)
I_Si = np.array([diode_current(v, I0_Si, 0.7) * 1e3 for v in V])
I_Ge = np.array([diode_current(v, I0_Ge, 0.3) * 1e3 for v in V])


# Plotting the graph

plt.figure(figsize=(8, 6))

# Silicon and Germanium curves
plt.plot(V, I_Si, 'b-', lw=2, label='Silicon (0.7 V knee)')
plt.plot(V, I_Ge, 'g-', lw=2, label='Germanium (0.3 V knee)')


plt.fill_between(V, I_Si, where=(V>0), color='lavender', alpha=0.5)


for V_knee, col, txt in [(0.3, 'g', 'Ge: 0.3 V'), (0.7, 'b', 'Si: 0.7 V')]:
    plt.axvline(V_knee, color=col, ls='--', lw=1.5)
    plt.text(V_knee, 9.5, txt, ha='center', va='bottom', color=col, fontsize=11)


plt.xlim(-1.0, 1.0)
plt.ylim(-10.0, 10.0)
plt.xticks([-1.0, -0.5, 0, 0.3, 0.7, 1.0])
plt.yticks([-10, -5, 0, 5, 10])


plt.xlabel('Forward/Reverse Voltage +V →', fontsize=12)
plt.ylabel('Current +I (mA) ↑ / –I (mA) ↓', fontsize=12)
plt.title('PN Junction Diode I–V Characteristics', fontsize=14)
plt.grid(True, ls='--', alpha=0.6)


plt.text(-0.6, -9.0, 'Reverse bias\n(–1 mA plateau)', color='red',
         ha='center', va='top', fontsize=11)


plt.text(0.5, 9.0, 'Forward bias', color='black',
         ha='center', va='bottom', fontsize=13, weight='bold')

plt.legend(loc='lower right')
plt.tight_layout()
plt.show()
