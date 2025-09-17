# Upcoming Updates

## Release 2.0 (Release Date TBA)

### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Participant Data Updates

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
      <td style="word-wrap: break-word; white-space: normal;">PNRs are participants allowed to join the study in the postnatal period, completing a modified V01 and V02 after the child is born</td>
    </tr>
  </tbody>
</table>

### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Brain Imaging Data & Metadata Updates

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
      <td style="word-wrap: break-word; white-space: normal;">Addition of source DICOMs to file-based data for <a href="../../datacuration/rawbids" target="_blank">raw BIDS</a> for all imaging modalities</td>
    </tr>
    <tr>
      <td>2</td>
      <td style="word-wrap: break-word; white-space: normal;">V03+ structural and functional MRI derivatives</td>
      <td style="word-wrap: break-word; white-space: normal;">Processed <a href="../../datacuration/derivatives/#infant-fmriprep-nibabies" target="_blank" rel="noopener noreferrer">Infant fMRIPrep</a> and <a href="../../datacuration/derivatives/#xcp-d-xcp_d" target="_blank" rel="noopener noreferrer">XCP-D</a> derivatives for visits V03+</td>
    </tr>
    <tr>
      <td>3</td>
      <td style="word-wrap: break-word; white-space: normal;">MRI Scanner Information</td>
      <td style="word-wrap: break-word; white-space: normal;">MRI Scanner Information for all scanners used at each site will be added to the <code>sub-&lt;label&gt;_ses-&lt;label&gt;_scans.tsv</code> file (<a href="../../datacuration/rawbids/#participant-session-scan-level-data" target="_blank" rel="noopener noreferrer">see details</a>), including ScannerManufacturer, ScannerModel, ScannerSoftwareVersion, and ScannerSerialNumber (used to differentiate different scanners at the same site). Note that this information is currently available in the sidecar <code>.json</code> files that accompany the raw image data, e.g.:
        <pre style="font-size: 12px;">
        hbcd/
        |__ rawdata/ 
            |__ sub-<span class="label">&lt;label&gt;</span>/
                |__ ses-<span class="label">&lt;label&gt;</span>/
                    |__ anat/
                        |__ sub-<span class="label">&lt;label&gt;</span>_ses-<span class="label">&lt;label&gt;</span>_run-<span class="label">&lt;label&gt;</span>_T1w.json
        </pre>
      </td>
    </tr>
  </tbody>
</table>

### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 New Tabulated Data

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
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/#bcgi" target="_blank"><i class="fa fa-people-arrows"></i> Behavior & CG-Child Interaction</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Early Regulation in Context Assessment (<strong>ERICA</strong>)</td>
      <td style="word-wrap: break-word; white-space: normal;">Co-regulation, Child Regulation/Dysregulation, Parenting</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/#biospec" target="_blank"><i class="fa fa-vial"></i> Biospec & Omics</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Maternal Blood</td>
      <td style="word-wrap: break-word; white-space: normal;">Metals, nutrition, toxins, proteins</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/#neurocog" target="_blank"><i class="fa fa-brain"></i> Neurocog & Language</a></td>
      <td style="word-wrap: break-word; white-space: normal;">NIH Baby Toolbox</td>
      <td style="word-wrap: break-word; white-space: normal;">Cognitive/Executive Function/Memory & Language</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/#sed" target="_blank"><i class="fas fa-city"></i> Social & Env Determinants</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Geocoding & Linking External Data (<strong>GLED</strong>)</td>
      <td style="word-wrap: break-word; white-space: normal;">Toxin Exposure and Other Neighborhood Measures</td>
    </tr>
    <tr>
      <td rowspan="2" style="word-wrap: break-word; white-space: normal;"><i class="fas fa-clipboard"></i> Recruitment/Retention</td>
      <td style="word-wrap: break-word; white-space: normal;">Study Navigators Contact Form</td>
      <td style="word-wrap: break-word; white-space: normal;">Recruitment/Retention</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;">Transitions in Care (<strong>TIC</strong>) Screener</td>
      <td style="word-wrap: break-word; white-space: normal;">Recruitment/Retention</td>
    </tr>
    <tr>
      <td style="word-wrap: break-word; white-space: normal;"><a href="../../instruments/#mri" target="_blank"><i class="fas fa-magnet"></i> MRI</a></td>
      <td style="word-wrap: break-word; white-space: normal;">Pre-Scan Survey</td>
      <td style="word-wrap: break-word; white-space: normal;">Sleep information, social behavior, transportation, scheduling, etc.</td>
    </tr>
  </tbody>
</table>

### <i class="fa-solid fa-arrows-rotate" style="margin-right: 8px;"></i> 2.0 Improvements to Existing Data

<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 15px;">
  <thead>
    <tr>
      <th>#</th>
      <th>Domain</th>
      <th>Instrument</th>
      <th>Update</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Physical Health</td>
      <td>Growth</td>
      <td style="word-wrap: break-word; white-space: normal;">Inclusion of age-based height/weight/head z-scores calculated based on (non-jittered) date of birth</td>
    </tr>
  </tbody>
</table>

