import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes, mark_inset
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.transforms import Bbox
from matplotlib import cm

def plotReducedPoints(fig, ax, rawPoints, acceleratedPoints, rawColors, acceleratedColors, cmin, cmax, coords=[0, 1]):
    ax[0].scatter(rawPoints[coords[0], :], rawPoints[coords[1], :], s = 4, c = rawColors,cmap = 'Spectral',
                  vmax = cmax, vmin = cmin);
    c = ax[1].scatter(acceleratedPoints[coords[0], :], acceleratedPoints[coords[1], :], s = 4, c=acceleratedColors,cmap = 'Spectral', 
                      vmax = cmax, vmin = cmin);
    axins = zoomed_inset_axes(ax[1],3.5,loc=1,)
    axins.scatter(acceleratedPoints[coords[0], :], acceleratedPoints[coords[1], :], s = 4, c=acceleratedColors, cmap = 'Spectral',
                  vmax = cmax, vmin = cmin);

    coordsNames = [str(coords[0])+"}$", str(coords[1])+"}$"]
    ax[1].set_ylim(top = 2.0);
    ax[1].set_xlim(right = 5.5);
    ax[0].set_xlabel("$f_{r,"+coordsNames[0], fontsize = 19);
    ax[0].set_ylabel("$f_{r,"+coordsNames[1], fontsize = 19);
    ax[1].set_xlabel("$f_{r,"+coordsNames[0], fontsize = 19);
    ax[0].set_title("$\Tilde{\pmb{f}}$ forces, $\mathcal{F}$ output", fontsize = 19);
    ax[1].set_title("$\pmb{f}$ forces after acceleration", fontsize = 19);
    pp,p1,p2 = mark_inset(ax[1], axins, loc1=2, loc2=4)
    pp.set_fill(False)
    pp.set_edgecolor("k")
    
    ax[0].tick_params(axis='y', which='major', labelsize = 18)
    ax[0].tick_params(axis='x', which='major', labelsize = 14)
    ax[1].tick_params(axis='x', which='major', labelsize = 14)
    fig.tight_layout();
    
    p0 = ax[0].get_position().get_points().flatten()
    p1 = ax[1].get_position().get_points().flatten()
    ax_cbar = fig.add_axes([p0[0], -0.07, p1[2]-p0[0], 0.05])
    cbar = plt.colorbar(c, cax=ax_cbar, orientation='horizontal')
    cbar.ax.tick_params(axis='both', which='major', labelsize = 16);
    cbar.set_label("${f}_{x, |(x=1.2~m,~y=0.2744~m)}$", fontsize = 23);
