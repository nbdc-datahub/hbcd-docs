# Known Issues
The following issues have been identified in the current HBCD data release. **We are actively working to address them and will implement most fixes for Release 2.0 unless stated otherwise**. This page will be updated as new issues are discovered. If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## General
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Instruction Metadata - Caution, Please Read Carefully
Instruction text in the form's metadata is extracted programmatically from the most recent instruction field in the REDCap Data Dictionary for each form, based on field order. This means:

*   If an instruction spans multiple fields, only the last portion will be captured, resulting in partial instructions.
*   Because the instruction is provided for all fields up to the next set of instructions, some fields may display text intended for a previous section.
*   Manual curation of instruction metadata is planned for future releases. For the most accurate information, always refer to the original form.       

***Expected Fix: TBD***         

-------------------------

## Basic Demographics (`sed_basic_demographics`)

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Erroneous Inclusion of Response Option (2=Hawaiian) in 'Mother Race' Variable
The variable `sed_basic_demographics_screen_mother_race` has two levels to reflect Hawaiian race (`2` = `Hawaiian`; `7` = `Native Hawaiian or Other Pacific Islander`). `2` = `Hawaiian` was not a response option to this question and can be ignored; no participants selected this option.       
***Expected Fix: R2.0***
--------------------------

**ALT FORMAT - LIST IN TABLE FORMAT?**

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <th>Variable(s) & Issue Description</th>
    <th>Fix</th>
</thead>
<tbody>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: #f97316;" class="fas fa-bug"></i> <b>Mother race (<code>screen_mother_race</code>)</b><br>
    Erroneous inclusion of two levels for Hawaiian race (2 = <i>Hawaiian</i>; 7 = <i>Native Hawaiian or Other Pacific Islander</i>). The 2 = <i>Hawaiian</i> code was not a valid response option and can be ignored; no participants selected it.</td>
    <td>R2.0</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: #f97316;" class="fas fa-bug"></i> <b>Child Multi-Race and Multi-Ethnicity (ACS) (<code>child_ethnoracial_acs_by_multi_&lt;race|ethnicity&gt;</code>)</b><br>
    (#1) Variables have the same data and levels. Child Multi-Race to be removed to resolve.
    </td>
    <td>R2.0</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: #f97316;" class="fas fa-bug"></i> <b>Child Multi-Race and Multi-Ethnicity (ACS) (<code>child_ethnoracial_acs_by_multi_&lt;race|ethnicity&gt;</code>)</b><br>
    (#2) Variables populated at V01, prior to the child being born. V01 data will be removed.
    </td>
    <td>R2.0</td>
</tr>
</tbody>
</table>

## Imaging Data
###### <span class="emoji" style="color: #be7215ff;"><i class="fas fa-bug"></i></span> Run ID Order May Be Incorrect
For HBCD BIDS data with multiple runs, the run number displayed in the `run-<label>` field is not guaranteed to reflect the chronological acquisition order. This applies to both raw and processed <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data, as well as derived <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data. Despite this, the data remain internally consistent — for example, the run IDs in the raw BIDS data match the corresponding runs in the processed BIDS data.               
***Expected Fix: R2.0***
--------------------------  

## Neurocognition & Language

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> SPM-2 Age Fields Missing
Age fields are not available for the SPM-2. Please refer to corresponding age fields available from related datasets for the same time point.    
***Expected Fix: R2.0***   
--------------------------    

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> SPM-2 T-Scores
T-scores are now provided (see [1.1 Resolved Known Issues](../changelog/releasenotes.md#r1.1ngl)), but **STATUS SCORE** is still missing for all but one subscale. To be provided in the next release.                  
***Expected Fix: R2.0***   
--------------------------   

**ALT TABLE FORMAT**

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
    <th>Variable(s) & Issue Description</th>
    <th>Fix</th>
</thead>
<tbody>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: #f97316;" class="fas fa-bug"></i> <b>SPM-2 Age (<code>ncl_cg_spm2__inf</code>)</b><br>
    (#1) Age fields not included - refer to corresponding age fields from related datasets for the same time point.</td>
    <td>R2.0</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">
    <i style="color: #f97316;" class="fas fa-bug"></i> <b>SPM-2 Age (<code>ncl_cg_spm2__inf</code>)</b><br>
    (#2) T-scores are now provided (see <a href="../../changelog/releasenotes/#r1.1ngl" target="_blank">1.1 Resolved Known Issues</a>), but <b>STATUS SCORE</b> is still missing for all but one subscale. To be provided in the next release.</td>
    <td>R2.0</td>
</tr>
</tbody>
</table>

## Pregnancy & Exposure, Including Substance Use
### Pregnancy & Infant Health
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> ICD Code Names/Labels Inconsistently Provided
In cases where ICD codes are provided, corresponding names/labels are sometimes not provided. This is a known issue to be fixed in future releases. In the meantime, users can consider existing packages to merge ICD labels in [Stata](https://www.stata.com/features/overview/icd/), [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp), or [R](https://www.rdocumentation.org/packages/icd/versions/3.3).       
***Expected Fix: R2.0***
--------------------------

## Social & Environmental Determinants
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants.       
***Expected Fix: R2.0***
--------------------------

## Visit Information       

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Participants who did not withdraw from the study (and so have a value of "no" for `par_visit_data_participant_withdrawal`) have a sentinel value of `12/26/1999`, <i>meaning no withdrawal</i>, for participant withdrawal date (`par_visit_data_participant_withdrawal_date`). This can be safely ignored. Participants who did withdraw (and so have a value of “yes” for `par_visit_data_participant_withdrawal`) have a valid date and are unimpacted.          
***Expected Fix: TBD*** 
--------------------------   