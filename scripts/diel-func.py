
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.offsetbox import AnchoredText

# Functions
def py_grep(file_path, search_string):
    with open(file_path, 'r') as file:
        for line in file:
            if search_string in line:

                string = line.strip()
                string = string.split()

    return string

# loading the font style
plt.rcParams['text.usetex'] = True
fonte = {'family': 'serif', 'serif': ['Liberation Serif']}
# fonte = {'family':'sans-serif','sans-serif':['Helvetica']}
plt.rc('font', **fonte)

# line, spine and markers width
gro   = 1.0
grol  = 1.5
mkgro = 1.0

# format text size
tam=15

# figure formating, shape, etc.
fig = plt.figure(figsize=(8, 6))
gs = fig.add_gridspec(3, 2)
fig.subplots_adjust(left=0.09, wspace=0.4, hspace=0.03, right=0.975, top=0.985, bottom=0.09)

# plot 1: real x
ax1 = fig.add_subplot(gs[0, 0]) 

# plot 2: im x
ax2 = fig.add_subplot(gs[0, 1]) 

# plot 3: real y
ax3 = fig.add_subplot(gs[1, 0]) 

# plot 4: im y
ax4 = fig.add_subplot(gs[1, 1]) 

# plot 3: real y
ax5 = fig.add_subplot(gs[2, 0]) 

# plot 4: im y
ax6 = fig.add_subplot(gs[2, 1]) 


# finding the exciton ground state energy from outputfile 'log_bse-diel.dat'
file_path = 'out/log_bse-diel.dat'
search_strings = 'exciton ground state'
desireble_column = 3

found_line = py_grep(file_path, search_strings)
e1s = float(found_line[desireble_column])
print('# Exciton ground state energy: {:.5f} (eV)'.format(e1s))

# finding the direct band gap from outputfile 'gap-kpath.dat'
file_path = 'out/gap-kmesh.dat'
search_strings = 'direct band gap (eV)'
desireble_column = 4

found_line = py_grep(file_path, search_strings)
eg = float(found_line[desireble_column])
print('# Direct band gap energy: {:.5f} (eV)'.format(eg))

# drawing vertical lines corresponding to exciton ground state and band gap energies
for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    ax.axvline(x=e1s, color='gray', linestyle=':',
                linewidth=gro,
                zorder=2
               )
    ax.axvline(x=eg, color='gray', linestyle=':',
                linewidth=gro,
                zorder=2
               )
    


# data from ipa_diel-pol_x.dat
energy, real, imag = np.loadtxt('out/ipa_diel_xx.dat', 
                                    usecols=(0, 1, 2), unpack=True).astype(float)


# alpha_x ----------------------------------------------#
ax1.plot(energy[2252:5252], real[2252:5252], color='blue', label= r'(IPA)',
             linestyle='solid', linewidth=gro)

ax2.plot(energy[2252:5252], imag[2252:5252], color='blue', label= r'(IPA)',
             linestyle='solid', linewidth=gro)

# fill below curves
ax1.fill_between(energy[2252:5252], real[2252:5252], 0, color='lightblue', zorder=0)
ax2.fill_between(energy[2252:5252], imag[2252:5252], 0, color='lightblue', zorder=0)

# data from bse_diel-pol_x.dat
energy, real, imag = np.loadtxt('out/bse_diel_xx.dat', 
                                    usecols=(0, 1, 2), unpack=True).astype(float)
# alpha_x ----------------------------------------------#
ax1.plot(energy[2252:5252], real[2252:5252], color='red', label= r'(BSE)',
             linestyle='solid', linewidth=gro)
ax2.plot(energy[2252:5252], imag[2252:5252], color='red', label= r'(BSE)',
             linestyle='solid', linewidth=gro)


# data from ipa_diel-pol_y.dat
energy, real, imag = np.loadtxt('out/ipa_diel_yy.dat', 
                                    usecols=(0, 1, 2), unpack=True).astype(float)
# alpha_y ----------------------------------------------#
ax3.plot(energy[2252:5252], real[2252:5252], color='blue', label= r'(IPA)',
             linestyle='solid', linewidth=gro)
ax4.plot(energy[2252:5252], imag[2252:5252], color='blue', label= r'(IPA)',
             linestyle='solid', linewidth=gro)

# fill below curves
ax3.fill_between(energy[2252:5252], real[2252:5252], 0, color='lightblue', zorder=0)
ax4.fill_between(energy[2252:5252], imag[2252:5252], 0, color='lightblue', zorder=0)

# data from bse_diel-pol_y.dat
energy, real, imag = np.loadtxt('out/bse_diel_yy.dat', 
                                    usecols=(0, 1, 2), unpack=True).astype(float)
