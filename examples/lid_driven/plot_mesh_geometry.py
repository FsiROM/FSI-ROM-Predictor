"""
Visualization script for the lid-driven cavity FSI problem geometry.
Produces a high-quality, vectorized figure of the fluid and structural meshes,
suitable for a single-column academic paper (A4 format).

Requirements: pyvista, matplotlib, numpy
"""

import pyvista as pv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib.patches import Rectangle, FancyArrowPatch, ConnectionPatch
import matplotlib.patches as mpatches
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
# Single-column width for academic paper (approx 88 mm ~ 3.46 in)
FIG_WIDTH_IN = 3.46
FIG_HEIGHT_IN = 3.6  # Compact single-column height with room for BC annotations
DPI = 600  # High resolution for academic quality

# Use a clean serif font for academic style
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 8,
    'mathtext.fontset': 'cm',
    'axes.linewidth': 0.5,
    'xtick.major.width': 0.4,
    'ytick.major.width': 0.4,
    'xtick.major.size': 2.5,
    'ytick.major.size': 2.5,
})

# Colors (colorblind-friendly academic style)
FLUID_FACE_COLOR = "#DCEEFB"       # Light blue for fluid domain
FLUID_EDGE_COLOR = "#34495E"       # Dark grey-blue edge for fluid mesh
STRUCT_FACE_COLOR = "#F9C390"      # Light coral for structure
STRUCT_EDGE_COLOR = "#8B1A1A"      # Dark red edge for structure mesh
BOUNDARY_COLOR = "#1B2631"         # Domain boundary
INTERFACE_COLOR = "#7D3C98"        # Purple for FSI interface

# --------------------------------------------------------------------------
# Load meshes
# --------------------------------------------------------------------------
fluid = pv.read("vtk_output_lid_fsi_cfd/Parts_Fluid_0_1.vtk")
structure = pv.read("vtk_output_lid_fsi_csd/Structure_0_1.vtk")

# --------------------------------------------------------------------------
# Extract polygon data for matplotlib (vectorized output)
# --------------------------------------------------------------------------

def extract_cells_as_polygons(mesh):
    """Extract cell connectivity and return list of polygon vertex arrays."""
    polygons = []
    points = mesh.points[:, :2]  # 2D (x, y)
    cells = mesh.cells

    offset = 0
    for _ in range(mesh.n_cells):
        n_pts = cells[offset]
        pt_ids = cells[offset + 1: offset + 1 + n_pts]
        polygon = points[pt_ids]
        polygons.append(polygon)
        offset += n_pts + 1

    return polygons, points


fluid_polys, fluid_pts = extract_cells_as_polygons(fluid)
struct_polys, struct_pts = extract_cells_as_polygons(structure)

# --------------------------------------------------------------------------
# Create figure with GridSpec for precise control
# --------------------------------------------------------------------------
fig = plt.figure(figsize=(FIG_WIDTH_IN, FIG_HEIGHT_IN), dpi=DPI)
gs = fig.add_gridspec(
    2, 1,
    height_ratios=[1.0, 0.18],
    hspace=0.35,
    left=0.14, right=0.95, top=0.92, bottom=0.08
)

ax_fluid = fig.add_subplot(gs[0])
ax_struct = fig.add_subplot(gs[1])

# --------------------------------------------------------------------------
# Plot fluid domain
# --------------------------------------------------------------------------
fluid_collection = PolyCollection(
    fluid_polys,
    facecolors=FLUID_FACE_COLOR,
    edgecolors=FLUID_EDGE_COLOR,
    linewidths=0.12,
    alpha=0.95,
)
ax_fluid.add_collection(fluid_collection)
ax_fluid.set_xlim(-0.03, 1.03)
ax_fluid.set_ylim(-0.03, 1.03)
ax_fluid.set_aspect('equal')

# Domain boundary (thick)
rect_fluid = Rectangle((0, 0), 1, 1, linewidth=1.0,
                        edgecolor=BOUNDARY_COLOR, facecolor='none', zorder=5)
ax_fluid.add_patch(rect_fluid)

# FSI interface highlight (bottom edge of fluid)
ax_fluid.plot([0, 1], [0, 0], color=INTERFACE_COLOR, linewidth=1.5,
              zorder=6, linestyle='-')

# Labels
#ax_fluid.set_xlabel(r"$x$ [m]", fontsize=8, labelpad=3)
ax_fluid.set_ylabel(r"$y$ [m]", fontsize=8, labelpad=3)
ax_fluid.tick_params(axis='both', which='major', labelsize=7, pad=2)

# Annotate fluid domain
ax_fluid.text(0.5, 0.52, r"$\Omega_f$", fontsize=13,
              ha='center', va='center', color="#1A5276",
              fontweight='bold', style='italic')

