#!/usr/bin/env python3
"""
FNC Gene Scoring for Savant Genetics
====================================

Calculate FNC-specific gene scores that predict
Node tuning characteristics from genetic data.

This module implements a novel scoring system that
translates genetic variants into FNC tuning parameters.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json
from pathlib import Path

# Node tuning genes with weights
NODE_TUNING_GENES = {
    # Tuning Frequency (oscillation patterns)
    "frequency": {
        "CACNA1C": {"weight": 0.9, "direction": "frequency_shift"},
        "CACNA1D": {"weight": 0.7, "direction": "frequency_shift"},
        "SCN1A": {"weight": 0.85, "direction": "frequency_shift"},
        "SCN2A": {"weight": 0.85, "direction": "frequency_shift"},
        "SCN8A": {"weight": 0.75, "direction": "frequency_shift"},
        "KCNQ2": {"weight": 0.6, "direction": "frequency_modulation"},
        "KCNQ3": {"weight": 0.6, "direction": "frequency_modulation"},
        "HCN1": {"weight": 0.7, "direction": "pacemaking"},
    },
    
    # Filter Strength (E/I balance)
    "filtering": {
        "GABRA1": {"weight": 0.9, "direction": "inhibition"},
        "GABRB2": {"weight": 0.8, "direction": "inhibition"},
        "GABRG2": {"weight": 0.75, "direction": "inhibition"},
        "GRIN2A": {"weight": 0.85, "direction": "excitation"},
        "GRIN2B": {"weight": 0.85, "direction": "excitation"},
        "GRIA1": {"weight": 0.7, "direction": "excitation"},
        "SLC6A1": {"weight": 0.8, "direction": "gaba_transport"},
    },
    
    # Signal Integration (synaptic)
    "integration": {
        "SHANK3": {"weight": 0.95, "direction": "scaffolding"},
        "SHANK2": {"weight": 0.8, "direction": "scaffolding"},
        "NRXN1": {"weight": 0.9, "direction": "adhesion"},
        "NRXN2": {"weight": 0.7, "direction": "adhesion"},
        "NLGN3": {"weight": 0.75, "direction": "postsynaptic"},
        "NLGN4X": {"weight": 0.7, "direction": "postsynaptic"},
        "SYNGAP1": {"weight": 0.85, "direction": "plasticity"},
    },
    
    # Bandwidth (myelination/conduction)
    "bandwidth": {
        "MBP": {"weight": 0.9, "direction": "myelin_structure"},
        "PLP1": {"weight": 0.85, "direction": "myelin_structure"},
        "CNP": {"weight": 0.7, "direction": "myelin_maintenance"},
        "CNTNAP2": {"weight": 0.95, "direction": "node_ranvier"},
        "CNTN1": {"weight": 0.6, "direction": "axon_guidance"},
        "MAG": {"weight": 0.7, "direction": "myelin_axon"},
    },
    
    # Pattern Recognition
    "pattern": {
        "FOXP2": {"weight": 0.8, "direction": "language_pattern"},
        "CNTNAP2": {"weight": 0.85, "direction": "language_circuit"},
        "ATP2C2": {"weight": 0.5, "direction": "language_associated"},
        "CMIP": {"weight": 0.5, "direction": "language_associated"},
    }
}

# Domain-specific gene weights
DOMAIN_GENE_PROFILES = {
    "Music": {
        "priority_genes": ["CACNA1C", "SCN2A", "GABRA1"],
        "expected_pattern": "High frequency tuning, moderate filtering"
    },
    "Mathematics": {
        "priority_genes": ["GRIN2B", "SHANK3", "CACNA1C"],
        "expected_pattern": "High integration, enhanced pattern access"
    },
    "Art": {
        "priority_genes": ["CNTNAP2", "NRXN1", "MBP"],
        "expected_pattern": "High bandwidth, spatial processing"
    },
    "Calendar": {
        "priority_genes": ["SHANK3", "SYNGAP1", "GRIN2B"],
        "expected_pattern": "Strong integration, temporal patterns"
    }
}


@dataclass
class FNCTuningScore:
    """Container for FNC tuning score."""
    frequency_score: float
    filtering_score: float
    integration_score: float
    bandwidth_score: float
    pattern_score: float
    overall_score: float
    predicted_domain: str
    interpretation: str


def calculate_gene_contribution(
    gene: str,
    variant_impact: str = "moderate"
) -> Dict[str, float]:
    """
    Calculate a gene's contribution to each FNC tuning dimension.
    
    Args:
        gene: Gene symbol
        variant_impact: "high", "moderate", or "low"
        
    Returns:
        Dict mapping tuning dimension to contribution score
    """
    impact_multipliers = {"high": 1.0, "moderate": 0.6, "low": 0.3}
    multiplier = impact_multipliers.get(variant_impact, 0.5)
    
    contributions = {}
    
    for dimension, genes in NODE_TUNING_GENES.items():
        if gene.upper() in [g.upper() for g in genes]:
            gene_info = genes[gene.upper()]
            contributions[dimension] = gene_info["weight"] * multiplier
    
    return contributions


def calculate_fnc_scores(
    variant_genes: List[Dict],
    normalize: bool = True
) -> FNCTuningScore:
    """
    Calculate FNC tuning scores from a list of variant-affected genes.
    
    Args:
        variant_genes: List of dicts with 'gene' and optionally 'impact'
        normalize: Whether to normalize scores to 0-1 range
        
    Returns:
        FNCTuningScore object
    """
    # Initialize dimension scores
    dimension_scores = {
        "frequency": 0.0,
        "filtering": 0.0,
        "integration": 0.0,
        "bandwidth": 0.0,
        "pattern": 0.0
    }
    
    # Accumulate contributions
    for variant in variant_genes:
        gene = variant.get("gene", "")
        impact = variant.get("impact", "moderate")
        
        contributions = calculate_gene_contribution(gene, impact)
        for dim, score in contributions.items():
            dimension_scores[dim] += score
    
    # Normalize if requested
    if normalize:
        max_score = max(dimension_scores.values()) if dimension_scores.values() else 1
        if max_score > 0:
            dimension_scores = {k: v / max_score for k, v in dimension_scores.items()}
    
    # Calculate overall score (weighted average)
    weights = {"frequency": 0.2, "filtering": 0.25, "integration": 0.25, 
               "bandwidth": 0.15, "pattern": 0.15}
    overall = sum(dimension_scores[k] * weights[k] for k in dimension_scores)
    
    # Predict domain based on profile
    predicted_domain = predict_domain(dimension_scores)
    
    # Generate interpretation
    interpretation = generate_interpretation(dimension_scores, predicted_domain)
    
    return FNCTuningScore(
        frequency_score=dimension_scores["frequency"],
        filtering_score=dimension_scores["filtering"],
        integration_score=dimension_scores["integration"],
        bandwidth_score=dimension_scores["bandwidth"],
        pattern_score=dimension_scores["pattern"],
        overall_score=overall,
        predicted_domain=predicted_domain,
        interpretation=interpretation
    )


def predict_domain(dimension_scores: Dict[str, float]) -> str:
    """
    Predict most likely savant domain from tuning profile.
    
    Args:
        dimension_scores: Dict of dimension -> score
        
    Returns:
        Predicted domain string
    """
    # Simple heuristic based on dominant dimensions
    if dimension_scores["frequency"] > 0.7 and dimension_scores["pattern"] > 0.5:
        return "Music"
    elif dimension_scores["integration"] > 0.7 and dimension_scores["frequency"] > 0.5:
        return "Mathematics"
    elif dimension_scores["bandwidth"] > 0.7:
        return "Art"
    elif dimension_scores["integration"] > 0.6 and dimension_scores["pattern"] > 0.6:
        return "Calendar"
    else:
        return "Undetermined"


def generate_interpretation(
    dimension_scores: Dict[str, float],
    predicted_domain: str
) -> str:
    """
    Generate human-readable interpretation of tuning profile.
    
    Args:
        dimension_scores: Dict of dimension -> score
        predicted_domain: Predicted savant domain
        
    Returns:
        Interpretation string
    """
    # Find dominant and weak dimensions
    sorted_dims = sorted(dimension_scores.items(), key=lambda x: x[1], reverse=True)
    dominant = sorted_dims[0][0]
    weakest = sorted_dims[-1][0]
    
    interpretations = {
        "frequency": "oscillation/timing processing",
        "filtering": "information gating",
        "integration": "signal combination",
        "bandwidth": "information throughput",
        "pattern": "structure recognition"
    }
    
    return (
        f"FNC Profile: Strong {interpretations[dominant]}, "
        f"reduced {interpretations[weakest]}. "
        f"This pattern is consistent with {predicted_domain} domain access, "
        f"suggesting Node tuning that prioritizes {dominant} over {weakest}."
    )


def node_tuning_genes() -> Dict:
    """
    Return the complete node tuning gene dictionary.
    
    Returns:
        Dict of all node tuning genes by category
    """
    return NODE_TUNING_GENES


def generate_sample_report(
    sample_id: str,
    variant_genes: List[Dict]
) -> Dict:
    """
    Generate complete FNC tuning report for a sample.
    
    Args:
        sample_id: Sample identifier
        variant_genes: List of variant-affected genes
        
    Returns:
        Complete report dict
    """
    scores = calculate_fnc_scores(variant_genes)
    
    return {
        "sample_id": sample_id,
        "n_variants": len(variant_genes),
        "fnc_tuning_profile": {
            "frequency": scores.frequency_score,
            "filtering": scores.filtering_score,
            "integration": scores.integration_score,
            "bandwidth": scores.bandwidth_score,
            "pattern": scores.pattern_score
        },
        "overall_score": scores.overall_score,
        "predicted_domain": scores.predicted_domain,
        "interpretation": scores.interpretation,
        "gene_summary": {
            "frequency_genes": [v["gene"] for v in variant_genes 
                              if v["gene"].upper() in [g.upper() for g in NODE_TUNING_GENES["frequency"]]],
            "filtering_genes": [v["gene"] for v in variant_genes 
                               if v["gene"].upper() in [g.upper() for g in NODE_TUNING_GENES["filtering"]]],
            "integration_genes": [v["gene"] for v in variant_genes 
                                 if v["gene"].upper() in [g.upper() for g in NODE_TUNING_GENES["integration"]]],
        }
    }


if __name__ == "__main__":
    print("🧬 FNC Gene Scoring Demo")
    print("=" * 60)
    
    # Demo: Calculate scores for hypothetical savant sample
    demo_variants = [
        {"gene": "CACNA1C", "impact": "high"},
        {"gene": "SHANK3", "impact": "moderate"},
        {"gene": "GABRA1", "impact": "moderate"},
        {"gene": "MBP", "impact": "low"},
        {"gene": "SCN2A", "impact": "moderate"},
    ]
    
    print(f"\nInput: {len(demo_variants)} variants")
    for v in demo_variants:
        print(f"  - {v['gene']} ({v['impact']} impact)")
    
    print("\n" + "-" * 40)
    scores = calculate_fnc_scores(demo_variants)
    
    print("\nFNC Tuning Profile:")
    print(f"  Frequency:   {'█' * int(scores.frequency_score * 20):20} {scores.frequency_score:.2f}")
    print(f"  Filtering:   {'█' * int(scores.filtering_score * 20):20} {scores.filtering_score:.2f}")
    print(f"  Integration: {'█' * int(scores.integration_score * 20):20} {scores.integration_score:.2f}")
    print(f"  Bandwidth:   {'█' * int(scores.bandwidth_score * 20):20} {scores.bandwidth_score:.2f}")
    print(f"  Pattern:     {'█' * int(scores.pattern_score * 20):20} {scores.pattern_score:.2f}")
    
    print(f"\n  Overall Score: {scores.overall_score:.2f}")
    print(f"  Predicted Domain: {scores.predicted_domain}")
    
    print(f"\n  Interpretation:")
    print(f"    {scores.interpretation}")
    
    print("\n" + "=" * 60)
    
    # Generate full report
    report = generate_sample_report("DEMO_001", demo_variants)
    print("\nFull Sample Report (JSON):")
    print(json.dumps(report, indent=2))
    
    print("\n✅ FNC gene scoring demo complete!")
