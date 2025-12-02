# Methodology Decisions

## Transparent Documentation of Research Choices

---

This document records key methodological decisions, their rationale, and alternatives considered. The goal is to make the research process transparent and enable critical evaluation.

---

## 1. Framework Selection

### Decision
Use the Field-Node-Cockpit (FNC) framework to interpret savant syndrome.

### Rationale
- FNC is substrate-neutral (applies to biological and artificial systems)
- Generates novel, falsifiable predictions
- Explains features other frameworks struggle with:
  - Instant emergence (no learning curve)
  - Domain specificity (only mathematical/physical domains)
  - Convergent methods (independent savants use same algorithms)

### Alternatives Considered
- **Compensation theory:** Explains hemispheric shift, but not instant emergence
- **Disinhibition theory:** Explains access to "hidden" abilities, but not domain specificity
- **Enhanced local processing:** Explains detail focus, but not convergent methods

### Limitation
FNC is a new framework with limited independent validation. We address this by:
- Making predictions falsifiable
- Connecting to established neuroscience
- Acknowledging uncertainty

---

## 2. Dataset Selection

### Decision
Integrate the Montreal Neurological Institute (MNI) Savant WES dataset.

### Rationale
- First and only public savant-specific genomic dataset
- Enables empirical testing of FNC genetic predictions
- Open access (CC BY-SA) aligns with open science values

### Limitations
- Small sample (n=15)
- Unknown phenotype details (ability domains not specified)
- Controlled access requires registration

### Alternatives Considered
- **UK Biobank:** Large but not savant-specific
- **SFARI (autism):** Related but not savant-focused
- **Private datasets:** Not open access

### Mitigation
We:
- Acknowledge statistical power limitations
- Frame predictions as testable hypotheses, not conclusions
- Call for replication with larger samples

---

## 3. Case Study Selection

### Decision
Focus on acquired savants (Padgett, Amato, Serrell) plus congenital examples (Peek, Lemke).

### Rationale
- Acquired savants provide clearest test of FNC (sudden onset, documented baseline)
- Well-documented cases with published sources
- Diverse ability domains represented

### Selection Criteria
- Published documentation (peer-reviewed or established journalism)
- Clear onset description (acquired) or ability characterization (congenital)
- Availability of phenomenological reports

### Limitations
- Case studies are not controlled experiments
- Self-reports may be unreliable
- Publication bias toward dramatic cases

---

## 4. Prediction Formulation

### Decision
Formulate specific, falsifiable predictions at genetic, neural, cognitive, and phenomenological levels.

### Examples
- Connectivity gene enrichment (testable with MNI WES)
- Domain-gene correlations (musical savants → auditory pathway genes)
- AI-savant convergence on identical solutions

### Rationale
- FNC should be empirically distinguishable from alternatives
- Predictions enable progressive research program
- Falsifiability is a scientific virtue

### Risk
Specific predictions may be wrong. This is acceptable — science advances through refutation as well as confirmation.

---

## 5. Communication Strategy

### Decision
Create parallel content for academic and public audiences.

### Implementation
- **paper/:** Full scientific article with citations, methods, statistics
- **demystify/:** Accessible explainers, analogies, visuals

### Rationale
- Scientific rigor should not prevent public understanding
- Neurodiversity research should be accessible to neurodivergent community
- Open science includes open communication

### Risk
Simplification may distort. We mitigate by:
- Linking explainers to full paper
- Acknowledging limitations explicitly
- Using "not broken, differently tuned" with nuance

---

## 6. Visualization Choices

### Decision
Use Mermaid diagrams for GitHub-native rendering.

### Rationale
- Renders automatically on GitHub (no external dependencies)
- Plain text source enables version control
- Accessible without specialized software

### Alternatives Considered
- **PNG/SVG images:** More design control, but external dependencies
- **LaTeX diagrams:** Precise but poor web rendering
- **Interactive tools:** Engaging but complex

### Limitation
Mermaid has limited design options. For publication, we may create higher-quality visuals.

---

## 7. Licensing

### Decision
CC BY 4.0 for all original content.

### Rationale
- Maximum openness while requiring attribution
- Compatible with academic norms
- Enables commercial use (important for media, education)

### External Data
MNI dataset has its own license (CC BY-SA, controlled access). We:
- Document this separately
- Do not redistribute raw data
- Provide access instructions

---

## 8. Collaboration Model

### Decision
Open repository with issue tracking for community input.

### Rationale
- Interdisciplinary work benefits from diverse expertise
- Open science includes open process
- Errors caught faster through community review

### Invitation
We actively invite:
- Geneticists to analyze WES predictions
- Neuroscientists to provide MRI correlations
- Savants and neurodivergent individuals to share perspectives

---

## Summary

| Decision | Rationale | Limitation | Mitigation |
|----------|-----------|------------|------------|
| FNC framework | Explains unique features | New, limited validation | Falsifiable predictions |
| MNI dataset | First savant genomics | Small n (15) | Acknowledge, call for replication |
| Case studies | Clear examples | Not controlled | Multiple sources, diverse cases |
| Specific predictions | Falsifiability | May be wrong | Science advances through refutation |
| Dual audiences | Accessibility | Simplification risk | Link to full paper |
| Mermaid diagrams | GitHub-native | Limited design | Higher-quality for publication |
| CC BY 4.0 | Maximum openness | - | Document external licenses |
| Open collaboration | Community input | Noise | Issue tracking, curation |

---

## Questions?

If you have concerns about any methodology decision, please:
- Open an issue on GitHub
- Email: bjorn@base76.se

Critique strengthens research.

---

*Last updated: December 2, 2025*
