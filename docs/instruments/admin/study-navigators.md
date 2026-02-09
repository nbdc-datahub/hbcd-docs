<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>   

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

<div id="issues" class="issues-banner">
  <span class="emoji"><i class="fas fa-bug"></i></span>
  <span class="text">This data has known issues - <a href="../../../changelog/knownissues/#administrative" target="_blank">see details</a>.</span>
</div>

---

The Study Navigators Contact Form dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data">concatenated data</a> under <code>study_navigator/</code> (<i>see <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for additional details</i>):

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
<p><b>NOTE: For checkbox items, each checked item has a followup item to specify one or more of the following as they apply: <i>discussion</i>; <i>other</i>; <i>referrals</i>; <i>resources</i>.</b></p>
<table class="compact-table-no-vertical-lines">
  <thead>
    <tr>
      <th style="width: 20%;">Variable</th>
      <th style="width: 25%;">Description</th>
      <th style="width: 55%;">Possible / Example Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>FORM_SITE</code></td>
      <td>Site of contact</td>
      <td>See <a href="../../../access/metadata/#sites">Global Site ID Mapping</a></td>
    </tr>
    <tr>
      <td><code>CV_CUSTOM_ID_COPY</code></td>
      <td>Participant ID</td>
      <td></td>
    </tr>
    <tr>
      <td><code>FORM_SOURCE</code></td>
      <td>Respondent</td>
      <td>CH <i>(Child)</i>; BP <i>(Birth Parent)</i></td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_AT_CONTACT</code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>WHO_SCHEDULED_CONTACT</code></td>
      <td>Who scheduled visit</td>
      <td>participant; navigator; research_coordinator_ra; other
      </td>
    </tr>
    <tr>
      <td><code>SINGLE_OR_MULTIPLE_CONTACTS</code></td>
      <td>Single or multiple contacts</td>
      <td>multiple_contacts; one_contact</td>
    </tr>
    <tr>
      <td><code>CONTACT_SITE</code></td>
      <td>Site of contact</td>
      <td>clinic; community; home; hospital; other; phone; research_facility; zoom</td>
    </tr>
    <tr>
      <td><code>SUCCESSFUL_CONTACT</code></td>
      <td>Contact completed</td>
      <td>yes; no</td>
    </tr>
    <tr>
      <td><code>WHY_UNABLE_TO_CONTACT</code></td>
      <td>Reason if unable to contact</td>
      <td style="word-wrap: break-word; white-space: normal;">
        declined_to_continue; did_not_present; did_not_respond_to_contact;
        other; participant_left_b4_contact; prefer_to_complete_later; unable_to_complete_due_to_circumstances
      </td>
    </tr>
    <tr>
      <td><code>BARRIERS_TO_STUDY_ASSESSMENT_<br>CHECKBOXES</code></td>
      <td></td>
        <td>
        biosensors; biospecimen_collection; eeg;
        mri; observational_assessments; surveys
      </td>
    </tr>
    <tr>
      <td><code>BARRIERS_TO_STUDY_ASSESSMENT_<br>CHECKBOXES_PART_2</code></td>
      <td></td>
      <td style="word-wrap: break-word; white-space: normal;">
        childcare; concerns_about_confidentiality; family_instability;
        lack_of_time; other; transportation
      </td>
    </tr>
    <tr>
      <td><code>PREGNANCY_AND_LABOR_CHECKBOXES</code></td>
      <td></td>
      <td style="word-wrap: break-word; white-space: normal;">
        newborn_and_infant_care; labor_birth;
        maternal_perinatal_health; postpartum_care
      </td>
    </tr>
    <tr>
      <td><code>CHILD_HEALTH_CHECKBOXES</code></td>
      <td></td>
      <td>
        mental_health; physical_health; safety
      </td>
    </tr>
    <tr>
      <td><code>PARENTS_GUARDIANS_CHECKBOXES</code></td>
      <td></td>
      <td>
        mental_health; parenting; physical_health; safety
      </td>
    </tr>
    <tr>
      <td><code>BROADER_FAMILY_HEALTH_CHECKBOXES</code></td>
      <td></td>
      <td>
        caregiving; mental_health; physical_health; safety
      </td>
    </tr>
    <tr>
      <td><code>SOCIOECONOMIC_RESOURCES_CHECKBOXES</code></td>
      <td></td>
      <td>
        childcare; financial; food_nutrition; housing; transportation
      </td>
    </tr>
    <tr>
      <td><code>SUBSTANCE_USE_CHECKBOXES</code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>OTHER_CHECKBOXES</code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>IS_FOLLOW_UP_NEEDED</code></td>
      <td>Follow-up needed</td>
      <td>yes; no</td>
    </tr>
    <tr>
      <td><code>IS_CONTACT_SCHEDULED</code></td>
      <td>Follow-up contact scheduled</td>
      <td>yes; no</td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_NEXT_CONTACT</code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_FINAL_NAV_CONTACT</code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>AGE_IN_EDD_WEEKS_DATE_OF_COMPLETION</code></td>
      <td></td>
      <td></td>
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
