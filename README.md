# PN Junction Characteristics Analysis

A Python-based project to analyze the electrical and physical characteristics of a PN junction diode. This repository includes scripts to calculate and visualize key parameters such as depletion width, electric field, potential, capacitance, minority carrier distribution, I-V characteristics, and band diagrams under different bias conditions.

## 📋 Project Overview
- **Material**: Silicon PN junction.
- **Doping Concentrations**:
  - p-side: \( N_a = 2 \times 10^{15} \, \text{cm}^{-3} \)
  - n-side: \( N_d = 10^{16} \, \text{cm}^{-3} \)
- **Key Parameters**: Built-in potential (\( V_{bi} \)), depletion width (\( W \)), electric field (\( E \)), junction capacitance (\( C_j \)), and minority carrier concentrations.

## 📌 Questions Addressed
1. **Depletion Layer Width & Charge Profile**  
   Calculate \( W \), \( x_p \), \( x_n \), and plot charge density.  
2. **Electric Field Profile**  
   Compute and visualize the triangular electric field in the depletion region.  
3. **Electrostatic Potential**  
   Plot the parabolic potential across the junction.  
4. **Capacitance vs Reverse Bias**  
   Characterize \( C_j \) as a function of reverse voltage.  
5. **Minority Carrier Distribution**  
   Plot carrier concentrations in neutral and depletion regions (log/linear scale).  
6. **I-V Characteristics**  
   Simulate forward/reverse bias current-voltage curves for Si and Ge diodes.  
7. **Band Diagrams**  
   Visualize conduction/valence bands under zero, forward, and reverse bias.

## 🛠️ Prerequisites
- Python 3.8+
- Libraries: `numpy`, `matplotlib`  
  Install dependencies:  
  ```bash
  pip install numpy matplotlib
