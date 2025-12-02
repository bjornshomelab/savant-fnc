# Savant-FNC Analysis Scripts

Analysis tools for savant syndrome research using the FNC (Field-Node-Cockpit) framework.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run all analyses
python run_analysis.py --all

# Run specific modules
python run_analysis.py --viz       # Visualizations only
python run_analysis.py --stats     # Statistics only
python run_analysis.py --genetics  # Genetic analysis only
python run_analysis.py --report    # Generate full report
```

## Module Overview

### 📊 Visualization (`visualization/`)

Generate publication-ready figures:

```python
from visualization import create_domain_radar, create_lesion_heatmap

# Population domain distribution
create_domain_radar(output_path="figures/domain_radar.png")

# Lesion heatmap with FNC interpretation
create_lesion_heatmap(output_path="figures/lesion_heatmap.png")
```

**Available visualizations:**
- `domain_radar_chart.py` - Savant domain distribution radar charts
- `lesion_heatmap.py` - Brodmann area involvement heatmaps
- `case_timeline.py` - Acquired savant case timelines
- `fnc_tuning_diagram.py` - FNC tuning comparison diagrams

### 📈 Statistics (`statistics/`)

Statistical analysis with FNC interpretation:

```python
from statistics import autism_savant_association, tms_enhancement_effects

# Test autism-savant association
result = autism_savant_association()
print(f"Odds Ratio: {result['odds_ratio']:.0f}")

# Calculate TMS effect sizes
effects = tms_enhancement_effects()
print(f"Mean d = {effects['meta_analysis']['weighted_mean_d']:.2f}")
```

**Available analyses:**
- `prevalence_analysis.py` - Prevalence and association tests
- `effect_sizes.py` - Cohen's d and meta-analysis

### 🧬 Genetic Analysis (`genetic_analysis/`)

FNC-focused genetic analysis tools:

```python
from genetic_analysis import run_pathway_enrichment, calculate_fnc_scores

# Pathway enrichment
genes = ["CACNA1C", "SHANK3", "GABRA1"]
enrichment = run_pathway_enrichment(genes)

# FNC tuning scores
variants = [{"gene": "CACNA1C", "impact": "high"}]
scores = calculate_fnc_scores(variants)
print(f"Predicted domain: {scores.predicted_domain}")
```

**Available tools:**
- `pathway_enrichment.py` - GO/KEGG enrichment with FNC interpretation
- `variant_annotation.py` - VCF annotation for FNC-relevant variants
- `fnc_gene_scoring.py` - Novel FNC tuning score calculation

### 🤖 AI Experiments (`ai_experiments/`)

Test AI systems for savant-like patterns:

```python
from ai_experiments import run_pattern_test, score_savant_like_response

# Score a response for savant-like qualities
score = score_savant_like_response(
    question="What day was July 4, 1776?",
    response="Thursday.",
    correct_answer="Thursday"
)
print(f"Savant score: {score.overall_score:.2f}")
```

**Available tools:**
- `run_pattern_tests.py` - Test AI on savant-type tasks
- `score_responses.py` - Score responses for Field access patterns

## FNC Framework Integration

All modules include FNC-specific interpretations:

```python
# Every analysis returns FNC interpretation
result = autism_savant_association()
print(result['fnc_implication'])
# → "The autism-savant co-occurrence suggests shared underlying mechanisms..."

# Gene scores predict savant domains
scores = calculate_fnc_scores(variants)
print(scores.interpretation)
# → "FNC Profile: Strong oscillation/timing processing..."
```

## Output

- **Figures:** `../figures/` (PNG, 300 DPI)
- **Reports:** `../figures/analysis_report.md`
- **Data:** JSON files with full results

## Dependencies

See `requirements.txt`. Key packages:
- `numpy`, `scipy` - Numerical computation
- `matplotlib`, `seaborn` - Visualization
- `pandas` - Data manipulation
- `statsmodels` - Statistical models

## CI/CD

GitHub Actions automatically runs:
- Unit tests on push
- Visualization generation
- Statistical analyses
- Genetic analysis demos

See `.github/workflows/analysis.yml`

## Citation

```bibtex
@software{wikstrom_savant_fnc_2025,
  author = {Wikström, Björn},
  title = {Savant-FNC Analysis Scripts},
  year = {2025},
  doi = {10.5281/zenodo.17789741},
  url = {https://github.com/bjornshomelab/savant-fnc}
}
```

## License

CC BY 4.0 - See LICENSE in repository root.
