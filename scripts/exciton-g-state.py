
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

def G2greek(klabels):
    klabels_greek = klabels
    # change capital letters to greek: G -> \Gamma
    for i in range(len(klabels)):
        if klabels_greek[i] == 'G':
            klabels_greek[i] = r'$\Gamma$'
    
    return klabels_greek

# loading the font style
plt.rcParams['text.usetex'] = True
fonte = {'family': 'serif', 'serif': ['Liberation Serif']}
# fonte = {'family':'sans-serif','sans-serif':['Helvetica']}
plt.rc('font', **fonte)

# figure formating, shape, etc.
fig = plt.figure(figsize=(4, 4))

fig.subplots_adjust(left=0.175, 
                    wspace=0.3, 
                    hspace=0.08, 
                    right=0.97, 
                    top=0.98, 
                    bottom=0.08)

gs = fig.add_gridspec(1, 1)

# plot 2: x
ax2 = fig.add_subplot(gs[0, 0]) 

# line, spine and markers width
gro = 1 #0.25
groaux = -0.25

# format text size
tam=15

stylbnd = '-'
stylexc = '--'

# Plot BANDS
# n=1

# Plot k-label as hight- symmetry k-points
kpoints = np.loadtxt('out/KLABELS-BSE.dat', usecols=0).astype(float)


# set number of kpoints in the path
file_path = 'out/log_bse_kpath.dat'
search_strings = 'kpoint'
desireble_column = 6
found_line = py_grep(file_path, search_strings)
divsbse = int(found_line[desireble_column]) 

# Store k-label labels from WTB input file 'kpoints.dat' ('kpoints-bse.dat' also valid)
with open('kpoints.dat', 'r') as f:
  data = f.readlines()[3:]
  
# Split each row into a list of elements
rows = [row.split() for row in data]

# Extract the last element from each row (assuming consistent delimiters)
klabels = [row[-1] for row in rows]

# delet repetitive labels
for l in range(len(klabels)-1, 1, -1):
    
    if (l % 2) == 0:
        # print(klabels[l])
        del klabels[l]

# k-path
kpath_wtb = np.loadtxt('out/bands_bse.dat', 
                      # skiprows=2, 
                      # max_rows=40,
                      usecols=0).astype(float)


#get band data
data_wtb = np.loadtxt('out/bands_bse.dat',
                  usecols=1).astype(float)

# Plot parameters
lgro = 0 #-0.90
a1 = -0.5 #1.25
a2 = -0.75
a3 = 1.25
div = 40 # get this from log_bse file

# selecting the number of bands to plot
nb = 7800
nr = 7200

for k in range(nb-nr,-1,-1):

    inicial = k*div
    final = (1+k)*div
    
    ax2.plot(kpath_wtb[inicial:final],
            data_wtb[inicial:final],
            color='red',
            linestyle=stylexc, 
            # marker='+', markersize=3, markeredgewidth=gro,
            # markerfacecolor='white', #'none',
            linewidth=gro+a2,
            zorder=1
            )
    
# plot an arrow
ax2.annotate(text=r'E$\rm_{gs}$', 
             color='black',
             fontsize=tam,
             xy=(kpoints[2],1.86), 
             xytext=(kpoints[2]-0.25,1.84), 
             arrowprops=dict(
                 # facecolor = 'blue', # for not fancy arrow head '->'
                 edgecolor = 'black',
                 arrowstyle='-|>',
                 facecolor='black'
             ),
             )


# Customize the plot
ax2.set_ylim(1.8, 2.6)


for ax in [ax2]:
    # Formating the axes width
    for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(gro)
        
    # format ticklables
    ax.tick_params(axis='both', which='both', direction='in', labelsize=tam)
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.tick_params(which='major',length=5,width=gro)
    ax.tick_params(which='minor',length=3,width=gro)
    ax.locator_params(axis='y', nbins=7)
    
    # Adding point and comma after the major ticks in the y axis
    formatter = ticker.StrMethodFormatter("{x:.1f}")
    ax.yaxis.set_major_formatter(formatter)
        
    # Offsetting the major thicks from the axes
    for tick in ax.xaxis.get_major_ticks():
        tick.set_pad(10)
    for tick in ax.yaxis.get_major_ticks():
        tick.set_pad(10)

    if ax==ax2:
        ax.set_xticks(kpoints)
        ax.set_xticklabels(G2greek(klabels))
                
    else:
        ax.set_xticks(kpoints,[])

    ax.set_xlim(kpoints[0], kpoints[-1])
    ax.set_ylabel('Energy (eV)', fontsize=tam,labelpad=5)

    
    # plot vertical line
    for l in range(len(klabels)):
        ax.axvline(x=kpoints[l], color='black', linestyle='-', linewidth=gro, zorder=3)


# Save
plt.savefig('fig-exc-g-st.eps', format='eps', dpi=100)
