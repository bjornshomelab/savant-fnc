#!/usr/bin/env python3
"""
Pathway Enrichment Analysis for Savant Genetics
================================================

Perform Gene Ontology (GO) and KEGG pathway enrichment analysis
on savant-associated gene sets.

FNC Application:
- Identify biological pathways that modify Node tuning
- Connect genetic variants to Field access mechanisms
- Generate testable predictions about savant biology

Data Sources:
- MNI Savant WES Dataset (n=15): https://cbigr.loris.ca/
- Published savant genetics literature
"""

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict

# FNC-relevant pathway categories
FNC_PATHWAY_CATEGORIES = {
    "synaptic_transmission": {
        "go_terms": ["GO:0007268", "GO:0007269", "GO:0050804"],
        "fnc_role": "Node signal processing",
        "description": "Synaptic transmission and plasticity"
    },
    "ion_channels": {
        "go_terms": ["GO:0005216", "GO:0006811", "GO:0034765"],
        "fnc_role": "Node tuning frequency",
        "description": "Ion channel activity and transport"
    },
    "myelination": {
        "go_terms": ["GO:0042552", "GO:0008366", "GO:0007272"],
        "fnc_role": "Node bandwidth",
        "description": "Axon myelination and ensheathment"
    },
    "neuronal_development": {
        "go_terms": ["GO:0048666", "GO:0007399", "GO:0048699"],
        "fnc_role": "Node architecture",
        "description": "Neuron development and differentiation"
    },
    "excitation_inhibition": {
        "go_terms": ["GO:0051932", "GO:0051931", "GO:0007214"],
        "fnc_role": "Node filtering strength",
        "description": "E/I balance regulation"
    },
    "sensory_processing": {
        "go_terms": ["GO:0050954", "GO:0007605", "GO:0007601"],
        "fnc_role": "Field channel reception",
        "description": "Sensory perception and processing"
    }
}

# Known/candidate savant-associated genes
SAVANT_CANDIDATE_GENES = {
    "CACNA1C": {
        "function": "Calcium channel",
        "pathway": "ion_channels",
        "autism_link": True,
        "fnc_prediction": "Altered synaptic tuning frequency"
    },
    "SHANK3": {
        "function": "Synaptic scaffold",
        "pathway": "synaptic_transmission",
        "autism_link": True,
        "fnc_prediction": "Modified signal integration at Node"
    },
    "NRXN1": {
        "function": "Neurexin",
        "pathway": "synaptic_transmission",
        "autism_link": True,
        "fnc_prediction": "Altered synaptic connectivity patterns"
    },
    "SCN2A": {
        "function": "Sodium channel",
        "pathway": "ion_channels",
        "autism_link": True,
        "fnc_prediction": "Changed action potential dynamics"
    },
    "CNTNAP2": {
        "function": "Cell adhesion",
        "pathway": "myelination",
        "autism_link": True,
        "fnc_prediction": "Modified Node bandwidth via myelination"
    },
    "MBP": {
        "function": "Myelin basic protein",
        "pathway": "myelination",
        "autism_link": False,
        "fnc_prediction": "Direct Node bandwidth modification"
    },
    "GABRA1": {
        "function": "GABA receptor",
        "pathway": "excitation_inhibition",
        "autism_link": True,
        "fnc_prediction": "Altered inhibitory filtering strength"
    },
    "GRIN2B": {
        "function": "NMDA receptor",
        "pathway": "synaptic_transmission",
        "autism_link": True,
        "fnc_prediction": "Modified synaptic plasticity/learning"
    }
}


@dataclass
class EnrichmentResult:
    """Container for pathway enrichment results."""
    pathway: str
    go_terms: List[str]
    genes_found: List[str]
    p_value: float
    fold_enrichment: float
    fnc_interpretation: str


