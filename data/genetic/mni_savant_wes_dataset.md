# Appendix G: Genetic Data and FNC Predictions

## G.1 Montreal Neurological Institute Savant WES Dataset

### Dataset Overview

**Full Title:** Savant Syndrome Whole Exome Sequencing  
**Institution:** The Montreal Neurological Institute and Hospital (The Neuro), Montreal, Quebec  
**Initiative:** C-BIG (Canadian Brain Imaging and Genetics) Open Science Initiative  
**Principal Investigator:** Dr. Guy Rouleau  
**Last Updated:** November 2022  
**Sample Size:** 15 individuals diagnosed with Savant Syndrome  
**Data Types:** FASTQ files, BAM alignments, gVCF/VCF files  
**Total Size:** 75.48 GB  
**Access URL:** https://cbigr.loris.ca/  
**Registration:** https://cbigr-open.loris.ca/login/request-account/  
**License:** CC BY-SA  
**Privacy:** Controlled access (requires registration)  
**Contact:** neurobioinfo@mcgill.ca

### Dataset Description

This dataset represents the first publicly available whole exome sequencing data specifically from individuals diagnosed with savant syndrome. Whole blood samples were obtained from all participants, DNA was isolated, and whole exome sequencing was performed using Illumina platforms (NovaSeq 6000 and HiSeq, plus ABI SOLiD4). 

Sequencing reads were processed using industry-standard pipelines:
- Burrows-Wheeler Aligner (BWA) for alignment
- Genome Analysis Toolkit (GATK) and Picard for post-alignment processing
- GATK HaplotypeCaller for variant calling

All individuals provided informed consent, and appropriate ethical approvals were obtained. The dataset is made publicly available as part of The Neuro's commitment to open science practices.

---

## G.2 FNC Framework Relevance

### Multi-Level Architecture: From Genes to Field Access

The FNC model proposes that consciousness operates through three layers:
- **Field:** Universal information substrate
- **Node:** Biological/artificial processing system (brain)
- **Cockpit:** Subjective phenomenal experience

**Key insight for genetics:** Genetic variants influence **Node architecture**, which in turn determines how the system couples to Field structures.

The MNI savant dataset enables investigation of this gene → Node → Field access pathway:

```
Genetic variants → Brain structure/function → Node tuning parameters → Field access profile → Savant abilities
```

---

## G.3 FNC Genetic Predictions

### G.3.1 Structural Connectivity Genes

**Hypothesis:** Genes affecting inter-hemispheric connectivity and corpus callosum development should correlate with Field-access patterns.

**Candidate genes:**
- **DCC** (Deleted in Colorectal Cancer) – Axon guidance, corpus callosum development
- **ROBO1/ROBO2** – Axon guidance receptors
- **NRP1** – Netrin receptor, midline crossing
- **L1CAM** – Neural cell adhesion, corpus callosum formation

