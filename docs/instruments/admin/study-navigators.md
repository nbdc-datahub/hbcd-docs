<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>   

# Study Navigator Contact Form
<!-- 
The Study Navigators Contact Form dataset is provided as <a href="../../../datacuration/file-based-data/#concatenated-data" target="_blank">concatenated data</a> under <code>study_navigator/</code> (<i>see <a href="../../../datacuration/overview" target="_blank">Data Structure Overview</a> for additional details</i>). -->

{{ readme(instruments.studynav) }}

{{ alert_banner_macro() }}
<div class="collapsible-content">
<p>Study Navigators were strongly encouraged, but not required, to fill out the Study Navigator Contact Form. Guidance was provided to complete the contact form as soon as possible (within 24 hours) after a contact with a participant. Study Navigators were also provided with the option to complete the form to document multiple contacts within a specific time or for a specific participant (text messages, phone calls, etc.). The data is subject to recall bias.</p> 
</div>

{{ warning_banner_macro() }}
<div class="collapsible-content">
<p>The Study Navigator Contact Form was created for the HBCD Study as a document for characterizing participant contacts and support. The form was developed by integrating metrics from documents used in similar support professions (e.g. certified peer support, case managers, doulas, social workers, etc.). Use of the form was strongly encouraged but not mandatory for Study Navigators to complete.</p>
<p>There is wide variation across HBCD sites and Study Navigators in use of the forms, which should be considered in any analyses conducted and conclusions drawn using contact form data. Additionally, some HBCD sites provided study navigator support to all participants, and some sites focused support on participants with substance use and/or participants experiencing significant adversities.</p> 
</div>

{{ issues_banner_macro() }}

---

## Instrument Details