def run_pathway_enrichment(
    gene_list: List[str],
    background_size: int = 20000,
    significance_threshold: float = 0.05
) -> Dict[str, EnrichmentResult]:
    """
    Run pathway enrichment analysis on a gene list.
    
    Note: This is a simplified implementation for demonstration.
    For production use, integrate with goatools or DAVID API.
    
    Args:
        gene_list: List of gene symbols
        background_size: Total genes in background (default: human genome)
        significance_threshold: P-value cutoff
        
    Returns:
        Dict mapping pathway name to EnrichmentResult
    """
    from scipy import stats
    
    results = {}
    gene_set = set(g.upper() for g in gene_list)
    
    for pathway_name, pathway_info in FNC_PATHWAY_CATEGORIES.items():
        # Find genes from input that match this pathway
        pathway_genes = [
            gene for gene, info in SAVANT_CANDIDATE_GENES.items()
            if info["pathway"] == pathway_name and gene.upper() in gene_set
        ]
        
        if not pathway_genes:
            continue
        
        # Hypergeometric test (simplified)
        # M = background, n = pathway size, N = query size, k = overlap
        M = background_size
        n = len([g for g in SAVANT_CANDIDATE_GENES if 
                SAVANT_CANDIDATE_GENES[g]["pathway"] == pathway_name]) * 100  # estimated pathway size
        N = len(gene_list)
        k = len(pathway_genes)
        
        # P-value from hypergeometric distribution
        p_value = 1 - stats.hypergeom.cdf(k - 1, M, n, N)
        
        # Fold enrichment
        expected = (n / M) * N
        fold_enrichment = k / expected if expected > 0 else float('inf')
        
        if p_value < significance_threshold:
            results[pathway_name] = EnrichmentResult(
                pathway=pathway_name,
                go_terms=pathway_info["go_terms"],
                genes_found=pathway_genes,
                p_value=p_value,
                fold_enrichment=fold_enrichment,
                fnc_interpretation=pathway_info["fnc_role"]
            )
    
    return results


def fnc_pathway_interpretation(enrichment_results: Dict[str, EnrichmentResult]) -> Dict:
    """
    Generate FNC-specific interpretations of pathway enrichment.
    
    Args:
        enrichment_results: Results from run_pathway_enrichment
        
    Returns:
        Dict with comprehensive FNC interpretation
    """
    interpretation = {
        "summary": [],
        "node_modifications": [],
        "field_access_predictions": [],
        "testable_hypotheses": []
    }
    
    for pathway_name, result in enrichment_results.items():
        pathway_info = FNC_PATHWAY_CATEGORIES[pathway_name]
        
        # Summary
        interpretation["summary"].append(
            f"{pathway_name}: {len(result.genes_found)} genes, "
            f"p={result.p_value:.2e}, {result.fold_enrichment:.1f}x enrichment"
        )
        
        # Node modification interpretation
        interpretation["node_modifications"].append({
            "pathway": pathway_name,
            "mechanism": pathway_info["fnc_role"],
            "genes": result.genes_found,
            "effect": pathway_info["description"]
        })
        
        # Field access predictions
        if pathway_name == "ion_channels":
            interpretation["field_access_predictions"].append(
                "Ion channel variants → altered tuning frequency → "
                "access to different Field harmonic layers"
            )
        elif pathway_name == "excitation_inhibition":
            interpretation["field_access_predictions"].append(
                "E/I imbalance → reduced filtering → "
                "broader but potentially less controlled Field access"
            )
        elif pathway_name == "myelination":
            interpretation["field_access_predictions"].append(
                "Myelination variants → modified bandwidth → "
                "capacity for high-fidelity Field channel transmission"
            )
        elif pathway_name == "synaptic_transmission":
            interpretation["field_access_predictions"].append(
                "Synaptic variants → altered signal integration → "
                "modified Cockpit rendering of Field information"
            )
    
    # Generate testable hypotheses
    interpretation["testable_hypotheses"] = [
        "H1: Savants with ion channel variants show domain-specific abilities matching channel expression patterns",
        "H2: E/I ratio (measurable via MRS) correlates with savant ability breadth vs depth",
        "H3: White matter integrity (DTI) predicts ability fidelity/precision",
        "H4: Variants in sensory processing genes predict sensory-domain savant abilities"
    ]
    
    return interpretation


