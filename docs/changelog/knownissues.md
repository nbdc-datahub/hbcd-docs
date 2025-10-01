
<p style="font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION: update for 2.0</i></p>

# Known Issues
The following issues have been identified in the current HBCD data release. **We are actively working to address them and will implement most fixes for Release 3.0 unless stated otherwise**. This page will be updated as new issues are discovered. If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## General
###### <span class="emoji" style="color: #f97316;"><i class="fas fa-bug"></i></span> Instruction Metadata - Caution, Please Read Carefully
Instruction text in the form's metadata is extracted programmatically from the most recent instruction field in the REDCap Data Dictionary for each form, based on field order. This means:

*   If an instruction spans multiple fields, only the last portion will be captured, resulting in partial instructions.
*   Because the instruction is provided for all fields up to the next set of instructions, some fields may display text intended for a previous section.
*   Manual curation of instruction metadata is planned for future releases. For the most accurate information, always refer to the original form.       

***Expected Fix: TBD***         

-------------------------

## Imaging Data
###### <span class="emoji" style="color: #f97316;"><i class="fas fa-bug"></i></span> Run ID Order May Be Incorrect
For HBCD BIDS data with multiple runs, the run number displayed in the `run-<label>` field is not guaranteed to reflect the chronological acquisition order. This applies to both raw and processed <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data, as well as derived <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data. Despite this, the data remain internally consistent — for example, the run IDs in the raw BIDS data match the corresponding runs in the processed BIDS data.               
***Expected Fix: R2.0***
--------------------------  

## Visit Information       

###### <span class="emoji" style="color: #f97316;"><i class="fas fa-bug"></i></span> Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Participants who did not withdraw from the study (and so have a value of "no" for `par_visit_data_participant_withdrawal`) have a sentinel value of `12/26/1999`, <i>meaning no withdrawal</i>, for participant withdrawal date (`par_visit_data_participant_withdrawal_date`). This can be safely ignored. Participants who did withdraw (and so have a value of “yes” for `par_visit_data_participant_withdrawal`) have a valid date and are unimpacted.          
***Expected Fix: TBD*** 
--------------------------   