<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}
</style>   

# Study Navigator Contact Form

{{ readme_summary(instruments.study_nav) }}
{{ alert_warning(instruments.study_nav) }}
{{ data_warning(instruments.study_nav) }}
{{ issues_banner() }}

---

## Instrument Details

{{ instrument_description(instruments.study_nav) }}

## General Variables

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
      <td>&mdash;</td>
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

## Barriers Variables

<p><b>NOTE:</b> All RESPONSE OPTION values are appended with the relevant actions taken to barriers faced, including <i>referrals</i>, <i>resources</i>,  <i>discussion</i>, and/or <i>other</i> (example: <code>biosensors/referrals</code>).</p>
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

---

{{ references(instruments.study_nav) }}
