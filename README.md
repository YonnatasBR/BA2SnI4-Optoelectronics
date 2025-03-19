# BA2SnI4 Data Repository for reproducibility purposes
This repository possesses input/output data suitable to the study titled "BA2SnI4 as a Promising 2D Ruddlesden-Popper Perovskite for Optoelectronic Applications"

# Manuscript Information
Lead-free 2D hybrid metal halide perovskites (MHPs) emerge as promising eco-friendly alternatives to lead-based counterparts, offering excellent thermodynamic stability and environmental compatibility despite lower solar harvesting efficiency. Nonetheless, the dearth of research on tin-based MHPs illustrates the difficulties in their optoelectronic characterization. Herein, we present a computational protocol that integrates ab initio and semi-empirical approaches to investigate the electronic, optical, and excitonic properties of the scarcely explored BA2SnI4, where BA represents butylammonium. We apply a cost-effective computational framework that combines a maximally localized Wannier function tight-binding (MLWF-TB) method for electronic states with the Bethe-Salpeter equation (BSE) for excitonic properties. To improve the accuracy of the electronic band gap, we employ a relativistic quasi-particle correction (DFT-1/2) within the density functional theory (DFT) framework, which also includes van der Waals corrections and spin-orbit coupling effects. Our findings reveal that replacing Pb with
Sn weakens exciton binding, leading to lower exciton binding energies and improved charge extraction efficiency. These results indicate a band gap of 2.0 eV, an exciton ground state energy of 1.85 eV, and an exciton binding energy
of 150 meV. The BSE calculations also predict a redshift in absorption, extending the spectral response further into the visible range, compared to the independent particle approximation (IPA). 2D RP BA2SnI4 perovskite is a promising photovoltaic material since even in ultrathin films smaller than 0.25 μm, this material can achieve PCE values near 25%, close to the Shockley-Queisser limit. Although Sn-based 2D MHPs present advantageous features, more work is required to resolve manufacturing issues and enhance performance stability.

## Table of Contents
This README information about the stored data and folders:

1.***DOS***: density of states calculation for VASP-PBE+D3+SOC-1/2;

2.***BANDS-densePATH***: two-step electronic band structure calculation for VASP-PBE+D3+SOC-1/2 while calculating (1) charge density and (2) the eigenvalues along an initial and dense k-path inside the Brillouin Zone (BZ);

3.***BANDS-simplePATH***: two-step electronic band structure calculation for VASP-PBE+D3+SOC-1/2 while calculating (1) charge density and (2) the eigenvalues along a final and simpler k-path inside the Brillouin Zone (BZ);

4.***vasp2w90&Hamiltonian***: two-step calculation including (1) VASP-PBE+D3+SOC-1/2 to Wannier90 pré-wannierization and (2) Wannier90 wannierization to generate the tight-binding-based maximally-localised wannier functions Hamiltonian (MLWF-TB Hamiltonian);

5.***WanTiBEXOS***: mult-step calculation to investigate optoelectronic properties in the scope of the independent particle approximation (IPA) and Beth-Salpeter equations (BSE). we divided it between bandgap, dos, optical properties, excitonic properties, and power conversion efficiency (PCE) calculations.
