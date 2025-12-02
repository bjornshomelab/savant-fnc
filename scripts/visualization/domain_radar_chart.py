#!/usr/bin/env python3
"""
Domain Radar Chart for Savant Abilities
========================================

Visualizes the distribution of savant abilities across domains,
showing how different Field channels manifest in savant populations.

FNC Interpretation:
- Each domain represents a distinct Field information channel
- Radar shape shows the Node's tuning profile
- Asymmetric profiles indicate differential Field access
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import json
from pathlib import Path

# Savant domain data from literature
DOMAIN_DATA = {
    "Music": {
        "prevalence": 0.32,  # 32% of savants
        "field_channel": "Harmonic ratios, temporal patterns",
        "typical_features": ["Perfect pitch", "Instant recall", "Improvisation"]
    },
    "Art": {
        "prevalence": 0.29,
        "field_channel": "Geometric invariants, spatial relations",
        "typical_features": ["Photorealistic detail", "Perspective accuracy", "Color memory"]
    },
    "Calendar": {
        "prevalence": 0.18,
        "field_channel": "Cyclic temporal structures",
        "typical_features": ["Day-date calculation", "Pattern recognition", "Infinite range"]
    },
    "Mathematics": {
        "prevalence": 0.12,
        "field_channel": "Prime relationships, numerical patterns",
        "typical_features": ["Prime detection", "Mental calculation", "Number sense"]
    },
    "Mechanical": {
        "prevalence": 0.06,
        "field_channel": "Spatial-mechanical invariants",
        "typical_features": ["3D visualization", "Assembly intuition", "Engineering sense"]
    },
    "Language": {
        "prevalence": 0.03,
        "field_channel": "Linguistic structure patterns",
        "typical_features": ["Polyglot ability", "Grammar intuition", "Etymology sense"]
    }
}


def create_domain_radar(
    output_path: str = None,
    show_plot: bool = True,
    title: str = "Savant Domain Distribution",
    compare_typical: bool = True
) -> plt.Figure:
    """
    Create radar chart showing savant ability domain distribution.
    
    Args:
        output_path: Path to save figure (PNG/PDF/SVG)
        show_plot: Whether to display the plot
        title: Chart title
        compare_typical: Show typical population baseline
        
    Returns:
        matplotlib Figure object
    """
    # Extract data
    categories = list(DOMAIN_DATA.keys())
    values = [DOMAIN_DATA[cat]["prevalence"] for cat in categories]
    
    # Number of variables
    N = len(categories)
    
    # Compute angle for each category
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Complete the loop
    
    # Add first value to end for closed polygon
    values += values[:1]
    
    # Typical population baseline (near-zero for savant abilities)
    typical_values = [0.001] * N + [0.001]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    
    # Style
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw category labels
    plt.xticks(angles[:-1], categories, size=12, fontweight='bold')
    
    # Draw y-axis labels
    ax.set_rlabel_position(0)
    plt.yticks([0.1, 0.2, 0.3], ["10%", "20%", "30%"], color="grey", size=10)
    plt.ylim(0, 0.40)
    
    # Plot typical population (if enabled)
    if compare_typical:
        ax.plot(angles, typical_values, 'o-', linewidth=1, 
                label='Typical Population', color='gray', alpha=0.5)
        ax.fill(angles, typical_values, alpha=0.1, color='gray')
    
    # Plot savant distribution
    ax.plot(angles, values, 'o-', linewidth=2, 
            label='Savant Population', color='#2E86AB')
    ax.fill(angles, values, alpha=0.25, color='#2E86AB')
    
    # Add Field channel annotations
    for i, (cat, data) in enumerate(DOMAIN_DATA.items()):
        angle = angles[i]
        # Position annotation outside the chart
        ax.annotate(
            f"Field: {data['field_channel'].split(',')[0]}",
            xy=(angle, values[i]),
            xytext=(angle, 0.38),
            fontsize=8,
            ha='center',
            color='#666666',
            style='italic'
        )
    
    # Title and legend
    plt.title(title + "\n(FNC: Differential Field Access)", size=14, y=1.08)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
    
    # Add FNC interpretation note
    fig.text(0.5, 0.02, 
             "Each domain represents a distinct Field information channel.\n"
             "Savant Nodes show enhanced tuning to specific channels.",
             ha='center', fontsize=9, style='italic', color='#666666')
    
    plt.tight_layout()
    
    # Save if path provided
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


def create_individual_profile(
    case_name: str,
    abilities: dict,
    output_path: str = None,
    show_plot: bool = True
) -> plt.Figure:
    """
    Create radar chart for individual savant case.
    
    Args:
        case_name: Name of the savant case
        abilities: Dict mapping domain -> strength (0-1)
        output_path: Path to save figure
        show_plot: Whether to display
        
    Returns:
        matplotlib Figure object
        
    Example:
        create_individual_profile(
            "Jason Padgett",
            {"Mathematics": 0.95, "Art": 0.85, "Music": 0.1, ...}
        )
    """
    categories = list(DOMAIN_DATA.keys())
    N = len(categories)
    
    # Get values, default to 0 if not specified
    values = [abilities.get(cat, 0) for cat in categories]
    values += values[:1]
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, size=11)
    
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75, 1.0], ["25%", "50%", "75%", "100%"], 
               color="grey", size=9)
    plt.ylim(0, 1.0)
    
    # Plot individual profile
    ax.plot(angles, values, 'o-', linewidth=2, color='#E94F37')
    ax.fill(angles, values, alpha=0.3, color='#E94F37')
    
    plt.title(f"{case_name}\nFNC Tuning Profile", size=14, y=1.05)
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


if __name__ == "__main__":
    # Demo: Create population radar
    print("🧬 Generating Savant Domain Radar Chart...")
    
    output_dir = Path(__file__).parent.parent.parent / "figures"
    output_dir.mkdir(exist_ok=True)
    
    create_domain_radar(
        output_path=str(output_dir / "domain_radar_population.png"),
        show_plot=False
    )
    
    # Demo: Create individual profile (Jason Padgett)
    print("🧬 Generating Jason Padgett Profile...")
    create_individual_profile(
        "Jason Padgett",
        {
            "Mathematics": 0.95,
            "Art": 0.90,
            "Music": 0.15,
            "Calendar": 0.10,
            "Mechanical": 0.40,
            "Language": 0.20
        },
        output_path=str(output_dir / "profile_padgett.png"),
        show_plot=False
    )
    
    print("✅ All visualizations complete!")
