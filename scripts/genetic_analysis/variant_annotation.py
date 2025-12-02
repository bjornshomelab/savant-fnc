#!/usr/bin/env python3
"""
Variant Annotation for Savant Genetics
======================================

Annotate genetic variants with functional predictions
and FNC-relevant interpretations.

Designed for use with MNI Savant WES dataset.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
import json

# FNC-relevant annotation categories
FNC_VARIANT_CATEGORIES = {
    "tuning_frequency": {
        "genes": ["CACNA1C", "CACNA1D", "SCN1A", "SCN2A", "SCN8A", "KCNQ2", "KCNQ3"],
        "mechanism": "Ion channel variants alter neuronal firing patterns",
        "fnc_effect": "Modified Node oscillation frequency"
    },
    "filter_strength": {
        "genes": ["GABRA1", "GABRB2", "GABRG2", "GRIN2A", "GRIN2B"],
        "mechanism": "Neurotransmitter receptor variants alter E/I balance",
        "fnc_effect": "Changed filtering threshold at Node"
    },
    "signal_integration": {
        "genes": ["SHANK3", "SHANK2", "NRXN1", "NLGN3", "NLGN4"],
        "mechanism": "Synaptic scaffold variants alter signal processing",
        "fnc_effect": "Modified integration of Field signals"
    },
    "bandwidth": {
        "genes": ["MBP", "PLP1", "CNP", "CNTNAP2", "CNTN1"],
        "mechanism": "Myelination variants alter signal conduction",
        "fnc_effect": "Changed Node bandwidth/capacity"
    },
    "pattern_recognition": {
        "genes": ["CNTNAP2", "FOXP2", "ATP2C2", "CMIP"],
        "mechanism": "Language/pattern processing variants",
        "fnc_effect": "Altered Field pattern extraction"
    }
}


@dataclass
class AnnotatedVariant:
    """Container for annotated variant."""
    chrom: str
    pos: int
    ref: str
    alt: str
    gene: str
    consequence: str
    impact: str
    gnomad_af: Optional[float]
    cadd_score: Optional[float]
    fnc_category: Optional[str]
    fnc_interpretation: Optional[str]


def parse_vcf_line(line: str) -> Optional[Dict]:
    """
    Parse a single VCF line into variant dict.
    
    Args:
        line: VCF line string
        
    Returns:
        Dict with variant info or None if header/invalid
    """
    if line.startswith('#'):
        return None
    
    fields = line.strip().split('\t')
    if len(fields) < 8:
        return None
    
    return {
        "chrom": fields[0],
        "pos": int(fields[1]),
        "ref": fields[3],
        "alt": fields[4],
        "info": fields[7] if len(fields) > 7 else ""
    }


def annotate_variant(variant: Dict, gene: str = None) -> AnnotatedVariant:
    """
    Annotate a single variant with FNC interpretation.
    
    Args:
        variant: Dict with chrom, pos, ref, alt
        gene: Gene symbol if known
        
    Returns:
        AnnotatedVariant with FNC annotation
    """
    # Determine FNC category
    fnc_category = None
    fnc_interpretation = None
    
    if gene:
        for category, info in FNC_VARIANT_CATEGORIES.items():
            if gene.upper() in [g.upper() for g in info["genes"]]:
                fnc_category = category
                fnc_interpretation = info["fnc_effect"]
                break
    
    return AnnotatedVariant(
        chrom=variant.get("chrom", ""),
        pos=variant.get("pos", 0),
        ref=variant.get("ref", ""),
        alt=variant.get("alt", ""),
        gene=gene or "Unknown",
        consequence=variant.get("consequence", "Unknown"),
        impact=variant.get("impact", "Unknown"),
        gnomad_af=variant.get("gnomad_af"),
        cadd_score=variant.get("cadd_score"),
        fnc_category=fnc_category,
        fnc_interpretation=fnc_interpretation
    )


def annotate_variants(variants: List[Dict]) -> List[AnnotatedVariant]:
    """
    Annotate a list of variants.
    
    Args:
        variants: List of variant dicts
        
    Returns:
        List of AnnotatedVariant objects
    """
    return [annotate_variant(v, v.get("gene")) for v in variants]


def filter_neural_variants(
    variants: List[AnnotatedVariant],
    min_cadd: float = 15.0,
    max_gnomad_af: float = 0.01
) -> List[AnnotatedVariant]:
    """
    Filter variants for neural relevance.
    
    Args:
        variants: List of AnnotatedVariant
        min_cadd: Minimum CADD score (default 15 = top 3% deleterious)
        max_gnomad_af: Maximum gnomAD allele frequency (default 1%)
        
    Returns:
        Filtered list of variants
    """
    filtered = []
    
    for v in variants:
        # Must have FNC category
        if not v.fnc_category:
            continue
        
        # Apply CADD filter if available
        if v.cadd_score is not None and v.cadd_score < min_cadd:
            continue
        
        # Apply frequency filter if available
        if v.gnomad_af is not None and v.gnomad_af > max_gnomad_af:
            continue
        
        filtered.append(v)
    
    return filtered


def generate_fnc_variant_report(variants: List[AnnotatedVariant]) -> Dict:
    """
    Generate FNC-focused variant report.
    
    Args:
        variants: List of annotated variants
        
    Returns:
        Dict with report sections
    """
    # Count by category
    category_counts = {}
    for v in variants:
        if v.fnc_category:
            category_counts[v.fnc_category] = category_counts.get(v.fnc_category, 0) + 1
    
    # Group variants by category
    by_category = {}
    for v in variants:
        if v.fnc_category:
            if v.fnc_category not in by_category:
                by_category[v.fnc_category] = []
            by_category[v.fnc_category].append({
                "gene": v.gene,
                "variant": f"{v.chrom}:{v.pos} {v.ref}>{v.alt}",
                "interpretation": v.fnc_interpretation
            })
    
    # Generate predictions
    predictions = []
    if "tuning_frequency" in category_counts:
        predictions.append(
            f"Ion channel variants ({category_counts['tuning_frequency']} found): "
            "May alter Node oscillation patterns, affecting Field access frequency bands"
        )
    if "filter_strength" in category_counts:
        predictions.append(
            f"E/I balance variants ({category_counts['filter_strength']} found): "
            "May reduce Node filtering, enabling broader Field access"
        )
    if "bandwidth" in category_counts:
        predictions.append(
            f"Myelination variants ({category_counts['bandwidth']} found): "
            "May modify Node bandwidth, affecting information throughput"
        )
    
    return {
        "total_variants": len(variants),
        "fnc_relevant": sum(1 for v in variants if v.fnc_category),
        "category_distribution": category_counts,
        "variants_by_category": by_category,
        "fnc_predictions": predictions,
        "interpretation": (
            f"Of {len(variants)} total variants, {sum(1 for v in variants if v.fnc_category)} "
            f"map to FNC-relevant pathways. "
            f"Dominant category: {max(category_counts, key=category_counts.get) if category_counts else 'None'}"
        )
    }


if __name__ == "__main__":
    print("🧬 Variant Annotation Demo")
    print("=" * 60)
    
    # Demo variants
    demo_variants = [
        {"chrom": "1", "pos": 12345, "ref": "A", "alt": "G", "gene": "CACNA1C", 
         "consequence": "missense", "cadd_score": 25.3, "gnomad_af": 0.0001},
        {"chrom": "22", "pos": 51135467, "ref": "C", "alt": "T", "gene": "SHANK3",
         "consequence": "frameshift", "cadd_score": 35.0, "gnomad_af": 0.00001},
        {"chrom": "5", "pos": 88888, "ref": "G", "alt": "A", "gene": "GABRA1",
         "consequence": "missense", "cadd_score": 18.5, "gnomad_af": 0.005},
        {"chrom": "7", "pos": 99999, "ref": "T", "alt": "C", "gene": "FOXP2",
         "consequence": "synonymous", "cadd_score": 5.0, "gnomad_af": 0.10},
    ]
    
    print(f"\nAnnotating {len(demo_variants)} demo variants...")
    annotated = annotate_variants(demo_variants)
    
    print("\nAnnotated Variants:")
    for v in annotated:
        print(f"\n  {v.gene}: {v.chrom}:{v.pos}")
        print(f"    FNC Category: {v.fnc_category or 'Not FNC-relevant'}")
        if v.fnc_interpretation:
            print(f"    Interpretation: {v.fnc_interpretation}")
    
    print("\n" + "-" * 40)
    filtered = filter_neural_variants(annotated)
    print(f"\nAfter filtering: {len(filtered)} FNC-relevant variants")
    
    print("\n" + "-" * 40)
    report = generate_fnc_variant_report(annotated)
    print("\nFNC Variant Report:")
    print(f"  {report['interpretation']}")
    print("\n  Predictions:")
    for pred in report["fnc_predictions"]:
        print(f"    → {pred}")
    
    print("\n✅ Variant annotation demo complete!")
