#!/usr/bin/env python3
"""
Savant-FNC Main Analysis Runner
===============================

Master script to run all analyses and generate comprehensive report.

Usage:
    python run_analysis.py --all           # Run everything
    python run_analysis.py --viz           # Visualizations only
    python run_analysis.py --stats         # Statistics only
    python run_analysis.py --genetics      # Genetic analysis only
    python run_analysis.py --report        # Generate full report
"""

import argparse
import sys
import json
from pathlib import Path
from datetime import datetime

# Add scripts to path
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))


def run_visualizations(output_dir: Path):
    """Generate all visualizations."""
    print("\n" + "=" * 60)
    print("📊 GENERATING VISUALIZATIONS")
    print("=" * 60)
    
    output_dir.mkdir(exist_ok=True)
    
    from visualization.domain_radar_chart import create_domain_radar, create_individual_profile
    from visualization.lesion_heatmap import create_lesion_heatmap, create_case_comparison
    from visualization.case_timeline import create_case_timeline, create_onset_comparison
    from visualization.fnc_tuning_diagram import create_tuning_comparison, create_tuning_spectrum
    
    # Domain radar
    print("\n→ Creating domain radar chart...")
    create_domain_radar(
        output_path=str(output_dir / "domain_radar_population.png"),
        show_plot=False
    )
    
    # Individual profile (Padgett)
    print("→ Creating Jason Padgett profile...")
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
    
    # Lesion heatmap
    print("→ Creating lesion heatmap...")
    create_lesion_heatmap(
        output_path=str(output_dir / "lesion_heatmap.png"),
        show_plot=False
    )
    
    # Case comparison
    print("→ Creating case comparison...")
    create_case_comparison(
        output_path=str(output_dir / "case_lesion_comparison.png"),
        show_plot=False
    )
    
    # Case timelines
    print("→ Creating case timelines...")
    create_case_timeline(
        output_path=str(output_dir / "case_timelines_all.png"),
        show_plot=False
    )
    
    # Onset comparison
    print("→ Creating onset comparison...")
    create_onset_comparison(
        output_path=str(output_dir / "onset_comparison.png"),
        show_plot=False
    )
    
    # FNC tuning diagrams
    print("→ Creating FNC tuning comparison...")
    create_tuning_comparison(
        output_path=str(output_dir / "fnc_tuning_comparison.png"),
        show_plot=False
    )
    
    print("→ Creating tuning spectrum...")
    create_tuning_spectrum(
        output_path=str(output_dir / "fnc_tuning_spectrum.png"),
        show_plot=False
    )
    
    print(f"\n✅ All visualizations saved to: {output_dir}")


def run_statistics():
    """Run all statistical analyses."""
    print("\n" + "=" * 60)
    print("📈 RUNNING STATISTICAL ANALYSES")
    print("=" * 60)
    
    from statistics.prevalence_analysis import run_all_analyses
    from statistics.effect_sizes import calculate_all_effects
    
    print("\n→ Running prevalence analyses...")
    prevalence_results = run_all_analyses()
    
    print("\n→ Running effect size analyses...")
    effect_results = calculate_all_effects()
    
    return {
        "prevalence": prevalence_results,
        "effects": effect_results
    }


def run_genetic_analysis():
    """Run genetic analysis pipeline."""
    print("\n" + "=" * 60)
    print("🧬 RUNNING GENETIC ANALYSES")
    print("=" * 60)
    
    from genetic_analysis.pathway_enrichment import (
        run_pathway_enrichment,
        fnc_pathway_interpretation,
        analyze_mni_dataset_predictions
    )
    from genetic_analysis.fnc_gene_scoring import calculate_fnc_scores
    
    # Demo gene list
    demo_genes = ["CACNA1C", "SHANK3", "GABRA1", "SCN2A", "CNTNAP2", "MBP", "GRIN2B"]
    
    print(f"\n→ Running pathway enrichment on {len(demo_genes)} genes...")
    enrichment = run_pathway_enrichment(demo_genes)
    
    if enrichment:
        print("→ Generating FNC interpretation...")
        interpretation = fnc_pathway_interpretation(enrichment)
    else:
        interpretation = {"summary": ["No enriched pathways found"]}
    
    print("→ Generating MNI dataset protocol...")
    mni_protocol = analyze_mni_dataset_predictions()
    
    # Demo FNC scoring
    print("→ Calculating demo FNC tuning scores...")
    demo_variants = [
        {"gene": "CACNA1C", "impact": "high"},
        {"gene": "SHANK3", "impact": "moderate"},
        {"gene": "GABRA1", "impact": "moderate"},
    ]
    fnc_scores = calculate_fnc_scores(demo_variants)
    
    return {
        "enrichment": {name: {
            "genes": result.genes_found,
            "p_value": result.p_value,
            "fold_enrichment": result.fold_enrichment
        } for name, result in enrichment.items()},
        "interpretation": interpretation,
        "mni_protocol": mni_protocol,
        "demo_fnc_scores": {
            "frequency": fnc_scores.frequency_score,
            "filtering": fnc_scores.filtering_score,
            "integration": fnc_scores.integration_score,
            "bandwidth": fnc_scores.bandwidth_score,
            "predicted_domain": fnc_scores.predicted_domain
        }
    }