# alpha_y ----------------------------------------------#
ax3.plot(energy[2252:5252], real[2252:5252], color='red', label= r'(BSE)',
             linestyle='solid', linewidth=gro)
ax4.plot(energy[2252:5252], imag[2252:5252], color='red', label= r'(BSE)',
             linestyle='solid', linewidth=gro)

# data from ipa_diel-pol_z.dat
energy, real, imag = np.loadtxt('out/ipa_diel_zz.dat', 
                                    usecols=(0, 1, 2), unpack=True).astype(float)
# alpha_z ----------------------------------------------#
ax5.plot(energy[2252:5252], real[2252:5252], color='blue', label= r'(IPA)',
             linestyle='solid', linewidth=gro)
ax6.plot(energy[2252:5252], imag[2252:5252], color='blue', label= r'(IPA)',
             linestyle='solid', linewidth=gro)

# fill below curves
ax5.fill_between(energy[2252:5252], real[2252:5252], 0, color='lightblue', zorder=0)
ax6.fill_between(energy[2252:5252], imag[2252:5252], 0, color='lightblue', zorder=0)

# data from bse_diel-pol_z.dat
energy, real, imag = np.loadtxt('out/bse_diel_zz.dat', 
                                    usecols=(0, 1, 2), unpack=True).astype(float)
# alpha_z ----------------------------------------------#
ax5.plot(energy[2252:5252], real[2252:5252], color='red', label= r'(BSE)',
             linestyle='solid', linewidth=gro)
ax6.plot(energy[2252:5252], imag[2252:5252], color='red', label= r'(BSE)',
             linestyle='solid', linewidth=gro)

# Formating the axes
for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
    # Formating the axes width
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(gro)

    # format ticklables
    ax.tick_params(axis='both', which='both', direction='in', labelsize=tam)
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.tick_params(which='major',length=5,width=gro)
    ax.tick_params(which='minor',length=3,width=gro)
    ax.locator_params(axis='y', nbins=7)
    
    # Adding point and comma after the major ticks in the y axis
    formatter = ticker.StrMethodFormatter("{x:.2f}")
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)

    xinteval = [1.5, 2, 2.5, 3, 3.5, 4] # [0, 1, 2, 3, 4]
    
    # Set axies lables
    if ax==ax1:
        ax.set_ylabel(r'Re $\rm \epsilon_{x, x} (u.a.)$', fontsize=tam)
    
    if ax==ax2:
        ax.set_ylabel(r'Im $\rm \epsilon_{x, x} (u.a.)$', fontsize=tam)
    
    if ax==ax3:
        ax.set_ylabel(r'Re $\rm \epsilon_{y, y} (u.a.)$', fontsize=tam)
    
    if ax==ax4:
        ax.set_ylabel(r'Im $\rm \epsilon_{y, y} (u.a.)$', fontsize=tam)
    
    if ax==ax5:
        ax.set_ylabel(r'Re $\rm \epsilon_{z, z} (u.a.)$', fontsize=tam)
    
    if ax==ax6:
        ax.set_ylabel(r'Im $\rm \epsilon_{z, z} (u.a.)$', fontsize=tam)
        
    
    if ax==ax5 or ax==ax6:
        ax.set_xticks([1.5, 2, 2.5, 3, 3.5])
        ax.set_xlabel('Photon Energy (eV)', fontsize=tam)
        
    else:
        ax.set_xticks([1.5, 2, 2.5, 3, 3.5],[])

    ax.set_xlim(1.5, 3.5) 
    
    # Set axies limits
    if ax==ax1 or ax==ax3:
        ax.set_ylim(-0.3, 3.00)
        ax.locator_params(axis='y', nbins=5)

    elif ax==ax2 or ax==ax4:
        ax.set_ylim(-0.2, 2.0)
        ax.locator_params(axis='y', nbins=5)
        
    elif ax==ax5:
        ax.set_ylim(-0.2, 2.0)
        ax.locator_params(axis='y', nbins=5)

    elif ax==ax6:
        ax.set_ylim(-0.005, 0.05)
        ax.locator_params(axis='y', nbins=5)
        
    # else:
    #     ax.set_ylim(-0.2, 4.0)
    
    
    
    
# # Annoptations
ax1.add_artist(AnchoredText('(a)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax2.add_artist(AnchoredText('(b)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax3.add_artist(AnchoredText('(c)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax4.add_artist(AnchoredText('(d)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax5.add_artist(AnchoredText('(e)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax6.add_artist(AnchoredText('(f)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
# Adding legend
ax6.legend(fancybox='bow',edgecolor='black', loc='right', 
           bbox_to_anchor=(0.75, 0.75), 
           ncol=1, markerscale=0.7, 
           fontsize=tam-2,
           shadow=True
           )


# Save
plt.savefig('fig-diel-func-tensors.eps', format='eps', dpi=300)