# --- Top wall: u_x = v_bar, u_y = 0 ---
arrow_top = FancyArrowPatch(
    (0.18, 1.015), (0.82, 1.015),
    arrowstyle='->', mutation_scale=8,
    color='#C0392B', linewidth=1.0, clip_on=False, zorder=10
)
ax_fluid.add_patch(arrow_top)
ax_fluid.text(0.5, 1.05, r"$u_x=\bar{v},\; u_y=0$", fontsize=6.5,
              ha='center', va='bottom', color="#C0392B",
              clip_on=False)

# --- Left boundary: bottom 0.875 m no-slip ---
ax_fluid.plot([0, 0], [0, 0.875], color='#566573', linewidth=1.2, zorder=6)
ax_fluid.text(-0.065, 0.5, r"$\mathbf{u}=\mathbf{0}$", fontsize=5.5,
              ha='right', va='center', color="#566573", rotation=90,
              clip_on=False)

# --- Left boundary: top 0.125 m linear inlet profile ---
# Draw velocity profile: vertical baseline + horizontal arrows + diagonal envelope
profile_offset = 0.17  # how far left the baseline sits from x=0
# Vertical baseline (zero-velocity reference line)
ax_fluid.plot([-profile_offset, -profile_offset], [0.875, 1.0],
              color='#2471A3', linewidth=0.7, clip_on=False, zorder=10)
# Diagonal envelope from (baseline, 0.875) to (wall, 1.0)
inlet_y = np.linspace(0.875, 1.0, 30)
inlet_x = -profile_offset + profile_offset * (inlet_y - 0.875) / 0.125
ax_fluid.plot(inlet_x, inlet_y, color='#2471A3', linewidth=0.9,
              clip_on=False, zorder=10)
# Horizontal arrows at several heights
for y_arr in np.linspace(0.875, 1.0, 3)[1:]:  # skip y=0.875 (zero length)
    x_tip = -profile_offset + profile_offset * (y_arr - 0.875) / 0.125
    ax_fluid.annotate('', xy=(x_tip, y_arr), xytext=(-profile_offset, y_arr),
                      arrowprops=dict(arrowstyle='->', color='#2471A3', lw=0.6,
                                      shrinkA=0, shrinkB=0),
                      clip_on=False, zorder=10, annotation_clip=False)
# Tick at zero-velocity point
ax_fluid.plot([-profile_offset - 0.005, -profile_offset + 0.005], [0.875, 0.875],
              color='#2471A3', linewidth=0.6, clip_on=False, zorder=10)
ax_fluid.text(-profile_offset - 0.01, 0.9375, r"$u_y=0$", fontsize=8,
              ha='right', va='center', color="#2471A3",
              clip_on=False)
ax_fluid.text(- 0.05, 1.06, r"$u_x = \bar{v}$", fontsize=8,
              ha='right', va='center', color="#2471A3",
              clip_on=False)

# --- Right boundary: bottom 0.875 m no-slip ---
ax_fluid.plot([1, 1], [0, 0.875], color='#566573', linewidth=1.2, zorder=6)
ax_fluid.text(1.065, 0.4375, r"$\mathbf{u}=\mathbf{0}$", fontsize=5.5,
              ha='left', va='center', color="#566573", rotation=90,
              clip_on=False)

# --- Right boundary: top 0.125 m outlet ---
ax_fluid.plot([1, 1], [0.875, 1.0], color='#D4AC0D', linewidth=1.4, zorder=6)
ax_fluid.text(1.065, 0.9375, r"$p=0$", fontsize=6,
              ha='left', va='center', color="#D4AC0D",
              clip_on=False)

# FSI interface label
ax_fluid.text(0.5, -0.055, r"$\Gamma_\mathrm{fsi}$", fontsize=7.5,
              ha='center', va='top', color=INTERFACE_COLOR,
              clip_on=False, style='italic')

# --------------------------------------------------------------------------
# Plot structure domain (zoomed view)
# --------------------------------------------------------------------------
struct_y_min = structure.bounds[2]  # -0.002
struct_y_max = structure.bounds[3]  # 0.0
struct_thickness = struct_y_max - struct_y_min  # 0.002

struct_collection = PolyCollection(
    struct_polys,
    facecolors=STRUCT_FACE_COLOR,
    edgecolors=STRUCT_EDGE_COLOR,
    linewidths=0.35,
    alpha=0.95,
)
ax_struct.add_collection(struct_collection)

# Set limits with padding
y_pad = struct_thickness * 0.4
ax_struct.set_xlim(-0.03, 1.03)
ax_struct.set_ylim(struct_y_min - y_pad, struct_y_max + y_pad)
ax_struct.set_aspect('auto')

# Domain boundary for structure
rect_struct = Rectangle(
    (0, struct_y_min), 1, struct_thickness,
    linewidth=0.8, edgecolor=BOUNDARY_COLOR, facecolor='none', zorder=5
)
ax_struct.add_patch(rect_struct)

# FSI interface highlight (top edge of structure)
ax_struct.plot([0, 1], [0, 0], color=INTERFACE_COLOR, linewidth=1.5,
              zorder=6, linestyle='-')

