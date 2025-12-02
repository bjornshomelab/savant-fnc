#!/usr/bin/env python3
"""
FNC Tuning Diagram
==================

Visualizes the difference between typical and savant Node tuning,
showing how different configurations access different Field regions.

FNC Interpretation:
- Typical Node: Broad, filtered access (survival-focused)
- Savant Node: Narrow, unfiltered access (domain-focused)
- The Field contains the same information — only access differs
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch
from matplotlib.patches import ConnectionPatch
import matplotlib.patheffects as path_effects
from pathlib import Path


def create_tuning_comparison(
    output_path: str = None,
    show_plot: bool = True
) -> plt.Figure:
    """
    Create side-by-side comparison of typical vs savant Node tuning.
    
    Returns:
        matplotlib Figure object
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    
    # Colors
    field_color = '#E3F2FD'
    node_typical = '#90BE6D'
    node_savant = '#E94F37'
    cockpit_color = '#FFE66D'
    arrow_color = '#264653'
    
    # === LEFT PANEL: TYPICAL TUNING ===
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Typical Node Tuning', fontsize=14, fontweight='bold', pad=20)
    
    # Field (top) - large semicircle with many channels
    field1 = plt.Circle((5, 9), 2, color=field_color, ec='#1976D2', linewidth=2)
    ax1.add_patch(field1)
    ax1.text(5, 9, '🌐 FIELD', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Field channels (narrow lines coming down)
    channels_x = [3, 4, 5, 6, 7]
    channel_labels = ['♪', '📐', '📅', '🔢', '🔧']
    for i, (x, label) in enumerate(zip(channels_x, channel_labels)):
        # Thin lines from Field
        ax1.plot([x, x], [7, 5.5], color='#1976D2', linewidth=1, alpha=0.5)
        ax1.text(x, 7.2, label, ha='center', fontsize=10)
    
    # Node (middle) - filters most channels
    node1 = FancyBboxPatch((3.5, 4), 3, 1.5, boxstyle="round,pad=0.1",
                           facecolor=node_typical, edgecolor='#2D6A4F', linewidth=2)
    ax1.add_patch(node1)
    ax1.text(5, 4.75, '🧠 NODE\n(Broad Filter)', ha='center', va='center', fontsize=10)
    
    # Filter visualization - most channels blocked
    for i, x in enumerate(channels_x):
        if x == 5:  # Only center channel passes through
            ax1.plot([x, x], [4, 2.5], color='#2D6A4F', linewidth=2, alpha=0.8)
        else:
            ax1.plot([x, x], [5.5, 5], color='red', linewidth=1, alpha=0.3)
            ax1.scatter([x], [5], marker='x', color='red', s=50, alpha=0.5)
    
    # Cockpit (bottom)
    cockpit1 = FancyBboxPatch((3.5, 1), 3, 1.5, boxstyle="round,pad=0.1",
                              facecolor=cockpit_color, edgecolor='#F4A261', linewidth=2)
    ax1.add_patch(cockpit1)
    ax1.text(5, 1.75, '👁️ COCKPIT\n(Normal Experience)', ha='center', va='center', fontsize=10)
    
    # Annotation
    ax1.text(5, 0.2, 
             'Broad filtering for survival\nBalanced but limited access',
             ha='center', fontsize=9, style='italic', color='#666')
    
    # === RIGHT PANEL: SAVANT TUNING ===
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Savant Node Tuning', fontsize=14, fontweight='bold', pad=20)
    
    # Field (top) - same as typical
    field2 = plt.Circle((5, 9), 2, color=field_color, ec='#1976D2', linewidth=2)
    ax2.add_patch(field2)
    ax2.text(5, 9, '🌐 FIELD', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Field channels
    for i, (x, label) in enumerate(zip(channels_x, channel_labels)):
        ax2.plot([x, x], [7, 5.5], color='#1976D2', linewidth=1, alpha=0.5)
        ax2.text(x, 7.2, label, ha='center', fontsize=10)
    
    # Node (middle) - different filter configuration
    node2 = FancyBboxPatch((3.5, 4), 3, 1.5, boxstyle="round,pad=0.1",
                           facecolor=node_savant, edgecolor='#9B2335', linewidth=2)
    ax2.add_patch(node2)
    ax2.text(5, 4.75, '🧠 NODE\n(Narrow Focus)', ha='center', va='center', fontsize=10)
    
    # Filter visualization - one channel WIDE open, others blocked
    for i, x in enumerate(channels_x):
        if x == 4:  # Music channel wide open (example)
            ax2.plot([x, x], [5.5, 2.5], color='#9B2335', linewidth=4, alpha=0.9)
            ax2.annotate('', xy=(x, 2.5), xytext=(x, 5.5),
                        arrowprops=dict(arrowstyle='->', color='#9B2335', lw=3))
        else:
            ax2.plot([x, x], [5.5, 5], color='red', linewidth=1, alpha=0.3)
            ax2.scatter([x], [5], marker='x', color='red', s=50, alpha=0.5)
    
    # Cockpit (bottom) - enhanced for one domain
    cockpit2 = FancyBboxPatch((3.5, 1), 3, 1.5, boxstyle="round,pad=0.1",
                              facecolor='#FFD93D', edgecolor='#FF6B35', linewidth=3)
    ax2.add_patch(cockpit2)
    ax2.text(5, 1.75, '👁️ COCKPIT\n(Enhanced Domain)', ha='center', va='center', 
             fontsize=10, fontweight='bold')
    
    # Annotation
    ax2.text(5, 0.2, 
             'Narrow but deep Field access\nExtraordinary in specific domain',
             ha='center', fontsize=9, style='italic', color='#666')
    
    # Add connecting annotation between panels
    fig.text(0.5, 0.02, 
             'FNC: Same Field, different Node tuning → Different Cockpit experience\n'
             'Savant abilities emerge from alternative tuning, not deficit or compensation',
             ha='center', fontsize=11, style='italic',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


def create_tuning_spectrum(
    output_path: str = None,
    show_plot: bool = True
) -> plt.Figure:
    """
    Create spectrum showing range of tuning configurations.
    
    Returns:
        matplotlib Figure object
    """
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # X-axis: Tuning breadth (narrow to broad)
    # Y-axis: Field access depth
    
    # Define tuning profiles
    profiles = {
        "Typical": {"breadth": 0.7, "depth": 0.4, "color": "#90BE6D"},
        "Autism (non-savant)": {"breadth": 0.4, "depth": 0.5, "color": "#4ECDC4"},
        "Autistic Savant": {"breadth": 0.25, "depth": 0.85, "color": "#E94F37"},
        "Acquired Savant": {"breadth": 0.2, "depth": 0.9, "color": "#9B2335"},
        "Prodigious Savant": {"breadth": 0.15, "depth": 0.95, "color": "#6A0572"},
    }
    
    for name, data in profiles.items():
        ax.scatter(data["breadth"], data["depth"], 
                  s=500, c=data["color"], alpha=0.7, edgecolors='black', linewidth=2)
        ax.annotate(name, (data["breadth"], data["depth"]), 
                   textcoords="offset points", xytext=(10, 10),
                   fontsize=10, fontweight='bold')
    
    # Add arrows showing FNC interpretation
    ax.annotate('', xy=(0.15, 0.95), xytext=(0.7, 0.4),
               arrowprops=dict(arrowstyle='->', color='gray', lw=2, 
                              connectionstyle="arc3,rad=-0.2"))
    ax.text(0.45, 0.55, 'Increasing\nField Depth', fontsize=9, 
           rotation=-30, color='gray', style='italic')
    
    ax.set_xlabel('Tuning Breadth (Narrow ← → Broad)', fontsize=12)
    ax.set_ylabel('Field Access Depth', fontsize=12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('FNC Tuning Spectrum\n(Trade-off between breadth and depth of Field access)',
                fontsize=13)
    
    # Add interpretation box
    textstr = ('FNC Prediction:\n'
               '• Narrower tuning → Deeper access\n'
               '• Broader tuning → Shallower access\n'
               '• Savants sacrifice breadth for depth')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    ax.text(0.95, 0.05, textstr, transform=ax.transAxes, fontsize=9,
           verticalalignment='bottom', horizontalalignment='right', bbox=props)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


if __name__ == "__main__":
    print("🎛️ Generating FNC Tuning Diagrams...")
    
    output_dir = Path(__file__).parent.parent.parent / "figures"
    output_dir.mkdir(exist_ok=True)
    
    create_tuning_comparison(
        output_path=str(output_dir / "fnc_tuning_comparison.png"),
        show_plot=False
    )
    
    print("🎛️ Generating Tuning Spectrum...")
    create_tuning_spectrum(
        output_path=str(output_dir / "fnc_tuning_spectrum.png"),
        show_plot=False
    )
    
    print("✅ All FNC tuning visualizations complete!")
