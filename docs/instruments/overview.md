# Study Instruments
In this section we provide a brief overview of each study instrument provided in the data release, including, where applicable, details of implementation and data collection, scoring procedures, quality control procedures, data and responsible use warnings, and references. Full study protocols are available on the [HBCD Study site](https://hbcdstudy.org/study-protocols/). See [Pending Updates](../changelog/issues-updates.md#pending-updates) for details on what to expect in future releases.

## Age Of Child at Each Visit
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
<td><b>Visit 1 (V01)</b></td>
<td><b>Visit 2 (V02)</b></td>
<td><b>Visit 3 (V03)</b></td>
<td><b>Visit 4 (V04)</b></td>
<td><b>Visit 5 (V05)</b></td>
<td><b>Visit 6 (V06)</b></td>
<td><b>Visit 7 (V07)</b></td>
</tr>
<tr>
<td>Prenatal</td>
<td>0-1 month</td>
<td>3-9 months</td>
<td>9-15 months</td>
<td>10-17 months</td>
<td>15-30 months</td>
<td>16-32 months</td>
</tr>
</tbody>
</table>

## Spanish Translations
All surveys used in the HBCD Study were translated into Spanish by <a href="https://burgtranslations.com/our-services/">BURG Translations</a> and reviewed by the Spanish Language Committee (SLC) to ensure clarity and accessibility for a broad Spanish-speaking population. Instruments from third-party publishers (e.g., Bayley, CDI, BTB, Vineland) were excluded from this process, and the third party's translation was used.

## Data Collected at Visits

<img src="https://hbcdstudy.org/wp-content/uploads/2025/03/HBCD_Timeline_March2025_Updated.png" 
alt="Age of Child participants at each Visit number: Visit 1 (V01) = Prenatal; Visit 2 (V02) = 0-1 month old; Visit 3 (V03) = 3-9 months old; Visit 4 (V04) = 9-15 months old; Visit 5 (V05) = 10-17 months old;  Visit 6 (V06) = 15-30 months old; Visit 7 (V07) = 16-32 months old" width="100%" height="auto" class="center">

## Data Types Included in Release

**HBCD Study data includes both tabulated and file-based data - see <a href="../datacuration/overview" target="_blank">Data Structure Overview</a> for details.** In summary:

- <a href="../datacuration/phenotypes" target="_blank">Tabulated data</a> contain data across all participants organized according to a standardized tabulated format for HBCD (*includes Behavior, Biospecimens, Demographics, data derived from file-based MR/EEG data, etc.*).
- <a href="../datacuration/file-based-data/" target="_blank">File-based data</a> are in varied, modality-specific formats. This includes <a href="../datacuration/file-based-data/#raw-bids" target="_blank">raw BIDS data</a> and <a href="../datacuration/file-based-data/#derivatives" target="_blank">processed derivatives</a> organized under subject/session-level folders (*MRI/MRS, EEG, and Wearable Sensors*) as well as <a href="../datacuration/file-based-data/#concatenated-data" target="_blank">concatenated data</a> aggregated across participants for certain modalities (*including Genomics*).
