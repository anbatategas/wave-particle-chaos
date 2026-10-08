import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
k = 2.0
M = 0.1
P_values = [0.001, 0.01, 0.05, 0.1]
T = 2 * np.pi / k  # Period of the driving wave
t_max = 200  # Total integration time
t_eval = np.arange(0, t_max, T)


# Hamiltonian equations
def hamiltonian_system(t, z, M, P, k):
    x, v = z
    dxdt = v
    dvdt = -M * np.sin(x) - P * k * np.sin(k * (x - t))
    return [dxdt, dvdt]


# Initial condition grid
x0_values = np.linspace(-np.pi, np.pi, 12)
v0_values = [0.1, 0.5, 0.9]

# Plot Poincare sections
for P in P_values:
    plt.figure(figsize=(8, 6))
    for v0 in v0_values:
        for x0 in x0_values:
            sol = solve_ivp(hamiltonian_system, [0, t_max], [x0, v0],
                            args=(M, P, k), t_eval=t_eval, rtol=1e-6, atol=1e-9)
            x_mod = np.mod(sol.y[0] + np.pi, 2 * np.pi) - np.pi  # wrap to [-π, π]
            plt.plot(x_mod, sol.y[1], 'o', markersize=1)
    plt.title(f'Stroboscopic Poincare Section (P = {P})')
    plt.xlabel('$x$')
    plt.ylabel('$\\dot{x}$')
    plt.grid(True)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.ylim(-0.5, 1.5)
    plt.xlim(-np.pi, np.pi)
    plt.show()
