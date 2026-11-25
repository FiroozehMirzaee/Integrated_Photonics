# Integrated_Photonics
# Integrated Photonics — Transfer Matrix Method (TMM) Simulations

This repository contains Python simulations for analyzing electromagnetic wave propagation, power transmission ($\tau$), and power reflection ($\rho$) through 1D multilayer dielectric stacks using the **Transfer Matrix Method (TMM)**.

## Scripts Overview

### 1. `Transfer_Matrix_StackedLayers.py`
* **Structure:** 11-region multilayer stack consisting of alternating $\text{SiO}_2$ ($n = 1.44$, $d = 800\text{ nm}$) and $\text{Si}$ ($n = 3.48$, $d = 330\text{ nm}$) layers surrounded by air ($n = 1$).
* **Analysis:** Computes and plots the wavelength-dependent power transmission $\tau(\lambda)$ and reflection $\rho(\lambda)$ in the range of $1000\text{ nm}$ to $2000\text{ nm}$ under normal right-to-left incidence.

### 2. `Periodic_thin_Si_layers.py`
* **Structure:** Periodic stack of $N = 30$ ultrathin Silicon layers ($n = 3.48$, $d = 1\text{ nm}$) separated by air gaps ($n = 1$, $d = 500\text{ nm}$).
* **Analysis:** Evaluates $\tau$ and $\rho$ over a broad spectral range ($200\text{ nm}$ to $3000\text{ nm}$) and illustrates the photonic bandgap behavior as a function of both **wavelength ($\lambda$)** and **wavenumber ($k_0$)**.

## Requirements & Usage
To run the simulations, ensure you have Python installed along with `numpy` and `matplotlib`:

```bash
pip install numpy matplotlib
