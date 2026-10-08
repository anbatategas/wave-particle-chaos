# Wave-Particle Interaction & Chaos Analysis

This repository contains the computational analysis of the non-linear dynamics of a charged particle interacting with counter-propagating electrostatic waves. The project bridges fundamental Hamiltonian mechanics with chaos theory, demonstrating the transition from regular orbits to global chaos via KAM theorem breakdown and the Chirikov resonance overlap criterion.

This work was developed for the *Introduction to the Science & Technology of Controlled Thermonuclear Fusion* course at the National Technical University of Athens (NTUA). The full theoretical proofs and extended phase space maps can be found in the included PDF report.

## The Physics Model

The system models a charged particle (mass $m$, charge $-e$) interacting with two electrostatic waves. By shifting to the rest frame of the primary wave and applying a scale transformation, the dimensionless Hamiltonian of the system is given by:

$$\mathcal{H}(x,v,t) = \frac{1}{2}v^2 - M \cos x - P \cos(k(x-t))$$

Where:
* $M$ represents the depth of the static potential (primary wave).
* $P$ is the perturbation magnitude (secondary counter-propagating wave).
* $k$ is the wavenumber ratio between the two waves.

### Unperturbed System ($P = 0$)
In the absence of the secondary wave, the system reduces to a non-linear pendulum:

$$
\mathcal{H}_0(x,v) = \frac{1}{2}v^2 - M \cos x
$$

The phase space consists of stable and unstable fixed points, separated by a separatrix with a half-width of $\Delta v_{sep}^{(1/2)} = 2\sqrt{M}$. Orbits within the separatrix are librational (trapped), while orbits outside are rotational.

### Perturbed System & Chaos ($P > 0$)
When $P > 0$, the time-dependent perturbation disrupts the invariant KAM tori. Resonances occur when the unperturbed frequency matches the perturbation frequency. As $P$ increases, these resonance islands widen and eventually overlap (Chirikov criterion), leading to chaotic scattering near the separatrix and a transition to a mixed or globally chaotic phase space.

## Repository Structure

* `PartA_PhaseSpace.py`: Integrates and plots the unperturbed Hamiltonian ($P=0$). It generates the phase space contours, identifies stable/unstable fixed points, and overlays the separatrix.
* `PartB_StroboscopicPoincareSection.py`: Numerically integrates the perturbed Hamiltonian system ($P > 0$) using `scipy.integrate.solve_ivp`. It constructs stroboscopic Poincaré sections wrapped to the interval $[-\pi, \pi]$ to visualize the breakdown of KAM tori and the onset of chaos for various values of $P$.
* `Wave_Particle_Chaos_Report.pdf`: The complete academic coursework containing rigorous mathematical derivations, stability analysis, and extended stroboscopic plots. *(Written in Greek; math and code are in universal scientific notation).*

## Requirements and Usage

The scripts require standard scientific Python libraries:
* `numpy`
* `matplotlib`
* `scipy`

To run the phase space analysis:
```bash
python PartA_PhaseSpace.py