def analyze_mni_dataset_predictions() -> Dict:
    """
    Generate predictions for MNI Savant WES dataset analysis.
    
    Based on: https://cbigr.loris.ca/
    n=15 diagnosed savants with whole exome sequencing
    
    Returns:
        Dict with analysis protocol and FNC predictions
    """
    return {
        "dataset": {
            "name": "MNI Savant WES Dataset",
            "source": "Montreal Neurological Institute",
            "n": 15,
            "data_type": "Whole Exome Sequencing",
            "access": "https://cbigr.loris.ca/"
        },
        "analysis_protocol": {
            "step_1": {
                "name": "Variant Calling Quality Control",
                "tools": ["GATK", "bcftools"],
                "filters": "QUAL>30, DP>10, GQ>20"
            },
            "step_2": {
                "name": "Functional Annotation",
                "tools": ["ANNOVAR", "VEP"],
                "databases": ["gnomAD", "ClinVar", "CADD"]
            },
            "step_3": {
                "name": "FNC Pathway Enrichment",
                "tools": ["This module", "goatools"],
                "focus_pathways": list(FNC_PATHWAY_CATEGORIES.keys())
            },
            "step_4": {
                "name": "Node-Tuning Gene Scoring",
                "tools": ["fnc_gene_scoring.py"],
                "output": "Per-sample FNC tuning profile"
            }
        },
        "fnc_predictions": {
            "expected_enrichment": [
                "Synaptic transmission pathways (based on autism overlap)",
                "Ion channel genes (E/I balance hypothesis)",
                "Sensory processing genes (domain-specific abilities)"
            ],
            "novel_predictions": [
                "Myelination genes enriched (Node bandwidth hypothesis)",
                "Circadian rhythm genes (temporal pattern access)",
                "Variants cluster by savant domain (Field channel specificity)"
            ],
            "null_predictions": [
                "No enrichment in immune pathways (not Node-relevant)",
                "No enrichment in metabolic pathways (not directly tuning-related)"
            ]
        },
        "validation_approach": {
            "internal": "Split-half validation within dataset",
            "external": "Compare to published autism WES studies",
            "functional": "Cross-reference with TMS enhancement responders"
        }
    }


if __name__ == "__main__":
    print("🧬 Pathway Enrichment Analysis Demo")
    print("=" * 60)
    
    # Demo with candidate genes
    demo_genes = ["CACNA1C", "SHANK3", "GABRA1", "SCN2A", "CNTNAP2", "MBP"]
    
    print(f"\nInput genes: {', '.join(demo_genes)}")
    print("-" * 40)
    
    results = run_pathway_enrichment(demo_genes)
    
    if results:
        print("\nEnriched Pathways:")
        for pathway, result in results.items():
            print(f"\n  {pathway}:")
            print(f"    Genes: {', '.join(result.genes_found)}")
            print(f"    p-value: {result.p_value:.2e}")
            print(f"    Fold enrichment: {result.fold_enrichment:.1f}x")
            print(f"    FNC role: {result.fnc_interpretation}")
        
        print("\n" + "-" * 40)
        print("\nFNC Interpretation:")
        interp = fnc_pathway_interpretation(results)
        for pred in interp["field_access_predictions"]:
            print(f"  → {pred}")
    
    print("\n" + "=" * 60)
    print("\nMNI Dataset Analysis Protocol:")
    mni = analyze_mni_dataset_predictions()
    print(f"  Dataset: {mni['dataset']['name']} (n={mni['dataset']['n']})")
    print(f"  Access: {mni['dataset']['access']}")
    
    print("\n✅ Pathway enrichment demo complete!")
