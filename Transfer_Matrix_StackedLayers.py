import numpy as np
import matplotlib.pyplot as plt

# Material refractive indices (11 regions: Air, SiO2, Si, ..., Air)
n = np.array([1.0, 1.44, 3.48, 1.44, 3.48, 
              1.44, 3.48, 1.44, 3.48, 1.44, 1.0])

# Thickness of the internal layers (nm) - 9 internal layers (regions 2 to 10)
d = np.array([800, 330, 800, 330, 800, 
              330, 800, 330, 800], dtype=float)

# Wavelength range (nm)
lam = np.linspace(1000, 2000, 2000)

# Initialize transmission and reflection arrays
tau = np.zeros_like(lam)
rho = np.zeros_like(lam)

# Loop over wavelengths
for m, wavelength in enumerate(lam):
    k0 = 2 * np.pi / wavelength

    # First interface: region 1 -> region 2 (Python 0-based indexing: n[0] -> n[1])
    n1 = n[0]
    n2 = n[1]

    T = np.array([[(n1 + n2) / (2 * n2), (n2 - n1) / (2 * n2)],
                  [(n2 - n1) / (2 * n2), (n1 + n2) / (2 * n2)]], dtype=complex)

    M = T

    # Add propagation and subsequent interfaces (regions 2 to 10 -> indices 1 to 9)
    for i in range(1, 10):
        # Propagation through region i
        P = np.array([[np.exp(-1j * n[i] * k0 * d[i - 1]), 0],
                      [0, np.exp(1j * n[i] * k0 * d[i - 1])]], dtype=complex)

        # Interface from region i to region i+1
        n1 = n[i]
        n2 = n[i + 1]

        T = np.array([[(n1 + n2) / (2 * n2), (n2 - n1) / (2 * n2)],
                      [(n2 - n1) / (2 * n2), (n1 + n2) / (2 * n2)]], dtype=complex)

        # Update total matrix (use @ for matrix multiplication in Python)
        M = T @ P @ M

    # Transmission and reflection (right-to-left incidence)
    # Note: MATLAB M(2,2) is M[1, 1] and M(1,2) is M[0, 1] in Python
    tau[m] = 1.0 / (np.abs(M[1, 1]) ** 2)
    rho[m] = np.abs(M[0, 1] / M[1, 1]) ** 2

# Plot transmission and reflection
plt.figure(figsize=(9, 5))
plt.plot(lam, tau, linewidth=1.5, label=r'Transmission $\tau$')
plt.plot(lam, rho, linewidth=1.5, label=r'Reflection $\rho$')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Power coefficient')
plt.title('Transmission and Reflection of Multilayer Stack')
plt.legend()
plt.grid(True)
plt.ylim([0, 1.05])
plt.xlim([1000, 2000])
plt.tight_layout()
plt.show()
