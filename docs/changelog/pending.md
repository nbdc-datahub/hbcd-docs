
# Upcoming Updates

## Release 1.1 (Expected Release Date: 2025-10-10)

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 1.1 Resolution of <a href="../knownissues" target="_blank">Known Issues</a> Labeled *Expected Fix: R1.1*

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 1.1 Improvements to Existing Data

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 10%;">Domain</th>
      <th>Measure</th>
      <th>Table Name</th>
      <th>Update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../../instruments/#mri" target="_blank"><i class="fas fa-magnet"></i> MRI</a></td>
      <td><a href="../../instruments/mri/qc/#brainswipes" target="_blank">BrainSwipes QC</a></td>
      <td><code>img_brainswipes*</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Addition of QC scores for participants with missing QC results (N=8).</td>
    </tr>
    <tr>
      <td><a href="../../instruments/#pex" target="_blank"><i class="fa-solid fa-baby"></i> PEX</a></td>
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/pregexp/pex" target="_blank">Pregnancy & Infant Health</a></td>
      <td><code>pex_bm_health*</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Medications will be categorized using RxNorm IDs, with added columns for Brand Name, Ingredient, Precise Ingredient, and Multiple Active Ingredients, to support more clear and granular analyses.</td>
    </tr>
    <tr>
      <td><a href="../../instruments/#socenvdet" target="_blank"><i class="fas fa-city"></i> SED</a></td>
      <td><a href="../../instruments/SED/v01-demo" target="_blank">V01 Demographics</a></td>
      <td><code>sed_bm_demo</code></td>
      <td style="word-wrap: break-word; white-space: normal;">
        Inclusion of Birth Parent Sexual Orientation - <i>"Which of the following best represents how you think of yourself?"</i><br>
          • Gay/Lesbian<br>
          • Straight; that is, not gay or lesbian, etc.<br>
          • None of these describe me, and I'd like to see additional options 
          <span class="tooltip tooltip-left"><span class="emoji"><i class="fa-solid fa-circle-info"></i></span><span class="tooltiptext">Note: Further information on this response option (via branching logic) will not be included in release.</span></span><br>
          • Don't know<br>
          • Decline to answer<br>
          • Bisexual
      </td>
    </tr>
  </tbody>
</table>

<br>

## Release 2.0 (Release Date TBA)

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Resolution of <a href="../knownissues" target="_blank">Known Issues</a> Labeled *Expected Fix: R2.0*

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Participant Data Updates

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
  <thead>
    <tr>
      <th>#</th>
      <th>Update</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td style="word-wrap: break-word; white-space: normal;">Inclusion of Multiple Birth Participants</td>
      <td style="word-wrap: break-word; white-space: normal;">MBPs includes twins or other cases where multiple participants from the same birth are enrolled in the study</td>
    </tr>
    <tr>
      <td>2</td>
      <td style="word-wrap: break-word; white-space: normal;">Inclusion of Postnatal Recruits</td>
      <td style="word-wrap: break-word; white-space: normal;">PNRs, participants who joined the study in the postnatal period, complete a modified V01 and V02 after the child is born</td>
    </tr>
  </tbody>
