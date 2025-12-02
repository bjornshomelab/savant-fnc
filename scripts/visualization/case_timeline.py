#!/usr/bin/env python3
"""
Acquired Savant Case Timeline
=============================

Visualizes the temporal progression from injury to ability emergence,
showing the Node reconfiguration process.

FNC Interpretation:
- Injury creates sudden Node disruption
- Ability emergence shows Field access reconfiguration
- Timeline reveals tuning stabilization period
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import numpy as np
from datetime import datetime
from pathlib import Path

# Acquired savant case timeline data
CASE_TIMELINES = {
    "Jason Padgett": {
        "injury_date": "2002-09-13",
        "injury_type": "Assault (TBI)",
        "ability_onset": "Immediate",
        "ability_stabilized": "Weeks",
        "domain": "Mathematical/Geometric",
        "key_events": [
            ("2002-09", "Assault outside karaoke bar"),
            ("2002-09", "Immediate geometric visions"),
            ("2002-10", "Begins drawing fractals"),
            ("2003", "Enrolls in mathematics"),
            ("2014", "Published memoir")
        ],
        "fnc_note": "Instant Node reconfiguration"
    },
    "Derek Amato": {
        "injury_date": "2006-10",
        "injury_type": "Diving accident (TBI)",
        "ability_onset": "3 days",
        "ability_stabilized": "Weeks",
        "domain": "Musical",
        "key_events": [
            ("2006-10", "Diving accident, concussion"),
            ("2006-10", "First piano attempt (3 days post)"),
            ("2006-11", "Plays for hours continuously"),
            ("2007", "Performs publicly"),
            ("2013", "Featured in documentaries")
        ],
        "fnc_note": "Delayed onset = Node stabilization"
    },
    "Orlando Serrell": {
        "injury_date": "1979-08-17",
        "injury_type": "Baseball impact (TBI)",
        "ability_onset": "Gradual",
        "ability_stabilized": "Months",
        "domain": "Calendar/Autobiographical",
        "key_events": [
            ("1979-08", "Hit by baseball, age 10"),
            ("1979-09", "Headaches subside"),
            ("1979-12", "Notices date-recall ability"),
            ("1980s", "Ability becomes consistent"),
            ("2000s", "Media recognition")
        ],
        "fnc_note": "Gradual Field channel opening"
    },
    "Tony Cicoria": {
        "injury_date": "1994",
        "injury_type": "Lightning strike",
        "ability_onset": "Weeks",
        "ability_stabilized": "Months",
        "domain": "Musical composition",
        "key_events": [
            ("1994", "Struck by lightning"),
            ("1994", "Near-death experience"),
            ("1994", "Obsession with piano begins"),
            ("1995", "Composes 'Lightning Sonata'"),
            ("2007", "Featured in Sacks' 'Musicophilia'")
        ],
        "fnc_note": "NDE + Node reset"
    }
}


def create_case_timeline(
    case_name: str = None,
    output_path: str = None,
    show_plot: bool = True
) -> plt.Figure:
    """
    Create timeline visualization for acquired savant case(s).
    
    Args:
        case_name: Specific case to plot, or None for all
        output_path: Path to save figure
        show_plot: Whether to display
        
    Returns:
        matplotlib Figure object
    """
    if case_name:
        cases = {case_name: CASE_TIMELINES[case_name]}
    else:
        cases = CASE_TIMELINES
    
    n_cases = len(cases)
    fig, axes = plt.subplots(n_cases, 1, figsize=(14, 3 * n_cases))
    
    if n_cases == 1:
        axes = [axes]
    
    colors = {
        "injury": "#E94F37",
        "onset": "#F4A261", 
        "stabilized": "#2A9D8F",
        "event": "#264653"
    }
    
    for ax, (name, data) in zip(axes, cases.items()):
        events = data["key_events"]
        
        # Create timeline
        ax.set_xlim(-0.5, len(events) + 0.5)
        ax.set_ylim(-0.5, 1.5)
        
        # Draw horizontal line
        ax.axhline(y=0.5, color='gray', linestyle='-', linewidth=2, alpha=0.5)
        
        # Plot events
        for i, (date, description) in enumerate(events):
            # Determine color based on event type
            if i == 0:
                color = colors["injury"]
                marker = 'X'
                size = 200
            elif "first" in description.lower() or "immediate" in description.lower():
                color = colors["onset"]
                marker = 'o'
                size = 150
            else:
                color = colors["event"]
                marker = 'o'
                size = 100
            
            ax.scatter(i, 0.5, c=color, s=size, marker=marker, zorder=5)
            
            # Alternate labels above/below
            y_offset = 0.9 if i % 2 == 0 else 0.1
            va = 'bottom' if i % 2 == 0 else 'top'
            
            ax.annotate(
                f"{date}\n{description}",
                xy=(i, 0.5),
                xytext=(i, y_offset),
                ha='center',
                va=va,
                fontsize=8,
                arrowprops=dict(arrowstyle='-', color='gray', alpha=0.5)
            )
        
        # Title with FNC interpretation
        ax.set_title(
            f"{name} — {data['domain']}\n"
            f"Onset: {data['ability_onset']} | FNC: {data['fnc_note']}",
            fontsize=11,
            fontweight='bold'
        )
        
        ax.axis('off')
    
    # Add legend
    legend_elements = [
        Line2D([0], [0], marker='X', color='w', markerfacecolor=colors["injury"], 
               markersize=12, label='Injury Event'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=colors["onset"], 
               markersize=10, label='Ability Onset'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor=colors["event"], 
               markersize=8, label='Subsequent Event'),
    ]
    fig.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.98, 0.98))
    
    fig.suptitle(
        'Acquired Savant Timelines: From Injury to Ability\n'
        '(FNC: Node disruption → Field reconfiguration → New tuning)',
        fontsize=13,
        y=1.02
    )
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


def create_onset_comparison(
    output_path: str = None,
    show_plot: bool = True
) -> plt.Figure:
    """
    Compare ability onset times across cases.
    
    Returns:
        matplotlib Figure object
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Categorize onset times
    onset_categories = {
        "Immediate": [],
        "Days": [],
        "Weeks": [],
        "Months": []
    }
    
    for name, data in CASE_TIMELINES.items():
        onset = data["ability_onset"]
        if "immediate" in onset.lower():
            onset_categories["Immediate"].append(name)
        elif "day" in onset.lower():
            onset_categories["Days"].append(name)
        elif "week" in onset.lower():
            onset_categories["Weeks"].append(name)
        else:
            onset_categories["Months"].append(name)
    
    # Create bar chart
    categories = list(onset_categories.keys())
    counts = [len(onset_categories[c]) for c in categories]
    colors = ['#E94F37', '#F4A261', '#E9C46A', '#2A9D8F']
    
    bars = ax.bar(categories, counts, color=colors)
    
    # Add case names on bars
    for bar, cat in zip(bars, categories):
        cases = onset_categories[cat]
        if cases:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.05,
                   '\n'.join(cases), ha='center', va='bottom', fontsize=8)
    
    ax.set_ylabel('Number of Cases')
    ax.set_xlabel('Time to Ability Onset')
    ax.set_title('Acquired Savant: Onset Time Distribution\n'
                '(FNC: Faster onset = More dramatic Node reconfiguration)')
    
    # Add interpretation
    ax.text(0.98, 0.02, 
            "FNC Interpretation:\n"
            "• Immediate: Catastrophic filter removal\n"
            "• Days/Weeks: Gradual Node stabilization\n"
            "• Months: Slow Field channel opening",
            transform=ax.transAxes, fontsize=8, va='bottom', ha='right',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"✅ Saved: {output_path}")
    
    if show_plot:
        plt.show()
    
    return fig


if __name__ == "__main__":
    print("📅 Generating Case Timelines...")
    
    output_dir = Path(__file__).parent.parent.parent / "figures"
    output_dir.mkdir(exist_ok=True)
    
    create_case_timeline(
        output_path=str(output_dir / "case_timelines_all.png"),
        show_plot=False
    )
    
    print("📅 Generating Onset Comparison...")
    create_onset_comparison(
        output_path=str(output_dir / "onset_comparison.png"),
        show_plot=False
    )
    
    print("✅ All timeline visualizations complete!")
