import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

scaling_factor = 50
r0 = 1 / np.sqrt(np.pi)


def plotTube(ax, crossSection, velocity, pressure, dx, t, quantMin, quantMax, stressMin, stressMax):

    radius0 = np.sqrt(crossSection / np.pi)
    stress = pressure * radius0
    N = velocity.shape[0]

    ax.plot(np.arange(N) * dx, r0 + (radius0 - r0) * scaling_factor, 'k')
    ax.plot(np.arange(N) * dx, (r0 + (radius0 - r0) * scaling_factor)+(0.16*r0), 'k')

    ax.plot(np.arange(N) * dx, -(r0 + (radius0 - r0) * scaling_factor), 'k')
    ax.plot(np.arange(N) * dx, -(r0 + (radius0 - r0) * scaling_factor)-(0.16*r0), 'k')

    iii = 0
    rects0 = []
    map0 = plt.get_cmap('viridis')
    for x in np.arange(N) * dx:
        dy = 0.16*(r0)
        rect1 = Rectangle((x - .5 * dx, r0 + (radius0[iii] - r0) * scaling_factor), dx, dy,
                         color=map0((stress[iii]-stressMin)/(stressMax-stressMin)))
        rect2 = Rectangle((x - .5 * dx, -(r0 + (radius0[iii] - r0) * scaling_factor)-.16*r0 ), dx, dy,
                         color=map0((stress[iii]-stressMin)/(stressMax-stressMin)))
        ax.add_patch(rect1)
        ax.add_patch(rect2)
        iii += 1
        rects0.append(rect1)
        rects0.append(rect2)

    iii = 0
    rects = []
    map = plt.get_cmap('RdYlBu')
    for x in np.arange(N) * dx:
        dy = (r0 + (radius0[iii] - r0) * scaling_factor)
        rect = Rectangle((x - .5 * dx, -dy), dx, 2 * dy,
                         color=map((velocity[iii]-quantMin)/(quantMax-quantMin)))
        ax.add_patch(rect)
        iii += 1
        rects.append(rect)

    ax.set_ylim([-2, 2])

    return map0((stress-stressMin)/(stressMax-stressMin))


def plotVar(ax, crossSection, dx, t):
    radius0 = np.sqrt(crossSection / np.pi)
    radius_mean = np.mean(np.sqrt(crossSection / np.pi))
    N = crossSection.shape[0]
    plt.plot(np.arange(N) * dx, (radius_mean - radius0) * scaling_factor)
    lim = np.max(np.abs(radius0 - radius_mean))
    borders = 10**0
    ax.set_ylim([-borders, +borders])


def doPlotting(ax, crossSection0, velocity0, pressure0, dx, t, quantMin, quantMax, stressMin, stressMax):
    cmaps = plotTube(ax, crossSection0, velocity0,
             pressure0, dx, t, quantMin, quantMax, stressMin, stressMax)
    ax.set_title("t = {:.1f}".format(t))
    plt.pause(0.1)
    # ax[1].cla()

    return cmaps
