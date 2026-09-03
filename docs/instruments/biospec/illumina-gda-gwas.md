# Illumina Global Diversity GWAS Array 

{{ readme_summary(instruments.illumina_r3) }}
{{ alert_warning(instruments.illumina_r3) }}
{{ data_warning(instruments.illumina_r3) }}
{{ issues_banner() }}

---

## Instrument Details

The genomic dataset generated from the Illumina Global Diversity Array (GDA GWAS) is provided in the release as concatenated data. Along with the genomic data, the release also includes quality-control derivatives, relatedness and ancestry analyses, imputed genotypes, and copy-number variation (CNV) calls.


<!-- 
| Data product | Contents | Primary formats |
| --- | --- | --- |
| Core genotype data | Genotype calls, variant information, participant identifiers, and batch assignments | PLINK `.bed`, `.bim`, and `.fam`; text |
| QC and relatedness derivatives | Genetic principal components, relatedness estimates, family clusters, and supporting matrices | TSV, text, and binary GRM files |
| Imputed genotype data | Per-chromosome genotype dosages, genotype probabilities, indexes, and variant-level imputation metrics | bgzipped VCF, TBI, and gzipped text |
| Copy-number variation calls | Release-filtered CNV segments and sample-level QC metrics | TSV and CSV | -->


## Release Data

The core dataset contains batch metadata and a set of interlinked PLINK 1.9 files (`.bed`, `.bim`, `.fam`) aligned to the **GRCh38/hg38 Build**:

- `batch.info`: Plain-text file mapping participants to genotyping batches
- `hbcd.bed` (**[PLINK 1.9 .bed](https://www.cog-genomics.org/plink/1.9/formats#bed)**, distinct from UCSC BED): Binary genotype file
- `hbcd.bim` (**[PLINK 1.9 .bim](https://www.cog-genomics.org/plink/1.9/formats#bim)**): Variant information (chromosome, rsID, position, alleles)
- `hbcd.fam` (**[PLINK 1.9 .fam](https://www.cog-genomics.org/plink/1.9/formats#fam)**): Participant information

---

## Genomics QC and Relatedness Derivatives

Genotype data were processed using the [GDC Genomics QC pipeline](https://gdcgenomicsqc.readthedocs.io/en/latest/). Major QC and analysis steps include:

- Alternating filters for variant and subject missingness (10% followed by 2%)
- Sex checks
- Outlier detection based on the first two principal components derived from the genetic relatedness matrix using PC-AIR and PC-Relate ([GENESIS](https://bioc.r-universe.dev/GENESIS))
- Classification of relatedness using IBD estimates from [KING](https://www.kingrelatedness.com/) 

Release data files include the following (see details below):

- `pcrelate_relatedness.grm.bin`: Binary genetic relatedness matrix generated using PC-Relate.
- `pcrelate_relatedness.grm.N.bin`: Binary matrix containing the number of SNPs shared by each participant pair.
- `pcrelate_relatedness.grm.id`: Participant identifiers in the row and column order used by the relatedness matrices.
- `pcrelate_relatedness.tsv`: Tabular PC-Relate results for participant pairs.
- `family_clusters.txt`: Family-cluster assignments derived from estimated genetic relationships.

### Cryptic Relatedness

<div style="display: flex; align-items: flex-start; gap: 10px;">
  <div style="flex: 1;">
    <p>
      KING coefficient–inferred relatedness identified previously unreported familial relationships. The anonymized cryptic relatedness family graphs (right) show inferred relationships based on the following KING coefficient intervals (all visualized edges represent unreported relationships):
    </p>
    <ul>
    <li>[0.354, ∞] → Monozygotic twins or duplicate samples</li>
    <li>[0.177, 0.354] → First-degree (parent–offspring or siblings)</li>
    <li>[0.0884, 0.177] → Second-degree</li>
    <li>[0, 0.0884] → Unrelated</li>
    </ul>
  </div>
  <img
  src="https://raw.githubusercontent.com/nbdc-datahub/hbcd-docs/main/docs/resources/biospec/family-clusters.png"
  alt="Family Clusters"
  style="width: 400px; height: auto;">
</div>

### Genetic Ancestry-Based Clustering

<div style="display: flex; align-items: flex-start; gap: 15px;">
<div style="flex: 1;">
<p>
PC space derived from the first two PC-Relate components was visually inspected to assess clustering by reported race. Reported race largely clustered within the first two genetic principal components (see figure below). Subject scores along the first 32 principal components, along with IBD estimates, genetic relatedness (estimated through PC-Relate), and kinship estimates are all included as derivatives. These derivatives were calculated off of the full sample less the individuals removed for QC related reasons. Individuals that were excluded for other non-genomic QC related reasons were included in these computations even if their data and related derivatives are not included for release.
</p>
</div>
<img
src="https://raw.githubusercontent.com/nbdc-datahub/hbcd-docs/main/docs/resources/biospec/pca.png"
alt="PCA"
style="width: 500px; height: auto;">
</div>

## Imputed SNP VCFs

To maximize genomic coverage, HBCD performs genome-wide genotype imputation using high-density reference panels. Note that HBCD sequencing data is not generated; imputation is derived entirely from our GDA microarray data. Imputed SNP files included in the release include the following:

  - **Imputed Dosage VCFs (`imputed/chr*_dose.vcf.gz` + `.tbi`)**: Per-chromosome bgzipped VCF files containing estimated genotype dosages and posterior probabilities (GP) for release subjects, accompanied by Tabix index files.
  - **Variant Quality Metrics (`imputed/chr*.info.gz`)**: Per-variant imputation quality scores ($R^2$) and minor allele frequencies (MAF) from TOPMed.

##### Imputation Pipeline

 1. **Pre-Imputation Preparation**: Microarray datasets are filtered to exclude ambiguous palindromic variants, non-ACGT alleles, and multiallelic sites. Strand and allele orientation are aligned to reference genome build GRCh38 using `bcftools +fixref`.
 2. **Phasing & Imputation**: Pre-phasing is performed using **Eagle2**, followed by imputation via **Minimac4** on the **TOPMed Reference Panel (Release r3)** across multi-chromosome chunks.
 3. **Release Filtering**: Imputed dosage VCFs are filtered to retain only release-whitelisted subjects and are paired with per-variant INFO metrics.

## Copy-Number Variation Data

HBCD provides copy number variation (CNV) calls derived directly from microarray intensity data (Log R Ratio and B Allele Frequency) derived from microarray intensity.

- **CNV segment calls** (`cnv/CNV_slim.txt`): Segment-level CNV calls for non biallelic (tab-delimited)
- **CNV quality metrics** (`cnv/CNV_bookmarks.csv`): Summary CNV quality scores and bookmark metrics per sample (comma-delimited)

---

{{ references(instruments.illumina_r3) }}