# Labels
ax_struct.set_xlabel(r"$x$ [m]", fontsize=8, labelpad=3)
ax_struct.set_ylabel(r"$y$ [m]", fontsize=8, labelpad=3)
ax_struct.tick_params(axis='both', which='major', labelsize=7, pad=2)

# Format y-axis with scientific notation
ax_struct.ticklabel_format(axis='y', style='scientific', scilimits=(-3, -3))
ax_struct.yaxis.get_offset_text().set_fontsize(6)

# Annotate structure domain
ax_struct.text(0.5, (struct_y_min + struct_y_max) / 2, r"$\Omega_s$",
               fontsize=10, ha='center', va='center',
               color="#8B1A1A", fontweight='bold', style='italic')

# Clamped BC annotations on structure (left and right)
ax_struct.plot([0, 0], [struct_y_min, struct_y_max], color='#2C3E50',
              linewidth=2.0, zorder=7)
ax_struct.plot([1, 1], [struct_y_min, struct_y_max], color='#2C3E50',
              linewidth=2.0, zorder=7)
# Hatching to indicate fixed support (small ticks)
for y_tick in np.linspace(struct_y_min, struct_y_max, 5):
    ax_struct.plot([-0.012, 0], [y_tick - struct_thickness*0.15, y_tick + struct_thickness*0.15],
                  color='#2C3E50', linewidth=0.6, clip_on=False, zorder=7)
    ax_struct.plot([1, 1.012], [y_tick - struct_thickness*0.15, y_tick + struct_thickness*0.15],
                  color='#2C3E50', linewidth=0.6, clip_on=False, zorder=7)
ax_struct.text(-0.02, (struct_y_min + struct_y_max) / 2, r"Fixed", fontsize=5,
              ha='right', va='center', color='#2C3E50', clip_on=False)
ax_struct.text(1.02, (struct_y_min + struct_y_max) / 2, r"Fixed", fontsize=5,
              ha='left', va='center', color='#2C3E50', clip_on=False)

# Title for the structure panel indicating zoom
ax_struct.set_title(r"Structure domain", fontsize=7,
                    pad=4, style='italic', color='#555555')

# --------------------------------------------------------------------------
# Add connection lines between panels to indicate zoom
# --------------------------------------------------------------------------
# Draw connector lines from the fluid bottom to the structure panel
con_left = ConnectionPatch(
    xyA=(0, 0), coordsA=ax_fluid.transData,
    xyB=(0, struct_y_max + y_pad), coordsB=ax_struct.transData,
    color='#AAAAAA', linewidth=0.5, linestyle='--'
)
con_right = ConnectionPatch(
    xyA=(1, 0), coordsA=ax_fluid.transData,
    xyB=(1, struct_y_max + y_pad), coordsB=ax_struct.transData,
    color='#AAAAAA', linewidth=0.5, linestyle='--'
)
fig.add_artist(con_left)
fig.add_artist(con_right)

# --------------------------------------------------------------------------
# Add legend
# --------------------------------------------------------------------------
fluid_patch = mpatches.Patch(
    facecolor=FLUID_FACE_COLOR, edgecolor=FLUID_EDGE_COLOR,
    linewidth=0.5, label=r"Fluid ($\Omega_f$)"
)
struct_patch = mpatches.Patch(
    facecolor=STRUCT_FACE_COLOR, edgecolor=STRUCT_EDGE_COLOR,
    linewidth=0.5, label=r"Structure ($\Omega_s$)"
)
interface_line = plt.Line2D(
    [0], [0], color=INTERFACE_COLOR, linewidth=1.2,
    label=r"FSI interface ($\Gamma_\mathrm{fsi}$)"
)
"""
ax_fluid.legend(
    handles=[fluid_patch, struct_patch, interface_line],
    loc='lower right',
    fontsize=6,
    frameon=True,
    framealpha=0.92,
    edgecolor='#BDC3C7',
    handlelength=1.5,
    handletextpad=0.5,
    borderpad=0.4,
)
"""

ax_fluid.spines['top'].set_visible(False)
ax_fluid.spines['right'].set_visible(False)

# --------------------------------------------------------------------------
# Save figures
# --------------------------------------------------------------------------
# Save as vectorized PDF (best for academic papers / LaTeX)
fig.savefig(
    "figs/lid_driven_cavity_mesh_Lid.pdf",
    format='pdf',
    dpi=DPI,
    bbox_inches='tight',
    pad_inches=0.03
)

# Save as SVG for flexibility
fig.savefig(
    "figs/lid_driven_cavity_mesh_Lid.svg",
    format='svg',
    bbox_inches='tight',
    pad_inches=0.03
)

# PNG preview at high resolution
fig.savefig(
    "figs/lid_driven_cavity_mesh_Lid.png",
    format='png',
    dpi=DPI,
    bbox_inches='tight',
    pad_inches=0.03
)

print("Figures saved to figs/lid_driven_cavity_mesh.{pdf,svg,png}")
print(f"  PDF: suitable for LaTeX inclusion (vectorized)")
print(f"  SVG: editable vector format")
print(f"  PNG: preview at {DPI} DPI")
plt.close()
