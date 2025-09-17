# Upcoming Updates

## Release 1.1 (Release Date TBA)

### Additional Data & Information Expected in 1.1


<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <tbody>
    <tr>
      <td style="text-align: center; vertical-align: top; white-space: nowrap;"><b>[2]</b></td>
      <td style="word-wrap: break-word; white-space: normal;"><b>BrainSwipes QC results</b> (<a href="../../instruments/mri/qc/#brainswipes">see details</a>) for remaining participants with XCP-D derivatives available, but no corresponding BrainSwipes results, in Release 1.0 (N=8)</p>
      </td>
    </tr>
  </tbody>
</table>

### Improvements to Existing Data

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <tbody>
    <tr>
      <td style="text-align: center; vertical-align: top; white-space: nowrap;"><b>[1]</b></td>
      <td style="word-wrap: break-word; white-space: normal;">
        <b>Inclusion of Birth Parent Sexual Orientation in <a href="../../instruments/SED/v01-demo">V01 Demographics</a></b>
        <p>
          The interim release will include birth parent sexual orientation information (<i>"Which of the following best represents how you think of yourself?"</i>), collected with the following response options:<br>
          • Gay/Lesbian<br>
          • Straight; that is, not gay or lesbian, etc.<br>
          • None of these describe me, and I'd like to see additional options 
          <span class="tooltip"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">Note: Further information on this response option (via branching logic) will not be included in release.</span></span><br>
          • Don't know<br>
          • Decline to answer<br>
          • Bisexual<br>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; vertical-align: top; white-space: nowrap;"><b>[2]</b></td>
      <td style="word-wrap: break-word; white-space: normal;">
        <b>Enhanced Medication Classification for Pregnancy & Exposure Data</b>
        <p>
          The interim release will refine medication classifications in the 
          <a href="../../instruments/#pregexp">Pregnancy & Exposure, Including Substance Use</a> domain by categorizing them into more detailed components based on RxNorm IDs. These enhancements will improve clarity and enable more granular analyses. Additional columns in the 
          <span class="tooltip">tabulated data<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> will specify:<br>
          • Brand Name<br>
          • Ingredient<br>
          • Precise Ingredient<br>
          • Multiple Active Ingredients
        </p>
      </td>
    </tr>
  </tbody>
</table>

-----------------------

## Release 2.0 (Release Date TBA)

### Additional Data & Information Expected in 2.0

#### Documentation/Resources:

*   Study Navigator Contact Form <p>&nbsp;</p>

#### Participant Data:

1. Multiple birth participants (i.e. twins or other cases where multiple participants from the same birth are enrolled in the study)
1. Postnatal Recruits (PNR): participants allowed to join the study in the postnatal period, completing a modified V01 and V02 after the child is born <p>&nbsp;</p>


#### Brain Imaging Data & Metadata:

Release 2.0 will include the following imaging data and metadata:

- **Source DICOMs** for [raw BIDS](../datacuration/rawbids.md) for all imaging modalities
- **Processed V03+ structural and functional MRI derivatives** from [Infant fMRIPrep](../datacuration/derivatives.md/#infant-fmriprep-nibabies) and [XCP-D](../datacuration/derivatives.md/#xcp-d-xcp_d) 

**MRI Scanner Information**   
In addition, Release 2.0 will include MRI scanner information for all scanners used at each site in the [`scans.tsv`](../datacuration/rawbids.md#participant-session-scan-level-data) file, including: 

  * `ScannerManufacturer`
  * `ScannerModel`
  * `ScannerSofwareVersion`
  * `ScannerSerialNumber` (Used to differentiate different scanners at the same site)

Until then, complete scanner metadata is available in the sidecar `.json` files that accompany the raw <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> image data ([see details](../datacuration/rawbids.md)). For example, metadata for a T1-weighted scan is located here:

<pre class="folder-tree">
hbcd/
|__ rawdata/ 
    |__ sub-<span class="label">&lt;label&gt;</span>/
        |__ ses-<span class="label">&lt;label&gt;</span>/
            |__ anat/
                |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T1w.json

</pre>
<br>

#### Tabulated study instrument data:

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
    <tr>
      <th style="width: 25%; border: 1px solid #ddd; padding: 10px; text-align: left; word-wrap: break-word; white-space: normal; font-size: 14px;">HBCD Workgroup</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 10px; text-align: left; word-wrap: break-word; white-space: normal; font-size: 14px;">Name of Instrument</th>
      <th style="width: 15%; border: 1px solid #ddd; padding: 10px; text-align: left; word-wrap: break-word; white-space: normal; font-size: 14px;">Acronym</th>
      <th style="width: 30%; border: 1px solid #ddd; padding: 10px; text-align: left; word-wrap: break-word; white-space: normal; font-size: 14px;">Construct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Neurocognition & Language</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">National Institutes of Health (NIH) Baby Toolbox</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">NBTB</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Cognitive and executive function (gaze-based and touch-based tasks) and memory</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Behavior & Caregiver-Child Interaction</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Early Regulation in Context Assessment</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">ERICA</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Affect and self-regulation behavior in children and families</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Biospecimens & Omics</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Maternal Blood</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Blood</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Metals, nutrition, toxins, proteins</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Geocoding</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Geocoding & Linking External Data</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">GLED</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Toxin exposure and other neighbourhood measures</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Transitions in Care</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Transitions in Care Screener</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">TIC Screener</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Survey to ssess whether there were changes in child’s main caregiver since the last visit</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Magnetic Resonance Imaging (MRI)</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Pre-Scan Survey</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Pre-Scan Survey</td>
      <td style="border: 1px solid #ddd; padding: 10px; word-wrap: break-word; white-space: normal;">Sleep information, social behavior, transportation, scheduling, etc.</td>
    </tr>
  </tbody>
</table>


### Improvements to Existing Data

#### Physical Health 

Age-based height/weight/head z-scores calculated based on (non-jittered) date of birth.