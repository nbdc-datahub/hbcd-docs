<div style="display: flex; gap: 30px; align-items: flex-start;">
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <caption style="caption-side: top; font-weight: bold; padding-bottom: 8px;">
    Possible Values:  <code>domain</code>
    </caption>
    <tbody>
      <tr><td><code>bio</code></td><td>BioSpecimens</td></tr>
      <tr><td><code>eeg</code></td><td>Tabular EEG</td></tr>
      <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
      <tr><td><code>img</code></td><td>Tabular Imaging</td></tr>
      <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
      <tr><td><code>nt</code></td><td>Novel Tech (<i>Novel Technology & Wearable Sensors</i>)</td></tr>
      <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
      <tr><td><code>ph</code></td><td>Physical Health</td></tr>
      <tr><td><code>sed</code></td><td>Social and Environmental Determinants</td></tr>
    </tbody>
  </table>
  <table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <caption style="caption-side: top; font-weight: bold; padding-bottom: 8px;">
    Possible Values:  <code>source</code>
    </caption>
    <tbody>
      <tr><td><code>bm</code></td><td>Biological Mother</td></tr>
      <tr><td><code>cg</code></td><td>Caregiver (Responsible Adult)</td></tr>
      <tr><td><code>ch</code></td><td>Child</td></tr>
      <tr><td><code>ld</code></td><td>Linked Data</td></tr>
      <tr><td><code>ra</code></td><td>RA (research assistant)</td></tr>
    </tbody>
  </table>
</div>



<table class="compact-table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th>Keyword</th>
      <th>Domain</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>bio</code></td><td>BioSpecimens</td></tr>
    <tr><td><code>eeg</code></td><td>Tabular EEG</td></tr>
    <tr><td><code>mh</code></td><td>Behavior/Child-Caregiver Interaction</td></tr>
    <tr><td><code>img</code></td><td>Tabular Imaging</td></tr>
    <tr><td><code>ncl</code></td><td>Neurocognition and Language</td></tr>
    <tr><td><code>nt</code></td><td><span class="tooltip">Novel Tech<span class="tooltiptext">Novel Technology & Wearable Sensors</span></span></td></tr>
    <tr><td><code>pex</code></td><td>Pregnancy/Exposure Including Substance</td></tr>
    <tr><td><code>ph</code></td><td>Physical Health</td></tr>
    <tr><td><code>sed</code></td><td>Social and Environmental Determinants</td></tr>
  </tbody>
</table>

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th>Keyword</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>bm</code></td><td>Biological Mother</td></tr>
    <td><code>cg</code></td><td>Caregiver (Responsible Adult)</td>
    <tr><td><code>ch</code></td><td>Child</td></tr>
    <tr><td><code>ld</code></td><td>Linked Data</td></tr>
    <tr><td><code>ra</code></td><td>RA (research assistant)</td></tr>
  </tbody>
</table>



<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th style="width: 10%;">Component</th>
  <th style="width: 45%;">Definition</th>
  <th style="width: 35%;">Example Values</th>
</thead>
<tbody>
<tr>
  <td><b><code>domain</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Data domain (e.g. biospecimens, imaging)</td>
  <td><span class="tooltip"><code>bio</code><span class="tooltiptext">Biospecimens</span></span>;
  <span class="tooltip"><code>img</code><span class="tooltiptext">Imaging/MRI</span></span>; <i><a href="#domain">see full list</a></i></td>
</tr>
<tr>
  <td><b><code>source</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Subject/respondent (e.g., child, birth parent)</td>
  <td><span class="tooltip"><code>bm</code><span class="tooltiptext">Biological Mother</span></span>;
    <span class="tooltip"><code>ch</code><span class="tooltiptext">Child</span></span>; <i><a href="#source">see full list</a></i>
  </td>
</tr>
<tr>
<td><b><code>table</code></b></td>
<td>Instrument/protocol element name</td>
<td>Varies by instrument</td></tr>
</tr>
<tr>
<td><b><code><span style="color: teal;">{scale}</span></code></b></td>
<td style="word-wrap: break-word; white-space: normal;">Name of scale within instrument/protocol element - <i>only if instrument contains multiple scales</i></td>
<td style="word-wrap: break-word; white-space: normal;">Varies by instrument - <i><a href="#scale">see details</a></i></td></tr>
</tr>
<tr>
  <td><b><code>item</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Item number, score label, or admin field</td>
  <td style="word-wrap: break-word; white-space: normal;"><code>001</code>; <code>score</code>; <code>administration</code> - <i><a href="#item">see details</a></i></td>
</tr>
<tr>
  <td><b><code>admin</code></b></td>
  <td style="word-wrap: break-word; white-space: normal;">Admin field - <i>administrative variables only</i></td>
  <td style="word-wrap: break-word; white-space: normal;"><code>001</code>; <code>score</code>; <code>administration</code> - <i><a href="#item">see details</a></i></td>
</tr>
</tbody>
</table>