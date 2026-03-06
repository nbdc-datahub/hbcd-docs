# Olink Explore 384 Inflammation 1 Panel

Protein abundance of inflammatory markers generated using the **Olink Explore 384 Inflammation 1 Panel ([Olink® Explore 3072/384](https://olink.com/products/olink-explore-3072-384))** and read with Explore version 6.7.2 are provided for the birth parent during pregnancy at Visit 1 as a measure of maternal inflammation.

## Release Data

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>Limits of detection were not calculated for this data release; however, LODs should be calculated based on NC values and proteins with a large number of samples being below the LOD should be removed or evaluated with caution.</p>
</div>

The Olink dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> under <code> proteins/olink/inflammation/</code> (*see <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for additional details*).

<pre class="folder-tree">
hbcd/
|__ concatenated/ 
    |__ proteins/
        |__ olink/
            |__ inflammation/
                |__ Olink_allplates_long.csv
                |__ Olink_allplates_wide.csv
</pre>


**[Protein NPX estimates](#normalized-protein-expression-npx) are provided in two files with different data structures:**  

<table class="table-no-vertical-lines">
<thead> <tr> <th></th> <th><code>Olink_allplates_long.csv</code></th> <th><code>Olink_allplates_wide.csv</code></th> </tr> </thead> <tbody> <tr> <td><strong>Format</strong></td> <td>Long</td> <td>Wide</td> </tr> 
<tr> <td><strong>Structure</strong></td> <td>One row per participant–protein combination</td> <td>One row per participant & one column per protein</td> </tr> 
<tr> <td><strong>Dimensions</strong></td> <td>538,080 rows × 16 columns</td> <td>1,416 rows × 1,522 columns</td> </tr> 
</tbody> </table>

## Details

### Olink Panel

Protein abundance was measured using the **Olink® Explore 384 Inflammation 1 Panel** - visit [Olink® Explore 3072/384](https://olink.com/products/olink-explore-3072-384) for details. The expandable section below provides a **quick reference of assays included in this panel**, with markers indicating assays that did not pass Olink QC in this dataset.

<div id="assays" class="table-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-circle-info"></i></span>
  <span class="text-with-link">
  <span class="text">Olink Explore 384 Inflammation Panel Quick Guide</span>
  <a class="anchor-link" href="#assays" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content"><br>
<input type="text" id="assaySearch" placeholder="Search assays..." /><br>
<p class="legend">
  <span class="failed-marker" style="color: #b00020;">✖</span>
  <b>= Assay did not pass Olink QC (excluded from downstream analyses)</b>
</p>
<div class="assay-grid">
<span>ACTN4</span><span>ADA</span><span>ADAM23</span><span>ADGRE2</span><span>AGER</span><span>AGRN</span><span>AGRP</span><span>ALDH3A1</span><span>AMBN</span><span>AMN</span><span>ANGPT1</span><span>ANGPTL2</span><span>ANGPTL4</span><span>ANXA11</span><span>AOC1</span><span>ARHGEF12</span><span>ARNT</span><span>ARTN</span><span>ATP5IF1</span><span>AXIN1</span><span>B4GALT1</span><span>BACH1</span><span>BANK1</span><span>BCR</span><span class="failed">BCL2L11</span><span class="failed">BID</span><span>BSG</span><span>BTN2A1</span><span>BTN3A2</span><span>CCL3</span><span>CCL4</span><span>CCL7</span><span>CCL11</span><span>CCL13</span><span>CCL17</span><span>CCL20</span><span>CCL21</span><span>CCL22</span><span>CCL23</span><span>CCL24</span><span>CCL25</span><span>CCL26</span><span>CCL28</span><span>CCN2</span><span>CD4</span><span>CD6</span><span>CD22</span><span>CD40</span>
<span class="failed">CD40LG</span><span>CD48</span><span>CD58</span><span>CD70</span><span>CD79B</span><span>CD83</span><span>CD84</span><span>CD160</span><span>CD200</span><span>CD200R1</span><span>CD244</span><span>CD276</span><span>CDON</span><span>CEACAM21</span><span>CEP164</span><span>CHRDL1</span><span>CLEC4A</span><span>CLEC4C</span><span>CLEC4D</span><span>CLEC4G</span>
<span class="failed">CLEC7A</span><span>CLIP2</span><span>CLSTN2</span><span>CNTNAP2</span><span>COL9A1</span><span>COLEC12</span><span>CRHBP</span><span>CRIM1</span><span>CRKL</span><span>CRLF1</span><span>CSF1</span><span>CSF3</span><span>CST7</span><span>CTRC</span><span>CTSC</span><span>CTSO</span><span>CXADR</span><span>CXCL1</span><span>CXCL3</span><span>CXCL6</span><span>CXCL8</span><span>CXCL9</span><span>CXCL10</span><span>CXCL12</span><span>CXCL14</span><span>CXCL17</span><span>DAG1</span><span>DAPP1</span><span>DBNL</span><span>DECR1</span><span>DGKZ</span><span>DNAJA2</span><span>DNPH1</span><span>DNER</span><span>DPP10</span><span>DFFA</span><span>EDAR</span><span>EGF</span><span>EGLN1</span><span>EIF4G1</span><span>EIF5A</span><span>ENAH</span><span>ENPP5</span><span>ENPP7</span><span>EPCAM</span><span>EPHA1</span><span>EPO</span><span>ERBB3</span><span>ESM1</span><span>FABP1</span><span>FABP9</span><span>FASLG</span><span>FCAR</span><span>FCRL2</span><span>FCRL3</span><span>FCRL6</span><span>FGF2</span><span>FGF5</span><span>FGF19</span><span>FIS1</span><span>FLT3LG</span><span>FOXO1</span><span>FST</span><span>FSTL3</span><span>FXYD5</span><span>GAL</span><span>GALNT3</span><span>GBP2</span><span>GMPR</span><span>GLOD4</span><span>GOPC</span><span>GZMA</span><span>GZMB</span><span class="failed">HGF</span><span>HCLS1</span><span>HEXIM1</span><span>HLA-DRA</span><span>HLA-E</span><span>HPCAL1</span><span>HSD11B1</span><span>HSPA1A</span><span>ICA1</span><span>ICAM4</span>
<span class="failed">IDS</span><span>IFNG</span><span>IFNGR1</span><span>IFNLR1</span><span>IKBKG</span><span>IL1A</span><span>IL1B</span><span>IL1R2</span><span>IL1RL2</span><span>IL1RN</span><span>IL2</span><span>IL2RB</span><span>IL3RA</span><span>IL4</span><span>IL4R</span><span>IL5</span><span>IL5RA</span><span>IL6</span><span>IL7</span><span>IL10</span><span>IL10RA</span><span>IL10RB</span><span>IL11</span><span>IL12B</span><span>IL12RB1</span><span>IL13</span><span>IL15</span><span>IL15RA</span><span>IL16</span><span>IL17A</span><span>IL17C</span><span>IL17D</span><span>IL17F</span><span>IL17RB</span><span>IL18</span><span>IL18R1</span><span>IL20</span><span>IL20RA</span><span>IL22RA1</span><span>IL24</span><span>IL32</span><span>IL33</span><span>IRAK1</span><span>IRAK4</span><span>IRF?</span><span>ISM1</span><span>ITGA6</span><span>ITGA11</span><span>ITGB6</span><span>ITM2A</span><span>JCHAIN</span><span>JUN</span><span>KLRB1</span><span>KLRD1</span><span>KRT19</span><span>KYNU</span><span>LAMA4</span><span>LAMP3</span><span>LAP3</span><span>LAIR1</span><span>LAT</span><span>LGALS4</span><span>LGALS9</span><span>LGMN</span><span>LIFR</span><span class="failed">LTA</span><span>LTBR</span><span>LY6D</span><span>LY75</span><span>LY9</span><span>MANF</span><span>MAP2K6</span><span>MAPK9</span><span>MATN2</span><span>MEGF10</span><span>MEPE</span><span>METAP1D</span><span>MERTK</span><span>MGMT</span><span class="failed">MGLL</span><span>MILR1</span><span>MICB_MICA</span><span>MMP1</span><span>MMP10</span><span>MPIG6B</span><span>MVK</span><span>MYO9B</span><span>MZB1</span><span>NBN</span><span>NCK2</span><span>NCF2</span><span>NCLN</span><span>NCR1</span><span>NELL2</span><span>NME3</span><span>NFASC</span><span>NFATC1</span><span>NFATC3</span><span>NRTN</span><span>NT5C3A</span><span>NTF3</span><span>NUDC</span><span>NUB1</span><span>NPPC</span><span>OMD</span><span>OSCAR</span><span>OSM</span><span>PADI2</span><span>PAPPA</span><span>PARP1</span><span>PCDH1</span><span>PDGFB</span><span>PDLIM7</span><span>PGF</span><span>PIK3AP1</span><span>PLA2G4A</span><span>PLAUR</span><span>PLXNA4</span><span>PNLIPRP2</span><span>PON3</span><span>PREB</span><span>PRELP</span><span>PRDX3</span><span>PRDX5</span><span>PRKAB1</span><span>PRKCQ</span><span>PRSS8</span><span>PSIP1</span><span>PSMG3</span><span>PSPN</span><span class="failed">PTPRM</span><span>PTPN6</span><span>PTX3</span><span>RAB37</span><span>RABGAP1L</span><span class="failed">RAB6A</span><span>REG4</span><span>RGS8</span><span>ROBO1</span><span>SAMD9L</span><span>SCG3</span><span>SCGB1A1</span><span>SCGB3A2</span><span>SCGN</span><span>SCRN1</span><span>SELPLG</span><span>SERPINB8</span><span>SH2D1A</span><span>SHMT1</span><span>SIGLEC1</span><span>SIGLEC10</span><span>SIRPB1</span><span>SIT1</span><span>SKAP2</span><span>SLAMF1</span><span>SLAMF7</span><span>SLC39A5</span><span>SMOC2</span><span>SMPDL3A</span><span>SPINK4</span><span>SPINT2</span><span>SPON1</span><span>SPRY2</span><span>SRPK2</span><span>STX8</span><span>SULT2A1</span><span>TANK</span><span>TFF2</span><span>TGFA</span><span>TGFB1</span><span>TIMP3</span><span>TLR3</span><span>TNF</span><span>TNFAIP8</span><span>TNFRSF4</span><span>TNFRSF11A</span><span>TNFRSF11B</span><span>TNFRSF13B</span><span>TNFRSF13C</span><span>TNFRSF14</span><span>TNFSF10</span><span>TNFSF11</span><span>TNFSF12</span><span>TNFSF13</span><span>TPSAB1</span><span>TPT1</span><span>TRAF2</span><span>TREM2</span><span>TRIM5</span><span>TRIM21</span><span>VEGFA</span><span>VEGFD</span><span>VASH1</span><span>WAS</span><span>WFIKKN2</span><span>WNT9A</span><span>YTHDF3</span>
</div>
</div>

### Normalized Protein eXpression (NPX)
Olink data are reported as **Normalized Protein eXpression (NPX)** values. NPX is a **proprietary, arbitrary unit that reflects relative protein abundance**, with higher values indicating higher abundance. It is reported on a log₂ scale, so a difference of 1 NPX represents a two-fold difference in protein abundance. Note that NPX is a relative measures and so is **only comparable for the same protein** across samples and plates. Direct comparison between different proteins are not valid. The most commonly used output variable for analyses, following Olink recommendations, is **NPX normalized by median plate intensity** (the variable 'NPX' in the release data). 

## File Variables

### Long File (`Olink_allplates_long.csv`)

<table class="table-no-vertical-lines">
<thead>
<tr>
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr><td>SampleID</td><td>Participant or control identifier</td></tr>
<tr>
<td>SampleType</td>
<td>Sample type. Possible values include:
    <ul>
    <li><b>SAMPLE</b></li>
    <li><b>NEGATIVE_CONTROL</b> (used to determine background signal levels and calculate LOD)</li>
    <li><b>PLATE_CONTROL</b> (for normalization between plates)</li>
    <li><b>SAMPLE_CONTROL</b> (positive control; not needed for downstream data analysis)</li>
    </ul>
</td></tr>
<tr><td>WellID</td><td>Plate well position</td></tr>
<tr><td>PlateID</td><td>Plate number (1-15)/run identifier</td></tr>
<tr><td>DataAnalysisRefID</td><td>Olink analysis reference ID</td></tr>
<tr><td>OlinkID</td><td>Olink assay identifier</td></tr>
<tr><td>UniProt</td><td>UniProt or control code</td></tr>
<tr><td>Assay</td><td>Assay/control name</td></tr>
<tr><td>AssayType</td><td>assay, ext_ctrl, inc_ctrl, amp_ctrl</td></tr>
<tr><td>Block</td><td>Olink plate block</td></tr>
<tr><td>Count</td><td>Raw count value (number of times the oligo sequence was counted in the sample)</td></tr>
<tr><td>ExtNPX</td><td>Extension-normalized value (count normalized by extension control)</td></tr>
<tr><td>NPX</td><td>Normalized Protein eXpression value (ExtNPX normalized by median plate intensity)</td></tr>
<tr><td>PCNormalizedNPX</td><td>Plate-control normalized NPX-like value</td></tr>
<tr><td>AssayQC</td><td>Assay-level QC flag</td></tr>
<tr><td>SampleQC</td><td>Sample-level QC flag</td></tr>
</tbody>
</table>

Reference: [Olink® Explore Overview](https://7074596.fs1.hubspotusercontent-na1.net/hubfs/7074596/01-User%20Manuals%20for%20website/1187-olink-explore-overview-user-manual.pdf)

### Wide File (`Olink_allplates_wide.csv`)

- Identifier columns:
    - SampleID
    - PlateID
- Expanded metric columns for each assay/control:
    - {Assay}_Count
    - {Assay}_ExtNPX
    - {Assay}_NPX 
    - {Assay}_PCNormalizedNPX
 - Observed assay/control count: 380
 - Observed metric suffixes: Count, ExtNPX, NPX, PCNormalizedNPX

## Quality Control

#### Olink QC 

Internal assay controls include an **extension control**, used for normalization to generate NPX values, as well as **incubation** and **amplification controls**, which monitor assay performance (QC). See the [Olink® Explore Overview](https://7074596.fs1.hubspotusercontent-na1.net/hubfs/7074596/01-User%20Manuals%20for%20website/1187-olink-explore-overview-user-manual.pdf) for a detailed description of these controls. Proteins that did not meet Olink’s quality control criteria have values of **0** for **[Protein]_Count** and **NA** for **ExtNPX**, **NPX**, and **PCNormalizedNPX**. This includes the following proteins:

<ul style="font-size: 0.9em;">
<li>BCL2L11 (O43521-2) </li>
<li>BID (P55957) </li>
<li>CD40LG (P29965) </li>
<li>CLEC7A (Q9BXN2) </li>
<li>HGF (P14210) </li>
<li>IDS (P22304) </li>
<li>LTA (P01374) </li>
<li>MGLL (Q99685)  </li>
<li>PTPRM (P28827) </li>
<li>RAB6A (P20340) </li>
</ul>

#### Plate Effects

Samples were run on 15 plates (numbered 1–15). Proteins exhibiting a plate effect were not excluded from the release. Plate effects were determined by ANOVA with a p-value threshold of *.0033* (*.05 / 15*). Post-hoc tests were run to determine if plate effects were driven by a small number of outlier plates and this was determined not to be the case. A total of **337 proteins** demonstrated a plate effect when normalizing by plate control; a total of **46 proteins** demonstrated a plate effect when normalizing by median plate intensity (expand [section below](#plate-effects) for stats).

<div id="plate-effects" class="table-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-table"></i></span>
  <span class="text-with-link">
  <span class="text">Plate Effects (Median Plate Intensity Normalization)</span>
  <a class="anchor-link" href="#plate-effects" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
  <th>Assay</th>
  <th>P-value</th>
  <th>Adj p-value</th>
  <th>&nbsp;</th>
  <th>Assay</th>
  <th>P-value</th>
  <th>Adj p-value</th>
  </tr>
<tbody>
<tr><td>IL4</td><td>9.36E-38</td><td>3.35E-35</td><td>&nbsp;</td><td>LTO1</td><td>1.57E-10</td><td>2.33E-09</td></tr>
<tr><td>NRTN</td><td>5.76E-36</td><td>1.03E-33</td><td>&nbsp;</td><td>IL22RA1</td><td>3.26E-09</td><td>4.67E-08</td></tr>
<tr><td>IL2RB</td><td>1.83E-33</td><td>2.18E-31</td><td>&nbsp;</td><td>TANK</td><td>8.15E-09</td><td>1.12E-07</td></tr>
<tr><td>PADI2</td><td>1.89E-32</td><td>1.69E-30</td><td>&nbsp;</td><td>IFNG</td><td>1.32E-08</td><td>1.76E-07</td></tr>
<tr><td>IL2</td><td>2.05E-29</td><td>1.47E-27</td><td>&nbsp;</td><td>NCLN</td><td>1.54E-08</td><td>1.96E-07</td></tr>
<tr><td>PRKCQ</td><td>1.06E-19</td><td>6.34E-18</td><td>&nbsp;</td><td>PNPT1</td><td>4.67E-08</td><td>5.77E-07</td></tr>
<tr><td>IL33</td><td>3.71E-19</td><td>1.90E-17</td><td>&nbsp;</td><td>TNFAIP8</td><td>8.73E-08</td><td>0.000001041</td></tr>
<tr><td>IL12RB1</td><td>1.28E-18</td><td>5.75E-17</td><td>&nbsp;</td><td>JUN</td><td>1.79E-07</td><td>0.000002007</td></tr>
<tr><td>TPT1</td><td>1.51E-18</td><td>6.02E-17</td><td>&nbsp;</td><td>NFATC3</td><td>1.76E-07</td><td>0.000002007</td></tr>
<tr><td>IL20RA</td><td>2.54E-18</td><td>9.10E-17</td><td>&nbsp;</td><td>LAP3</td><td>2.69E-07</td><td>0.000002913</td></tr>
<tr><td>DGKZ</td><td>5.29E-18</td><td>1.72E-16</td><td>&nbsp;</td><td>JCHAIN</td><td>0.00000199</td><td>0.000021</td></tr>
<tr><td>IL13</td><td>4.00E-17</td><td>1.19E-15</td><td>&nbsp;</td><td>RGS8</td><td>0.00000458</td><td>0.0000469</td></tr>
<tr><td>GBP2</td><td>7.27E-17</td><td>2.00E-15</td><td>&nbsp;</td><td>IL10RA</td><td>0.00000587</td><td>0.00005838</td></tr>
<tr><td>IL17F</td><td>1.75E-16</td><td>4.48E-15</td><td>&nbsp;</td><td>FXYD5</td><td>0.0000213</td><td>0.0002061</td></tr>
<tr><td>ACTN4</td><td>2.05E-16</td><td>4.89E-15</td><td>&nbsp;</td><td>PRDX3</td><td>0.00003494</td><td>0.0003292</td></tr>
<tr><td>IL15RA</td><td>5.16E-13</td><td>1.15E-11</td><td>&nbsp;</td><td>IL11</td><td>0.0001046</td><td>0.0009602</td></tr>
<tr><td>EIF5A</td><td>1.50E-12</td><td>3.17E-11</td><td>&nbsp;</td><td>FCRL3</td><td>0.0001765</td><td>0.00158</td></tr>
<tr><td>SLAMF1</td><td>2.37E-12</td><td>4.71E-11</td><td>&nbsp;</td><td>IL17A</td><td>0.0002635</td><td>0.002301</td></tr>
<tr><td>IL20</td><td>2.95E-12</td><td>5.56E-11</td><td>&nbsp;</td><td>ICA1</td><td>0.0009262</td><td>0.007895</td></tr>
<tr><td>IL5</td><td>2.09E-11</td><td>3.74E-10</td><td>&nbsp;</td><td>ITGB6</td><td>0.001058</td><td>0.008812</td></tr>
<tr><td>AMN</td><td>2.95E-11</td><td>5.03E-10</td><td>&nbsp;</td><td>CEACAM21</td><td>0.002006</td><td>0.01596</td></tr>
<tr><td>IL1B</td><td>4.79E-11</td><td>7.45E-10</td><td>&nbsp;</td><td>TNFRSF13C</td><td>0.001986</td><td>0.01596</td></tr>
<tr><td>PRKAB1</td><td>4.75E-11</td><td>7.45E-10</td><td>&nbsp;</td><td>IL24</td><td>0.00248</td><td>0.0193</td></tr>
</tbody>
</table>
</div> 

## Resources

- [Olink.com](https://olink.com/products/olink-explore-3072-384)
- [Olink Insight](https://olink.com/software/olink-insight): a web-based data analysis application provided by Olink that can be used for release data 
- [Olink® Explore Overview User Manual](https://7074596.fs1.hubspotusercontent-na1.net/hubfs/7074596/01-User%20Manuals%20for%20website/1187-olink-explore-overview-user-manual.pdf#page=6&zoom=100,170,128)

## References
<div class="references"> 
<p>Olink Proteomics AB. (2025). <i>Olink® Explore Overview User Manual</i> (Version 5.0, Doc. 1187) [PDF]. <a href="https://7074596.fs1.hubspotusercontent-na1.net/hubfs/7074596/01-User%20Manuals%20for%20website/1187-olink-explore-overview-user-manual.pdf">https://7074596.fs1.hubspotusercontent-na1.net/hubfs/7074596/01-User%20Manuals%20for%20website/1187-olink-explore-overview-user-manual.pdf</a></p>  
</div>
