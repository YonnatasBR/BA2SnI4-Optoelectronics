
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.offsetbox import AnchoredText

# loading the font style
plt.rcParams['text.usetex'] = True
fonte = {'family': 'serif', 'serif': ['Liberation Serif']}
# fonte = {'family':'sans-serif','sans-serif':['Helvetica']}
plt.rc('font', **fonte)

fig = plt.figure(figsize=(4, 4))

fig.subplots_adjust(left=0.18, 
                    wspace=0.3, 
                    hspace=0.1, #0.05, 
                    right=0.96, 
                    top=0.98, 
                    bottom=0.15)

gs = fig.add_gridspec(1, 1)

# plot 1: sum
ax1 = fig.add_subplot(gs[0, 0]) 

# linewidth
gro = 1 #0.25
grol  = 1.0

tam=15


# thickness,pce,jmax,j0,jsc,vmax,voc,ff
thic,pce_ipa,jmax,j0,jsc,vmax,voc,ff = np.loadtxt('out/SLME-ipa.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6, 7), unpack=True).astype(float)


ax1.plot(thic, pce_ipa, color='blue', label= r'IPA',
             linestyle='-', linewidth=grol+1)

# thickness,pce,jmax,j0,jsc,vmax,voc,ff
thic,pce_bse,jmax,j0,jsc,vmax,voc,ff = np.loadtxt('out/SLME-bse.dat', 
                                    usecols=(0, 1, 2, 3, 4, 5, 6, 7), unpack=True).astype(float)


ax1.plot(thic, pce_bse, color='red', label= r'BSE',
             linestyle='--', linewidth=grol)


# fill below curves
ax1.fill_between(thic, pce_ipa, 0, color='lightblue', zorder=0)


# Customize the plot
ax1.set_ylim(0, 30)
ax1.set_xlim(-0.125, 1.0)

for ax in [ax1]:
    # Formating the axes width
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(gro)
        
    # format ticklables
    ax.tick_params(axis='both', which='both', direction='in', labelsize=tam)
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(4))
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.tick_params(which='major',length=5,width=gro)
    ax.tick_params(which='minor',length=3,width=gro)
    ax.locator_params(axis='y', nbins=5)
    
    # Adding point and comma after the major ticks in the y axis
    formatter = ticker.StrMethodFormatter("{x:.1f}")
    ax.yaxis.set_major_formatter(formatter)
        
    # Offsetting the major thicks from the axes
    for tick in ax.xaxis.get_major_ticks():
        tick.set_pad(10)
    for tick in ax.yaxis.get_major_ticks():
        tick.set_pad(10)

    # ax.set_xlim(kpoints[0], kpoints[-1])
    ax1.set_ylabel(r'PCE (\%)', fontsize=tam,labelpad=0)
    ax1.set_xlabel(r'Thickness ($\rm\times10^{-6} m$)', fontsize=tam,labelpad=0)
    
    # Adding legend
    ax.legend(fancybox='bow',edgecolor='black', loc='center', 
           bbox_to_anchor=(0.5, 0.5), 
           ncol=1, markerscale=0.7, 
           fontsize=tam-2,
           )

# Save
plt.savefig('fig-pce-slme.eps', format='eps', dpi=300)

