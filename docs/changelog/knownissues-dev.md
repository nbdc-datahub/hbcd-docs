***🚧 To replace [Known Issues](knownissues.md) page content once patch release 1.1 is live - users please ignore!! 🚧***

# Known Issues (DEV for R1.1)
The following issues have been identified in the current HBCD data release. **We are actively working to address them and will include fixes in a future release**. This page will be updated as new issues are discovered. If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## General
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Instruction Metadata - Caution, Please Read Carefully
Instruction text in the form's metadata is extracted programmatically from the most recent instruction field in the REDCap Data Dictionary for each form, based on field order. This means:

*   If an instruction spans multiple fields, only the last portion will be captured, resulting in partial instructions.
*   Because the instruction is provided for all fields up to the next set of instructions, some fields may display text intended for a previous section.
*   Manual curation of instruction metadata is planned for future releases. For the most accurate information, always refer to the original form.       

***Expected Fix: TBD***         

-------------------------

## Basic Demographics

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Erroneous Inclusion of Response Option (2=Hawaiian) in 'Mother Race' Variable
The variable `sed_basic_demographics_screen_mother_race` has two levels to reflect Hawaiian race (`2` = `Hawaiian`; `7` = `Native Hawaiian or Other Pacific Islander`). `2` = `Hawaiian` was not a response option to this question and can be ignored; no participants selected this option.       
***Expected Fix: R2.0***
--------------------------

## Imaging Data
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Run ID Order May Be Incorrect
For HBCD BIDS data with multiple runs, the run number displayed in the `run-<label>` field is not guaranteed to reflect the chronological acquisition order. This applies to both raw and processed <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data, as well as derived <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data. Despite this, the data remain internally consistent — for example, the run IDs in the raw BIDS data match the corresponding runs in the processed BIDS data.               
***Expected Fix: R2.0***
--------------------------  

## Neurocognition & Language
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> SPM-2 Age Fields Missing
Age fields are not available for the SPM-2. Please refer to corresponding age fields available from related datasets for the same time point.    
***Expected Fix: R3.0***   
--------------------------    

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