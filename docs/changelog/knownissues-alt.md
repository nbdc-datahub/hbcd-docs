

## Imaging Data
###### <span class="emoji" style="color: #be7215ff;"><i class="fas fa-bug"></i></span> Run ID Order May Be Incorrect
For HBCD BIDS data with multiple runs, the run number displayed in the `run-<label>` field is not guaranteed to reflect the chronological acquisition order. This applies to both raw and processed <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data, as well as derived <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data. Despite this, the data remain internally consistent — for example, the run IDs in the raw BIDS data match the corresponding runs in the processed BIDS data.               
***Expected Fix: R2.0***
--------------------------  



## Social & Environmental Determinants
###### <span class="emoji" style="color: #f97316;"><i class="fas fa-bug"></i></span> Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants.       
***Expected Fix: R2.0***
--------------------------

## Visit Information       

###### <span class="emoji" style="color: #f97316;"><i class="fas fa-bug"></i></span> Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Participants who did not withdraw from the study (and so have a value of "no" for `par_visit_data_participant_withdrawal`) have a sentinel value of `12/26/1999`, <i>meaning no withdrawal</i>, for participant withdrawal date (`par_visit_data_participant_withdrawal_date`). This can be safely ignored. Participants who did withdraw (and so have a value of “yes” for `par_visit_data_participant_withdrawal`) have a valid date and are unimpacted.          
***Expected Fix: TBD*** 
--------------------------   