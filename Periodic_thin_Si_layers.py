import numpy as np
import matplotlib.pyplot as plt

# Number of silicon layers
N = 30

# Refractive indices: Air = 1.0, Silicon = 3.48
n = np.concatenate(([1.0], np.tile([3.48, 1.0], N)))

# Thicknesses of the internal regions (nm): Si = 1 nm, Air gap = 500 nm
d = np.tile([1.0, 500.0], N)

# Remove the last unnecessary air-gap thickness
d = d[:-1]

# Wavelength range (nm)
lam = np.linspace(200, 3000, 5000)

# Initialize transmission and reflection arrays
tau = np.zeros_like(lam)
rho = np.zeros_like(lam)

# Loop over wavelengths
for m, wavelength in enumerate(lam):
    k0 = 2 * np.pi / wavelength

    # First interface (Python 0-based indexing: n[0] -> n[1])
    n1 = n[0]
    n2 = n[1]

    T = np.array([[(n1 + n2) / (2 * n2), (n2 - n1) / (2 * n2)],
                  [(n2 - n1) / (2 * n2), (n1 + n2) / (2 * n2)]], dtype=complex)

    M = T

    # Propagation and subsequent interfaces
    for i in range(1, len(n) - 1):
        # Propagation through region i
        P = np.array([[np.exp(-1j * n[i] * k0 * d[i - 1]), 0],
                      [0, np.exp(1j * n[i] * k0 * d[i - 1])]], dtype=complex)

        # Interface i -> i+1
        n1 = n[i]
        n2 = n[i + 1]

        T = np.array([[(n1 + n2) / (2 * n2), (n2 - n1) / (2 * n2)],
                      [(n2 - n1) / (2 * n2), (n1 + n2) / (2 * n2)]], dtype=complex)

        # Update total matrix
        M = T @ P @ M

    # Transmission and reflection
    tau[m] = 1.0 / (np.abs(M[1, 1]) ** 2)
    rho[m] = np.abs(M[0, 1] / M[1, 1]) ** 2

# Plot
# --- Figure 1: Plot vs. Wavelength (nm) ---
plt.figure(figsize=(9, 5))
plt.plot(lam, tau, linewidth=1.5, label=r'Transmission $\tau$')
plt.plot(lam, rho, linewidth=1.5, label=r'Reflection $\rho$')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Power coefficient')
plt.title('30 Ultrathin Silicon Layers Separated by Air (vs. Wavelength)')
plt.legend()
plt.grid(True)
plt.ylim([0, 1.05])
plt.xlim([200, 3000])
plt.tight_layout()

# --- Figure 2: Plot vs. Wavenumber k0 (1/nm or 1/um) ---
k0_arr = 2 * np.pi / lam   # Wavenumber in rad/nm (multiply by 1000 for rad/um)

plt.figure(figsize=(9, 5))
plt.plot(k0_arr, tau, linewidth=1.5, label=r'Transmission $\tau$')
plt.plot(k0_arr, rho, linewidth=1.5, label=r'Reflection $\rho$')

plt.xlabel(r'Wavenumber $k_0$ ($\mathrm{nm}^{-1}$)')
plt.ylabel('Power coefficient')
plt.title('30 Ultrathin Silicon Layers Separated by Air (vs. Wavenumber)')
plt.legend()
plt.grid(True)
plt.ylim([0, 1.05])
plt.xlim([np.min(k0_arr), np.max(k0_arr)])
plt.tight_layout()

# Show both figures at the same time
plt.show()