def generate_report(stats_results, genetic_results, output_path: Path):
    """Generate comprehensive markdown report."""
    print("\n" + "=" * 60)
    print("📝 GENERATING COMPREHENSIVE REPORT")
    print("=" * 60)
    
    report = f"""# Savant-FNC Analysis Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Version:** 1.0.0  
**DOI:** [10.5281/zenodo.17789741](https://doi.org/10.5281/zenodo.17789741)

---

## Executive Summary

This report presents automated analyses from the Savant-FNC research project,
applying the Field-Node-Cockpit (FNC) framework to savant syndrome data.

---

## 1. Statistical Analyses

### 1.1 Autism-Savant Association

{json.dumps(stats_results['prevalence']['autism_savant_association'], indent=2, default=str)}

### 1.2 Domain Specificity

{json.dumps(stats_results['prevalence']['domain_specificity'], indent=2, default=str)}

### 1.3 TMS Effect Sizes

**Meta-Analysis:**
- Weighted mean d = {stats_results['effects']['tms_effects']['meta_analysis']['weighted_mean_d']:.2f}
- k = {stats_results['effects']['tms_effects']['meta_analysis']['k_studies']} studies
- Total N = {stats_results['effects']['tms_effects']['meta_analysis']['total_n']}

---

## 2. Genetic Analyses

### 2.1 Pathway Enrichment

{json.dumps(genetic_results['enrichment'], indent=2, default=str)}

### 2.2 FNC Tuning Predictions

{json.dumps(genetic_results['interpretation'], indent=2, default=str)}

### 2.3 MNI Dataset Analysis Protocol

{json.dumps(genetic_results['mni_protocol'], indent=2, default=str)}

---

## 3. FNC Interpretation Summary

{stats_results['prevalence']['meta_interpretation']}

---

## 4. Testable Predictions

Based on these analyses, the FNC framework generates the following predictions:

1. **Ion channel variants** in savants will cluster in frequency-tuning pathways
2. **E/I balance** (measurable via MRS) will correlate with savant ability breadth
3. **TMS responders** will show higher baseline autistic traits
4. **Acquired savants** will show left hemisphere lesion dominance (>90%)

---

## Citation

Wikström, B. (2025). *Savant Syndrome as Differential Access to Relational Information Structures*.
Zenodo. https://doi.org/10.5281/zenodo.17789741

---

*Report generated automatically by savant-fnc analysis pipeline.*
"""
    
    output_path.write_text(report)
    print(f"\n✅ Report saved to: {output_path}")
    
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Savant-FNC Analysis Runner"
    )
    parser.add_argument("--all", action="store_true", help="Run all analyses")
    parser.add_argument("--viz", action="store_true", help="Run visualizations only")
    parser.add_argument("--stats", action="store_true", help="Run statistics only")
    parser.add_argument("--genetics", action="store_true", help="Run genetic analysis only")
    parser.add_argument("--report", action="store_true", help="Generate full report")
    parser.add_argument("--output", type=str, default="../figures", help="Output directory")
    
    args = parser.parse_args()
    
    # If no args, default to --all
    if not any([args.all, args.viz, args.stats, args.genetics, args.report]):
        args.all = True
    
    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)
    
    print("=" * 60)
    print("🧬 SAVANT-FNC ANALYSIS PIPELINE")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Output: {output_dir.absolute()}")
    
    stats_results = None
    genetic_results = None
    
    # Run requested analyses
    if args.all or args.viz:
        run_visualizations(output_dir)
    
    if args.all or args.stats:
        stats_results = run_statistics()
    
    if args.all or args.genetics:
        genetic_results = run_genetic_analysis()
    
    if args.all or args.report:
        if stats_results is None:
            stats_results = run_statistics()
        if genetic_results is None:
            genetic_results = run_genetic_analysis()
        
        generate_report(
            stats_results,
            genetic_results,
            output_dir / "analysis_report.md"
        )
    
    print("\n" + "=" * 60)
    print("✅ ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
