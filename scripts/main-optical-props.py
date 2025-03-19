
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

## abs, refra,  reflec
# single partical (IPA) vs. exciton (BSE)

# linewidth
gro   = 1.0
grol  = 1.0
mkgro = 1.0
tam=15


fig = plt.figure(figsize=(8, 3))
gs = fig.add_gridspec(1, 3)
fig.subplots_adjust(left=0.08, wspace=0.4, hspace=0.05, right=0.99, top=0.95, bottom=0.18)

# plot 1: x
ax1 = fig.add_subplot(gs[0, 0]) 

# plot 2: y
ax2 = fig.add_subplot(gs[0, 1]) 

# plot 3: z
ax3 = fig.add_subplot(gs[0, 2]) 


for ax in [ax1, ax2, ax3]:
    ax.axvline(x=e1s, color='gray', linestyle=':',
                linewidth=gro,
                zorder=2
               )
    ax.axvline(x=eg, color='gray', linestyle=':',
                linewidth=gro,
                zorder=2
               )


# reducing multiplyer 10^5
multiabs = 0.00001

colorz = 'green' #'black'

# data from ipa_absorption_coef.dat
energy, axx, ayy, azz, axy, axz, ayz = np.loadtxt('out/ipa_absorption_coef.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True).astype(float)


ax1.plot(energy, axx*multiabs, color='blue', #label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# fill below curves
ax1.fill_between(energy, axx*multiabs, 0, color='lightblue', zorder=0)


ax1.plot(energy, ayy*multiabs, color='red', #label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# fill below curves
ax1.plot(energy, azz*multiabs, color=colorz, #label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# data from bse_absorption_coef.dat
energy, axx, ayy, azz, axy, axz, ayz = np.loadtxt('out/bse_absorption_coef.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True).astype(float)

ax1.plot(energy, axx*multiabs, color='blue', #label= r'(BSE)',
             linestyle='dashed', linewidth=grol)

ax1.plot(energy, ayy*multiabs, color='red', #label= r'(BSE)',
             linestyle='dashed', linewidth=grol)

ax1.plot(energy, azz*multiabs, color=colorz, #label= r'(BSE)',
             linestyle='dashed', linewidth=grol)


multi = 1

# data from ipa_refractive_index.dat
energy, axx, ayy, azz, axy, axz, ayz = np.loadtxt('out/ipa_refractive_index.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True).astype(float)

# legend ================================================
ax2.plot(energy, axx*multi, color='blue', label= r'x',
             linestyle='solid', linewidth=grol)
ax2.plot(energy, ayy*multi, color='red', label= r'y',
             linestyle='solid', linewidth=grol)
ax2.plot(energy, azz*multi, color=colorz, label= r'z',
             linestyle='solid', linewidth=grol)
ax2.plot(energy, axx*multi, color='gray', label= r'(IPA)',
             linestyle='solid', linewidth=grol)
# =======================================================

ax2.plot(energy, axx*multi, color='blue',# label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# fill below curves
ax2.fill_between(energy, axx*multi, 0, color='lightblue', zorder=0)

ax2.plot(energy, ayy*multi, color='red',# label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# fill below curves
ax2.plot(energy, azz*multi, color=colorz,# label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# data from bse_refractive_index.dat
energy, axx, ayy, azz, axy, axz, ayz = np.loadtxt('out/bse_refractive_index.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True).astype(float)

# legend ================================================
ax2.plot(energy, axx*multi, color='gray', label= r'(BSE)',
             linestyle='dashed', linewidth=grol)
# =======================================================

ax2.plot(energy, axx*multi, color='blue',# label= r'(BSE)',
             linestyle='dashed', linewidth=grol)

ax2.plot(energy, ayy*multi, color='red',# label= r'(BSE)',
             linestyle='dashed', linewidth=grol)

ax2.plot(energy, azz*multi, color=colorz,# label= r'(BSE)',
             linestyle='dashed', linewidth=grol)





multi = 1

# data from ipa_reflectibility.dat
energy, axx, ayy, azz, axy, axz, ayz = np.loadtxt('out/ipa_reflectibility.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True).astype(float)

ax3.plot(energy, axx*multi, color='blue',# label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# fill below curves
ax3.fill_between(energy, axx*multi, 0, color='lightblue', zorder=0)

ax3.plot(energy, ayy*multi, color='red',# label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# # fill below curves
ax3.plot(energy, azz*multi, color=colorz,# label= r'(IPA)',
             linestyle='solid', linewidth=grol)

# data from bse_reflectibility.dat
energy, axx, ayy, azz, axy, axz, ayz = np.loadtxt('out/bse_reflectibility.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6), unpack=True).astype(float)

ax3.plot(energy, axx*multi, color='blue',# label= r'(BSE)',
             linestyle='dashed', linewidth=grol)

ax3.plot(energy, ayy*multi, color='red',# label= r'(BSE)',
             linestyle='dashed', linewidth=grol)

ax3.plot(energy, azz*multi, color=colorz,# label= r'(BSE)',
             linestyle='dashed', linewidth=grol)


# # Formating the axes
for ax in [ax1, ax2, ax3]:
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
    formatter = ticker.StrMethodFormatter("{x:.1f}")
    ax.yaxis.set_major_formatter(formatter)
    ax.xaxis.set_major_formatter(formatter)
    
    # Set axies lables
    if ax==ax1:
        ax.set_ylabel(r'$\rm\alpha_{i}$ ($10^{5}$ cm$^{-1}$)', fontsize=tam)
        
    if ax==ax2:
        ax.set_ylabel(r'n$\rm _{i}$ (u.a.)', fontsize=tam)
    
    if ax==ax3:
        ax.set_ylabel(r'R$\rm _{i}$ ($\%$)', fontsize=tam)
    
        
    
    ax.set_xticks([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
    ax.set_xlabel('Photon Energy (eV)', fontsize=tam)
        
    ax.set_xlim(1.25, 3.75) 
    
# Annoptations
ax1.add_artist(AnchoredText('(a)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax2.add_artist(AnchoredText('(b)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))
ax3.add_artist(AnchoredText('(c)',prop=dict(size=tam), frameon=False,
                            loc='upper right',pad = 0.1, borderpad = 0.01))


ax2.legend(fancybox='bow',edgecolor='black', loc='upper left', 
           bbox_to_anchor=(0.00, 0.60), 
           ncol=1, 
           markerscale=0.7, 
           fontsize=tam-2,
           labelspacing= 0.2,
           shadow=True
           )

# Save
plt.savefig('fig-main-opt-props.eps', format='eps', dpi=300)