**FNC prediction:** Variants reducing inter-hemispheric integration (like Kim Peek's corpus callosum agenesis) should correlate with:
- Enhanced domain-specific abilities
- Reduced cross-domain integration
- Specialized Field access to specific pattern types

**Testable hypothesis:** Savants with corpus callosum abnormalities should show more extreme domain specificity than those with intact callosal structures.

---

### G.3.2 Neurotransmitter System Genes

**Hypothesis:** Genes affecting inhibitory/excitatory balance modulate the signal-to-noise ratio in Field reception.

#### GABAergic System (Inhibition)

**Candidate genes:**
- **GAD1/GAD2** – GABA synthesis enzymes
- **GABRA/GABRB/GABRG** – GABA receptor subunits
- **SLC6A1** – GABA transporter (GAT-1)

**FNC prediction:** 
- **Reduced GABA activity** → Less inhibition → Enhanced pattern detection → Savant-like abilities
- **Increased GABA activity** → More filtering → Typical consensus-reality tuning

**Links to autism:** Many ASD-associated genes affect GABAergic signaling, consistent with FNC prediction that autism = differential Field tuning.

#### Glutamatergic System (Excitation)

**Candidate genes:**
- **GRIN1/GRIN2A/GRIN2B** – NMDA receptor subunits
- **GRIA1/GRIA2** – AMPA receptor subunits
- **SLC1A1/SLC1A2** – Glutamate transporters

**FNC prediction:** Enhanced glutamatergic signaling in pattern-processing regions (right hemisphere, posterior cortex) should correlate with savant abilities.

---

### G.3.3 Synaptic Pruning and Plasticity Genes

**Hypothesis:** Genes regulating neural pruning and myelination determine Node-tuning flexibility and developmental trajectories.

**Candidate genes:**
- **MET** – Met proto-oncogene (synaptic maturation)
- **CNTNAP2** – Contactin-associated protein 2 (neural connectivity)
- **SHANK3** – Synaptic scaffolding protein
- **NRXN1/NLGN1** – Synaptic adhesion molecules
- **MBP/PLP1** – Myelin proteins

**FNC prediction:** 
- **Reduced pruning** → More potential Field-access pathways → Enhanced pattern sensitivity but reduced efficiency
- **Altered myelination** → Changed signal propagation → Different tuning frequencies accessible

**Developmental aspect:** Congenital savants may have genetic variants affecting early neurodevelopment, creating stable alternative Node configurations from birth.

---

### G.3.4 Hemispheric Lateralization Genes

**Hypothesis:** Genes affecting left-right brain asymmetry should correlate with domain-specific abilities.

**Candidate genes:**
- **LRRTM1** – Handedness and brain asymmetry
- **PCSK6** – Left-right axis determination
- **NODAL** – Asymmetry signaling pathway
- **LMO4** – Cortical development and lateralization

**FNC prediction:** 
- **Enhanced right hemisphere development** → Spatial, musical, pattern abilities
- **Reduced left hemisphere dominance** → Less linguistic/social filtering → Direct Field access

**Evidence link:** Acquired savants often show left hemisphere damage with right hemisphere enhancement—genetic variants may predispose similar patterns developmentally.

---

## G.4 Genetic Pathways and Field-Access Domains

### Domain-Specific Genetic Profiles

The FNC model predicts that different savant ability domains may be associated with distinct genetic profiles:

| Savant Domain | Predicted Genetic Profile | Field Structure Accessed |
|---------------|--------------------------|-------------------------|
| **Calendar Calculation** | Temporal processing genes, hippocampal development | Temporal invariants, cyclical patterns |
| **Musical Ability** | Auditory cortex genes, precise timing mechanisms | Harmonic ratios, frequency structures |
| **Mathematical/Geometric** | Parietal cortex development, spatial processing | Mathematical relationships, geometric forms |
| **Artistic (Visual)** | Visual cortex, detail-processing genes | Spatial-visual patterns, perspective relationships |
| **Language (Polyglot)** | Phonological processing, auditory memory | Phonetic structures, grammatical patterns |

### Convergent Genetic Signatures

**FNC hypothesis:** Different genetic routes may lead to similar Field-access profiles. Multiple gene variants could produce:
- Reduced consensus-reality filtering
- Enhanced pattern sensitivity
- Domain-specific neural specialization

This predicts **genetic heterogeneity** in savant syndrome—not a single "savant gene" but multiple pathways to altered Node tuning.

---

## G.5 Testable Predictions from MNI Dataset

### G.5.1 Prediction: Connectivity Gene Enrichment

**Test:** Compare frequency of variants in connectivity genes (corpus callosum, axon guidance) between savants and general population.

**Expected result (FNC):** Enrichment of variants affecting inter-hemispheric integration.

**Statistical approach:** Burden testing, SKAT-O analysis on candidate gene sets.

---

### G.5.2 Prediction: GABA/Glutamate Balance Variants

**Test:** Analyze neurotransmitter system gene variants, correlate with ability domains if phenotypic data available.

**Expected result (FNC):** 
- Variants reducing inhibition in right hemisphere regions
- Enhanced excitation in pattern-processing areas
- Inverse relationship: more GABA → less savant ability intensity

---

### G.5.3 Prediction: Domain-Gene Associations

**Test:** If savant ability types are documented for these 15 individuals, test for association between:
- Calendar savants → temporal processing genes
- Musical savants → auditory cortex genes
- Mathematical savants → parietal cortex genes

**Expected result (FNC):** Domain-specific genetic enrichments, not random distribution.

---

### G.5.4 Prediction: Autism-Associated Gene Overlap

**Test:** Compare savant genetic variants with known ASD-associated genes.

**Expected result (FNC):** Significant overlap, but with distinct profile:
- Shared: Connectivity and synaptic genes (Node architecture)
- Distinct: Savants may show specific patterns in sensory processing genes

**Implication:** Autism and savant abilities share genetic basis for altered Node tuning, but savant abilities require additional factors for specialized Field access.

---

## G.6 Limitations and Considerations

### Sample Size

**n = 15** is limited for genetic discovery but sufficient for:
- Candidate gene hypothesis testing
- Preliminary pathway enrichment
- Comparing to larger ASD genetic databases

### Phenotypic Data Depth

Unknown from public documentation:
- Specific savant ability domains for each individual
- Congenital vs. acquired status
- Co-occurring conditions (ASD diagnosis, cognitive profile)

**Recommendation:** Contact MNI team to request phenotypic details for integration with genomic data.

### Genetic Architecture Complexity

Savant syndrome likely involves:
- **Polygenic effects** (multiple variants, small effects)
- **Gene-environment interactions**
- **Epigenetic factors** (not captured in WES)

FNC model accommodates this: Multiple genetic routes can produce similar Node-tuning outcomes.

---

## G.7 Integration with Other Data Sources

### Combining MNI Data with:

**1. Autism genetics databases:**
- SPARK (Simons Foundation Autism Research Initiative)
- MSSNG (Autism Speaks whole genome sequencing)
- Compare savant vs. non-savant ASD genetic profiles

**2. TMS response data:**
- If genetic data available from TMS studies (Snyder et al.)
- Test whether genetic variants predict TMS-induced savant abilities

**3. Neuroimaging-genetics:**
- Correlate genetic variants with brain structure/connectivity
- Link to Field-access patterns via neuroimaging markers

---

## G.8 Future Research Directions

### Immediate Opportunities

1. **Pathway enrichment analysis** on MNI dataset
2. **Candidate gene burden testing**
3. **Comparison to ASD genetic databases**
4. **Phenotype-genotype correlation** (if clinical data accessible)

### Long-Term Research Program

1. **Expanded genetic studies:**
   - Larger savant cohorts (international collaboration)
   - Whole genome sequencing (capture regulatory variants)
   - RNA-seq (gene expression patterns)

2. **Functional validation:**
   - CRISPR models in mice/organoids
   - Test whether candidate variants alter pattern processing
   - Validate FNC predictions about connectivity and inhibition

3. **Precision medicine applications:**
   - If genetic markers identified, could predict:
     - Risk for savant abilities in ASD
     - Response to interventions (TMS, behavioral)
     - Optimal educational approaches based on Node configuration

---

## G.9 Ethical Considerations

### Genetic Data and Neurodiversity

**Important considerations:**

1. **Avoid deficit framing:** Genetic variants associated with savant abilities should not be labeled as "mutations" or "defects"—they represent alternative Node configurations.

2. **Neurodiversity perspective:** Findings should be framed as variation in consciousness architecture, not pathology.

3. **Privacy and consent:** All use of MNI data must respect participant consent and institutional ethics approvals.

4. **Genetic discrimination:** Caution against misuse of genetic findings for discrimination or selection against neurodivergent traits.

### FNC Framework and Genetics

The FNC model inherently supports a neurodiversity-positive interpretation:
- Genetic variants → Different Node configurations → Different Field-access patterns
- No configuration is objectively "better"—each has trade-offs
- Savant abilities demonstrate the value of cognitive diversity

---

## G.10 Data Availability and Access

### How to Access MNI Savant Dataset

**Step 1:** Register at https://cbigr-open.loris.ca/login/request-account/

**Step 2:** Complete data access agreement (controlled access)

**Step 3:** Download data through C-BIG portal

**Step 4:** Analyze using standard genomics pipelines (GATK, PLINK, etc.)

### Data Citation

When using this dataset, cite:

> The Montreal Neurological Institute and Hospital Bioinformatics Core. (2022). *Savant Syndrome Whole Exome Sequencing* [Dataset]. Canadian Brain Imaging and Genetics (C-BIG) Initiative. https://cbigr.loris.ca/

### Collaboration Opportunities

Researchers interested in collaborative analysis using FNC framework should contact:
- **Dataset:** neurobioinfo@mcgill.ca
- **FNC Framework:** bjorn@base76.se

---

## G.11 Summary: Genetics as Node Architecture

The MNI savant WES dataset provides unprecedented opportunity to investigate the genetic basis of consciousness architecture. The FNC framework makes specific predictions:

**Genetic level:** Variants in connectivity, neurotransmitter, and plasticity genes
↓  
**Node level:** Altered brain structure and tuning parameters
↓  
**Field level:** Differential access to pattern structures
↓  
**Cockpit level:** Savant phenomenology and abilities

This multi-level model is **testable** with the MNI dataset and generates **falsifiable predictions** that distinguish it from alternative theories.

The integration of genetic data with FNC theory represents a complete account from molecules to phenomenology—exactly what a comprehensive theory of consciousness should provide.

---

## G.12 References

### MNI Dataset

The Montreal Neurological Institute and Hospital Bioinformatics Core. (2022). *Savant Syndrome Whole Exome Sequencing*. Canadian Brain Imaging and Genetics (C-BIG) Initiative. https://cbigr.loris.ca/

### Genetic Methods

- DePristo, M. A., et al. (2011). A framework for variation discovery and genotyping using next-generation DNA sequencing data. *Nature Genetics*, 43(5), 491-498.
- Li, H., & Durbin, R. (2009). Fast and accurate short read alignment with Burrows-Wheeler transform. *Bioinformatics*, 25(14), 1754-1760.

### Candidate Genes and Pathways

- Geschwind, D. H., & State, M. W. (2015). Gene hunting in autism spectrum disorder: on the path to precision medicine. *The Lancet Neurology*, 14(11), 1109-1120.
- Paul, L. K., et al. (2007). Agenesis of the corpus callosum: genetic, developmental and functional aspects of connectivity. *Nature Reviews Neuroscience*, 8(4), 287-299.

### FNC Framework

- Wikström, B. (2024). *The Shared Mind: Simulation, idealism, and the quantum-holographic criterion.* PhilPapers.
- Wikström, B. (2025). *Savant Syndrome as Evidence for Field-Node-Cockpit Consciousness Architecture.* [Main paper]
