#!/usr/bin/env python3
"""
Lesion Location Heatmap
=======================

Visualizes brain regions implicated in acquired savant syndrome,
showing the Node modifications that alter Field access.

FNC Interpretation:
- Lesions don't create abilities, they modify Node tuning
- Left hemisphere damage → reduced filtering → broader Field access
- Specific Brodmann areas correlate with specific domain emergence
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from pathlib import Path

# Brodmann area involvement in acquired savant cases
# Data aggregated from Treffert (2009), Miller et al. (1998, 2000)
BRODMANN_DATA = {
    # Area: (involvement_frequency, primary_domain, fnc_interpretation)
    "BA 9/10": (0.45, "Executive", "Reduced top-down filtering"),
    "BA 21/22": (0.72, "Temporal/Language", "Altered auditory processing"),
    "BA 37": (0.38, "Visual/Fusiform", "Enhanced pattern extraction"),
    "BA 39/40": (0.55, "Parietal", "Modified spatial-mathematical"),
    "BA 17/18": (0.25, "Visual Primary", "Raw visual access"),
    "BA 44/45": (0.32, "Broca's", "Language-music interface"),
    "BA 6": (0.28, "Premotor", "Motor-creative coupling"),
    "BA 7": (0.48, "Superior Parietal", "Spatial integration"),
}

# Lateralization data
LATERALIZATION = {
    "Left Hemisphere": 0.78,   # 78% of acquired savants have left-side lesions
    "Right Hemisphere": 0.15,
    "Bilateral": 0.07
}

# Case-specific lesion data
CASE_LESIONS = {
    "Jason Padgett": {
        "type": "Traumatic Brain Injury",
        "location": "Left posterior parietal",
        "brodmann": ["BA 7", "BA 39/40"],
        "domain_emerged": "Mathematical/Geometric"
    },
    "Derek Amato": {
        "type": "Traumatic Brain Injury",
        "location": "Left temporal",
        "brodmann": ["BA 21/22", "BA 44/45"],
        "domain_emerged": "Musical"
    },
    "Orlando Serrell": {
        "type": "Traumatic Brain Injury",
        "location": "Left temporal",
        "brodmann": ["BA 21/22", "BA 37"],
        "domain_emerged": "Calendar/Memory"
    },
    "Alonzo Clemons": {
        "type": "Traumatic Brain Injury",
        "location": "Left frontotemporal",
        "brodmann": ["BA 9/10", "BA 21/22"],
        "domain_emerged": "Sculptural/Mechanical"
    },
    "FTD Cases (Miller)": {
        "type": "Frontotemporal Dementia",
        "location": "Left anterior temporal",
        "brodmann": ["BA 21/22", "BA 38"],
        "domain_emerged": "Visual Art"
    }
}


def create_lesion_heatmap(
    output_path: str = None,
    show_plot: bool = True,
    annotate_fnc: bool = True
) -> plt.Figure:
    """
    Create heatmap showing Brodmann area involvement frequency.
    
    Args:
        output_path: Path to save figure
        show_plot: Whether to display
        annotate_fnc: Add FNC interpretations
        
    Returns:
        matplotlib Figure object
    """
    # Prepare data
    areas = list(BRODMANN_DATA.keys())
    frequencies = [BRODMANN_DATA[a][0] for a in areas]
    domains = [BRODMANN_DATA[a][1] for a in areas]
    fnc_notes = [BRODMANN_DATA[a][2] for a in areas]
    
    # Sort by frequency
    sorted_idx = np.argsort(frequencies)[::-1]
    areas = [areas[i] for i in sorted_idx]
    frequencies = [frequencies[i] for i in sorted_idx]
    domains = [domains[i] for i in sorted_idx]
    fnc_notes = [fnc_notes[i] for i in sorted_idx]
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left plot: Brodmann area heatmap
    colors = ['#f7fbff', '#deebf7', '#c6dbef', '#9ecae1', 
              '#6baed6', '#4292c6', '#2171b5', '#084594']
    cmap = LinearSegmentedColormap.from_list('blues', colors)
    
    # Create horizontal bar chart with heatmap coloring
    bars = ax1.barh(range(len(areas)), frequencies, color=[cmap(f) for f in frequencies])
    ax1.set_yticks(range(len(areas)))
    ax1.set_yticklabels([f"{a}\n({d})" for a, d in zip(areas, domains)], fontsize=10)
    ax1.set_xlabel('Involvement Frequency in Acquired Savant Cases', fontsize=11)
    ax1.set_title('Brodmann Area Involvement\n(Node Modification Sites)', fontsize=13)
    ax1.set_xlim(0, 1)
    
    # Add percentage labels
    for i, (bar, freq) in enumerate(zip(bars, frequencies)):
        ax1.text(freq + 0.02, i, f'{freq*100:.0f}%', va='center', fontsize=9)
    
    # Add FNC annotations if enabled
    if annotate_fnc:
        for i, note in enumerate(fnc_notes):
            ax1.annotate(
                note, 
                xy=(frequencies[i], i),
                xytext=(0.85, i),
                fontsize=7,
                color='#666666',
                style='italic',
                va='center'
            )
    
    # Right plot: Lateralization pie chart
    lat_labels = list(LATERALIZATION.keys())
    lat_values = list(LATERALIZATION.values())
    lat_colors = ['#E94F37', '#4292c6', '#90BE6D']
    
    wedges, texts, autotexts = ax2.pie(
        lat_values, 
        labels=lat_labels,
        autopct='%1.0f%%',
        colors=lat_colors,
        explode=(0.05, 0, 0),
        startangle=90
    )
    ax2.set_title('Lesion Lateralization\n(Left Hemisphere Dominance)', fontsize=13)
    
    # Add FNC interpretation
    ax2.text(0, -1.4, 
             "FNC: Left hemisphere damage reduces\n"
             "analytical filtering, enabling direct Field access",
             ha='center', fontsize=9, style='italic', color='#666666')
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


def create_case_comparison(
    output_path: str = None,
    show_plot: bool = True
) -> plt.Figure:
    """
    Create comparison chart of specific acquired savant cases.
    
    Returns:
        matplotlib Figure object
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    cases = list(CASE_LESIONS.keys())
    y_positions = range(len(cases))
    
    # Create horizontal layout showing case -> lesion -> domain
    for i, (case, data) in enumerate(CASE_LESIONS.items()):
        # Case name
        ax.text(0, i, case, fontsize=11, fontweight='bold', va='center')
        
        # Arrow
        ax.annotate('', xy=(0.35, i), xytext=(0.15, i),
                   arrowprops=dict(arrowstyle='->', color='gray'))
        
        # Lesion info
        ax.text(0.38, i, f"{data['type']}\n{data['location']}", 
               fontsize=9, va='center', color='#E94F37')
        
        # Arrow
        ax.annotate('', xy=(0.7, i), xytext=(0.58, i),
                   arrowprops=dict(arrowstyle='->', color='gray'))
        
        # Domain emerged
        ax.text(0.73, i, data['domain_emerged'], 
               fontsize=10, va='center', color='#2E86AB', fontweight='bold')
        
        # Brodmann areas (small)
        ba_text = ", ".join(data['brodmann'])
        ax.text(0.38, i - 0.25, f"({ba_text})", fontsize=7, va='center', color='gray')
    
    ax.set_xlim(-0.05, 1)
    ax.set_ylim(-0.5, len(cases) - 0.5)
    ax.axis('off')
    
    # Headers
    ax.text(0.07, len(cases), "Case", fontsize=12, fontweight='bold', ha='center')
    ax.text(0.45, len(cases), "Node Modification", fontsize=12, fontweight='bold', ha='center')
    ax.text(0.85, len(cases), "Field Access", fontsize=12, fontweight='bold', ha='center')
    
    ax.set_title('Acquired Savant Cases: From Lesion to Ability\n'
                '(FNC: Node modification → Altered Field tuning → Domain emergence)',
                fontsize=13, pad=20)
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


if __name__ == "__main__":
    print("🧠 Generating Lesion Heatmap...")
    
    output_dir = Path(__file__).parent.parent.parent / "figures"
    output_dir.mkdir(exist_ok=True)
    
    create_lesion_heatmap(
        output_path=str(output_dir / "lesion_heatmap.png"),
        show_plot=False
    )
    
    print("🧠 Generating Case Comparison...")
    create_case_comparison(
        output_path=str(output_dir / "case_lesion_comparison.png"),
        show_plot=False
    )
    
    print("✅ All lesion visualizations complete!")