Recruitment and retention in studies involving pregnant individuals who use substances can be challenged by mistrust due to SUD-related stigma. To address this, the HBCD Study integrates **certified [peer support](https://www.sciencedirect.com/topics/nursing-and-health-professions/peer-group) specialists and/or other support professionals (case managers, doulas, social workers, etc.) i.e., Study Navigators**, at each site’s research team to provide participant-centered support throughout the study. Study Navigators may provide support specifically to families that are substance-involved or to a wider range of participants. The breadth of the provision of Study Navigator support is determined based on the needs and capacity of each HBCD site. For details on the conceptual framework, core skills, training, and team integration of support professionals, see [Hilliard et al. 2025](https://doi.org/10.1016/j.dcn.2024.101495).

The **Study Navigator Contact Form** included in the data release captures visit-specific information when participant support is provided. HBCD Study Navigator Workgroup members created this form in 2022 by integrating contact form information from other behavioral health practices. The “Support Services Offered” section of the form is original and was created specifically for the HBCD study. This data is purely descriptive and thus not scored. It documents:

- Visit details (date, time, location, scheduling, etc.)
- Support topics discussed
- Actions taken during each contact

### What is a contact? 
A “contact” includes all scheduled or unscheduled interactions relevant to the study or when providing additional support services to the participant. Contacts can be face-to-face interactions, phone calls, text chats, or other forms of communication between a participant and a research team member providing navigation services.

### Navigation Services & Support Offered: Actions Taken 
There are four options the Study Navigator can select to indicate actions taken, i.e. how they responded, for each topic, including:

<table class="table-no-vertical-lines">
<thead>
<tr>
  <th>Action</th>
  <th>Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td><b>Referrals</b></td>
    <td>When the navigator initiates a connection between individuals/entities such as a community service, clinical service, or research team member(s). The navigator is contacting this individual/entity to assist the participant in accessing additional support and/or services that they need. </td>
</tr>
<tr>
  <td><b>Resources</b></td>
    <td>The navigator shares information (fliers, brochures, websites, etc.) with the participant. The participant can use this content to obtain additional information, support, or services they need.</td>
</tr>
<tr>
  <td><b>Discussion</b></td>
    <td>The participant may simply ask the navigator to listen and/or to talk with them about a sensitive matter(s) relevant to the research study or in their personal lives. When appropriate, navigators are responsible for gently reminding participants that they are mandatory reporters. Discussion may be the first step to making a referral or providing a resource.</td>
</tr>
<tr>
  <td><b>Other</b></td>
    <td>Any other support the navigator provided that cannot be categorized as a referral, resource, or discussion.</td>
</tr>
</tbody>
</table>

## Concatenated Release Data

The Study Navigator Contact dataset is provided as in a single file as <a href="../../../datacuration/file-based-data/#concatenated-data" target="_blank">concatenated data</a>. 

<div id="metadata" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
    <span class="text">Study Navigator Variables - General</span>
    <a class="anchor-link" href="#metadata" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<table class="compact-table-no-vertical-lines">
  <thead>
    <tr>
      <th style="width: 20%;">Variable</th>
      <th style="width: 25%;">Description</th>
      <th style="width: 55%;">Possible Values (if categorical)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>FORM_SITE</code></td>
      <td>Study site of contact</td>
      <td>See <a href="../../../standards/metadata/#sites">Global Site ID Mapping</a></td>
    </tr>
    <tr>
      <td><code>CV_CUSTOM_ID_COPY</code></td>
      <td>Participant ID number</td>
      <td>&mdash;</td>
    </tr>
    <tr>
      <td><code>FORM_SOURCE</code></td>
      <td>Respondent</td>
      <td>CH <i>(Child)</i>; BP <i>(Birth Parent)</i></td>
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
      <td>one_contact; multiple_contacts</td>
    </tr>
    <tr>
      <td><code>CONTACT_SITE</code></td>
      <td>Site of contact</td>
      <td>clinic; community; home; hospital; other; phone; research_facility; zoom</td>
    </tr>
    <tr>
      <td><code>SUCCESSFUL_CONTACT</code></td>
      <td>Navigator completed a contact with the participant</td>
      <td>yes; no</td>
    </tr>
    <tr>
      <td><code>WHY_UNABLE_TO_CONTACT</code></td>
      <td>Reason if unable to contact</td>
      <td>
        declined_to_continue; did_not_present; did_not_respond_to_contact;
        other; participant_left_b4_contact; prefer_to_complete_later; unable_to_complete_due_to_circumstances
      </td>
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
      <td><code>AGE_IN_WEEKS_EDD_AT_CONTACT</code></td>
      <td>Age at contact</td>
      <td>&mdash;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_NEXT_CONTACT</code></td>
      <td>Age at next contact</td>
      <td>&mdash;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_WEEKS_EDD_FINAL_NAV_CONTACT</code></td>
      <td>Age at final contact</td>
      <td>&mdash;</td>
    </tr>
    <tr>
      <td><code>AGE_IN_EDD_WEEKS_DATE_OF_COMPLETION</code></td>
      <td>Age on completion date</td>
      <td>&mdash;</td>
    </tr>
</tbody>
</table>
</div>



<div id="metadata-barriers" class="banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text-with-link">
    <span class="text">Study Navigator Variables - Barriers Checkboxes</span>
    <a class="anchor-link" href="#metadata-barriers" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>Note: All RESPONSE OPTION values below are appended with the relevant <a href="#navigation-services-support-offered-actions-taken">actions taken</a> to barriers faced, including <i>referrals</i>, <i>resources</i>,  <i>discussion</i>, and/or <i>other</i> (e.g. <i>biosensors/referrals</i>).</b></p>
<table class="compact-table-no-vertical-lines">
<thead class="table-header">
<tr>
<th>Variable/Barrier Type</th>
<th>Response Options</th>
</tr>
</thead>
<tbody>
<tr>
<td>
  <code>BARRIERS_TO_STUDY_ASSESSMENT_CHECKBOXES</code>
  <div class="subtle">
    Relevant study domains
  </div>
</td>
<td>
biosensors; biospecimen_collection; eeg; mri; observational_assessments; surveys; other
</td>
</tr>
<tr>
<td>
  <code>BARRIERS_TO_STUDY_ASSESSMENT_CHECKBOXES_PART_2</code>
  <div class="subtle">General</div>
</td>
<td>
childcare; concerns_about_confidentiality; family_instability; lack_of_time; transportation; other
</td>
</tr>
<tr>
<td>
  <code>PREGNANCY_AND_LABOR_CHECKBOXES</code>
  <div class="subtle">Pregnancy & labor</div>
</td>
<td>newborn_and_infant_care; labor_birth; maternal_perinatal_health; postpartum_care; other</td>
</tr>

<tr>
<td>
  <code>CHILD_HEALTH_CHECKBOXES</code>
  <div class="subtle">Child health</div>
</td>
<td>mental_health; physical_health; safety; other</td>
</tr>

<tr>
<td>
  <code>PARENTS_GUARDIANS_CHECKBOXES</code>
  <div class="subtle">Parent or guardians</div>
</td>
<td> mental_health; parenting; physical_health; safety; other</td>
</tr>

<tr>
<td>
  <code>BROADER_FAMILY_HEALTH_CHECKBOXES</code>
  <div class="subtle">Family health</div>
</td>
<td>caregiving; mental_health; physical_health; safety; other</td>
</tr>

<tr>
<td>
  <code>SOCIOECONOMIC_RESOURCES_CHECKBOXES</code>
  <div class="subtle">Socioeconomic</div>
</td>
<td>
childcare; financial; food_nutrition; housing; transportation; other
</td>
</tr>
<tr>
<td>
  <code>SUBSTANCE_USE_CHECKBOXES</code>
  <div class="subtle">Substance use</div>
</td>
<td>
behavioral; medical; recovery; other
</td>
</tr>

<tr>
<td>
  <code>OTHER_CHECKBOXES</code>
  <div class="subtle">Other</div>
</td>
<td>family_crisis; court_or_legal; other</td>
</tr>

</tbody>
</table>
</div>

## References

<div class="references"> 
<p>Hilliard, F., Horan, H., Zgierska, A. E., Edwards, R. C., & HBCD Study Navigator Workgroup. (2025). Establishing a model of peer support for pregnant persons with a substance use disorder as an innovative approach for engaging participants in the healthy brain and child development study. Developmental Cognitive Neuroscience, 71(101495), 101495. <a href="https://doi.org/10.1016/j.dcn.2024.101495" target="_blank">https://doi.org/10.1016/j.dcn.2024.101495</a></p>  
</div>