</table>

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 New Tabulated Data

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
    <tr>
      <th style="width: 25%;">Domain</th>
      <th style="width: 30%;">Name of Instrument</th>
      <th style="width: 30%;">Construct</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td colspan="3"><strong>Behavior, Biology, & Environment</strong></td>
  </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal; padding-left: 25px;"><a href="../../instruments/#bcgi" target="_blank"><i class="fa fa-people-arrows"></i> Behavior & CG-Child Interaction</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Early Regulation in Context Assessment (<strong>ERICA</strong>)</td>
      <td style="word-wrap: break-word; white-space: normal;">Co-regulation, Child Regulation/Dysregulation, Parenting</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal; padding-left: 25px;"><a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i> Biospec & Omics</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Maternal Blood</td>
      <td style="word-wrap: break-word; white-space: normal;">Metals, nutrition, toxins, proteins</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal; padding-left: 25px;"><a href="../../instruments/#neurocog" target="_blank"><i class="fa fa-brain"></i> Neurocog & Language</a></td>
      <td style="word-wrap: break-word; white-space: normal;">NIH Baby Toolbox</td>
      <td style="word-wrap: break-word; white-space: normal;">Cognitive/Executive Function/Memory & Language</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal; padding-left: 25px;"><a href="../../instruments/#socenvdet" target="_blank"><i class="fas fa-city"></i> Social & Env Determinants</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Geocoding & Linking External Data (<strong>GLED</strong>)</td>
      <td style="word-wrap: break-word; white-space: normal;">Toxin Exposure and Other Neighborhood Measures</td>
    </tr>
  <tr>
    <td colspan="3"></td>
  </tr>
  <tr>
    <td colspan="3"><strong>Brain Activity - MRI & EEG</strong></td>
  </tr>
  <tr>
      <td style="word-wrap: break-word; white-space: normal; padding-left: 25px;"><a href="../../instruments/#mri" target="_blank"><i class="fas fa-magnet"></i> MRI</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Pre-Scan Survey</td>
      <td style="word-wrap: break-word; white-space: normal;">Sleeping Scan Prep</td>
  </tr>
  <tr>
    <td colspan="3"></td>
  </tr>
  <tr>
    <td colspan="3"><strong>Recruitment & Retention</strong></td>
  </tr>
    <tr>
      <td rowspan="2" style="word-wrap: break-word; white-space: normal; padding-left: 25px;"><a href="../../instruments/#admin" target="_blank"><i class="fas fa-clipboard"></i> Recruitment/Retention</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Study Navigators Contact Form</td>
      <td style="word-wrap: break-word; white-space: normal;">Recruitment/Retention</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;">Transitions in Care (<strong>TIC</strong>) Screener</td>
      <td style="word-wrap: break-word; white-space: normal;">Recruitment/Retention</td>
    </tr>
  </tbody>
</table>

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Brain Imaging File-Based Data Updates

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
  <thead>
    <tr>
      <th>#</th>
      <th>Update</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>DICOMs</td>
      <td style="word-wrap: break-word; white-space: normal;">Addition of source DICOMs to file-based data for <a href="../../datacuration/file-based-data/#raw-bids" target="_blank">raw BIDS</a> for all imaging modalities</td>
    </tr>
    <tr>
      <td>2</td>
      <td style="word-wrap: break-word; white-space: normal;">V03+ structural and functional MRI derivatives</td>
      <td style="word-wrap: break-word; white-space: normal;">Processed <a href="../../instruments/mri/fmri/#nibabies" target="_blank" rel="noopener noreferrer">Infant fMRIPrep</a> and <a href="../../instruments/mri/fmri/#xcpd" target="_blank" rel="noopener noreferrer">XCP-D</a> derivatives for visits V03+</td>
    </tr>
    <tr>
      <td>3</td>
      <td style="word-wrap: break-word; white-space: normal;">MRI Scanner Information</td>
      <td style="word-wrap: break-word; white-space: normal;">MRI Scanner Information for all scanners used at each site will be added to the <code>sub-&lt;ID&gt;_ses-&lt;V0X&gt;_scans.tsv</code> file (<a href="../../datacuration/file-based-data/#participant-session-scan-level-data" target="_blank" rel="noopener noreferrer">see details</a>), including ScannerManufacturer, ScannerModel, ScannerSoftwareVersion, and ScannerSerialNumber (used to differentiate different scanners at the same site). Note that this information is currently available in the sidecar JSON files that accompany the raw image data, e.g.:
        <pre style="font-size: 12px;">
        hbcd/
        |__ rawdata/ 
            |__ sub-<span class="label">&lt;ID&gt;</span>/
                |__ ses-<span class="label">&lt;V0X&gt;</span>/
                    |__ anat/
                        |__ sub-<span class="label">&lt;ID&gt;</span>_ses-<span class="label">&lt;V0X&gt;</span>_run-<span class="label">&lt;X&gt;</span>_T1w.json
        </pre>
      </td>
    </tr>
  </tbody>
</table>

#### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Improvements to Existing Data

<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="width: 10%;">Domain</th>
      <th>Measure</th>
      <th>Table Name</th>
      <th>Update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="../../instruments/#physhealth" target="_blank"><i class="fa fa-heart-pulse"></i> Physical Health</a></td>
      <td><a href="../../instruments/physhealth/growth" target="_blank">Growth</a></td>
      <td><code>ph_ch_anthro</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Inclusion of age-based height/weight/head z-scores calculated based on (non-jittered) date of birth</td>
    </tr>
  </tbody>
</table>

<br>
