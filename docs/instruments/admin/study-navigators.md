# Study Navigator Contact Form

The **Study Navigator Contact Form** data is provided by the Study Navigator, or person who is offering Study Navigator services, during and/or between study visits (V01-V06).

## Release Data

<div id="alert" class="alert-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-circle"></i></span>
  <span class="text-with-link">
  <span class="text">Responsible Use Warning</span>
  <a class="anchor-link" href="#alert" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="alert-collapsible-content">
<p>Study Navigators were strongly encouraged, but not required, to fill out the Study Navigator Contact Form. Guidance was provided to complete the contact form as soon as possible (within 24 hours) after a contact with a participant. Study Navigators were also provided with the option to complete the form to document multiple contacts within a specific time or for a specific participant (text messages, phone calls, etc.). The data is subject to recall bias.</p> 
</div>

<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
    <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</i></span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>The Study Navigator Contact Form was created for the HBCD Study as a document for characterizing participant contacts and support. The form was developed by integrating metrics from documents used in similar support professions (e.g. certified peer support, case managers, doulas, social workers, etc.). Use of the form was strongly encouraged but not mandatory for Study Navigators to complete.</p>
<p>There is wide variation across HBCD sites and Study Navigators in use of the forms, which should be considered in any analyses conducted and conclusions drawn using contact form data. Additionally, some HBCD sites provided study navigator support to all participants, and some sites focused support on participants with substance use and/or participants experiencing significant adversities.</p> 
</div>

---

The Study Navigators Contact Form dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> under <code>study_navigator/</code> (*see <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for additional details*):

<pre class="folder-tree">
hbcd/
└── concatenated/
  └── study_navigator/
      └── Study Navigator Export - Release 2.0.csv
</pre>

## Details

Recruitment and retention in studies involving pregnant individuals who use substances can be challenged by mistrust due to SUD-related stigma. To address this, the HBCD Study integrates **certified [peer support](https://www.sciencedirect.com/topics/nursing-and-health-professions/peer-group) specialists and/or other support professionals (case managers, doulas, social workers, etc., i.e., Study Navigators**, at each site’s research team to provide participant-centered support throughout the study. Study Navigators may provide support specifically to families that are substance-involved or to a wider range of participants. The breadth of the provision of Study Navigator support is determined based on the needs and capacity of each HBCD site. For details on the conceptual framework, core skills, training, and team integration of support professionals, see [Hilliard et al. 2025](https://doi.org/10.1016/j.dcn.2024.101495).

The **Study Navigator Contact Form** included in the data release captures visit-specific information when participant support is provided. This form was created in 2022 by integrating contact form information from other behavioral health practices from some Study Navigator Workgroup members. The “Support Services Offered” section of the form is original and was created specifically for the HBCD study. This data is purely descriptive and thus not scored. It documents:

- Visit details (date, time, location, scheduling, etc.)
- Support topics discussed
- Actions taken during each contact

<div id="metadata" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
    <span class="text">Study Navigator Variables</span>
    <a class="anchor-link" href="#metadata" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
  <thead>
    <tr>
      <th>Variable</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>FORM_SITE</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>CV_CUSTOM_ID_COPY</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>FORM_SOURCE</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_AT_CONTACT</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>WHO_SCHEDULED_CONTACT</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>SINGLE_OR_MULTIPLE_CONTACTS</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>CONTACT_SITE</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>SUCCESSFUL_CONTACT</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>WHY_UNABLE_TO_CONTACT</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>BARRIERS_TO_STUDY_ASSESSMENT_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>BARRIERS_TO_STUDY_ASSESSMENT_CHECKBOXES_PART_2</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>PREGNANCY_AND_LABOR_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>CHILD_HEALTH_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>PARENTS_GUARDIANS_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>BROADER_FAMILY_HEALTH_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>SOCIOECONOMIC_RESOURCES_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>SUBSTANCE_USE_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>OTHER_CHECKBOXES</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>IS_FOLLOW_UP_NEEDED</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>IS_CONTACT_SCHEDULED</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_NEXT_CONTACT</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_FINAL_NAV_CONTACT</code></td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_EDD_WEEKS_DATE_OF_COMPLETION</code></td>
      <td>&nbsp;</td>
    </tr>
  </tbody>
</table>
</div>

## Quality Control
This form is under development for HBCD. Data was collected with guidance using the <a href="../SNContactFormCompanionGuideOutline_Pilot_V4-HH.pdf" target="_blank">HBCD Study Navigation Contact Form Guide</a>.
Data review and cleaning has occurred 3 times: September 2024, February 2025, and November 2025. Minor updates to the form and the form guide were completed in September 2024 and October 2025.

## References

<div class="references"> 
<p>Hilliard, F., Horan, H., Zgierska, A. E., Edwards, R. C., & HBCD Study Navigator Workgroup. (2025). Establishing a model of peer support for pregnant persons with a substance use disorder as an innovative approach for engaging participants in the healthy brain and child development study. Developmental Cognitive Neuroscience, 71(101495), 101495. <a href="https://doi.org/10.1016/j.dcn.2024.101495" target="_blank">https://doi.org/10.1016/j.dcn.2024.101495</a></p>  
</div>
