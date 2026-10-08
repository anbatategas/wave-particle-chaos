# Part A : Phase Space of single-wave case (P=0).

# Import required packages
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
M = 0.1  # dimensionless wave amplitude for single-wave case

# Phase space grid
x_values = np.linspace(-3*np.pi, 3*np.pi, 400)
v_values = np.linspace(-2.0, 2.0, 400)
X, V = np.meshgrid(x_values, v_values)

# Hamiltonian: H = 0.5*v^2 - M*cos(x)
H = V ** 2 / 2 - M * np.cos(X)

# Plot phase space
plt.figure(figsize=(10, 6))
contours = plt.contour(X, V, H, levels=40, cmap='plasma')
plt.xlabel(r'$x$')
plt.ylabel(r'$\dot{x}$')
plt.title('Phase Space Contours (P = 0, $H = \\dot{x}^2/2 - M\\cos(x)$)')
plt.grid(True)
plt.colorbar(contours, label='Hamiltonian H')
plt.axhline(0, color='k', linestyle='--', linewidth=0.5)
plt.axvline(0, color='k', linestyle='--', linewidth=0.5)

# Fixed point labels
fixed_points = [-3*np.pi, -2*np.pi, -np.pi, 0, np.pi, 2*np.pi, 3*np.pi]
labels = [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$']
for x_fp, label in zip(fixed_points, labels):
    plt.axvline(x_fp, color='gray', linestyle='--', linewidth=0.5)
    plt.text(x_fp, -0.15, label, ha='center', va='bottom', fontsize=8, color='black')

# Separatrix: H = M
plt.contour(X, V, H, levels=[M], colors='red', linewidths=1.0, linestyles='--')

plt.show()
