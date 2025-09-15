# Known Issues
The following issues have been identified in the current HBCD data release. **We are actively working to address them and will include fixes in either the patch (Release 1.1) or next Release 2.0 unless stated otherwise**. This page will be updated as new issues are discovered. If you have questions or would like to report an issue, please submit a ticket through the [Lasso Help Center](https://nbdc.lassoinformatics.com/issue-tracker).

## General
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Instruction Metadata - Caution, Please Read Carefully
Instruction text in the form's metadata is extracted programmatically from the most recent instruction field in the REDCap Data Dictionary for each form, based on field order. This means:

*   If an instruction spans multiple fields, only the last portion will be captured, resulting in partial instructions.
*   Because the instruction is provided for all fields up to the next set of instructions, some fields may display text intended for a previous section.
*   Manual curation of instruction metadata is planned for future releases. For the most accurate information, always refer to the original form.       

***Expected Date of Fix TBD***

## Basic Demographics
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Income Not Displayed For All Participants     
In rare cases, the `Income` field in Basic Demographics (`sed_basic_demographics`) may not be displayed for certain participants. This issue results from errors in transferring data from the REDCap Demographics form (`sed_bm_demo`) into the Basic Demographics. For complete income information, please reference the original source field in `sed_bm_demo`.          
***Expected Fix: R1.1***     

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span>  Duplicate Options for 'Mother Race' Variable
The variable 'Mother Race' (`sed_basic_demographics_screen_mother_race`) has duplicate options for the selection of 'Black African American' (option #3). This option is not used for data entry, and instead the 'Black_or African American' option (option #5) should be used. No other variables are affected by this.           
***Expected Fix: R1.1***       

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Gestational Age at Delivery and Mother’s Age at Delivery
Gestational Age at Delivery (`sed_basic_demographics_gestational_age_delivery`) and Mother's Age at Delivery (`sed_basic_demographics_mother_age_delivery`) are variables that should only be available for participants who have V01 + V02 or V03 in the data release which had a cutoff of visit completion of July 1, 2024. However, for these measures data for deliveries after July 1, 2024 were included in the release in error. These fields which represent births beyond our cutoff dates were incorrectly made available, did not undergo QC, and will be removed in the patch release. Users can currently filter or remove any values for participants that do not have a V01 + V02 or V03 until the fix.         
***Expected Fix: R1.1***    

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Mother Ethnicity
The variable `screen_mother_ethnicity` should be a 2-level variable, however it is currently noted as a 4-level variable in the data dictionary. Levels of 0 and 1 (in the data dictionary) are included in error, they do not appear in the dataset; all participants with valid data have a value of 2 (Hispanic) or 3 (non-Hispanic).            
***Expected Fix: R1.1*** 

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Mother Race and Ethnicity
For the variable `rc_mother_ethnoracial_aou_race_ethnicity`, the “None of these fully describe me/Other” response option is not currently a separate category for this variable and will be added.          
***Expected Fix: R1.1*** 

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Erroneous Inclusion of Response Option (2=Hawaiian) in 'Mother Race' Variable
The variable `sed_basic_demographics_screen_mother_race` has two levels to reflect Hawaiian race (`2` = `Hawaiian`; `7` = `Native Hawaiian or Other Pacific Islander`). `2` = `Hawaiian` was not a response option to this question and can be ignored; no participants selected this option.       
***Expected Fix: R2.0***      


## Biospecimens
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Nails & Urine: Collection & Analysis Dates Currently Missing
Collection dates and analysis dates for Nails and Urine are not provided in the current release and will be provided in the future.         
***Expected Fix: R1.1***         

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Urine: Incorrect Specific Gravity Variable
Urine concentrations vary by participant and concentration corrections can be made by creatine or specific gravity. However, the urine specific gravity variable is incorrect (`bio_bm_biosample_urine_bio_spg_u`) (there are several participants with “1” when the variable should be expressed in the thousands) and should therefore not be analyzed. Only the initial creatinine results from sample validation should be used for urinary concentration corrections.          
***Expected Fix: R1.1***

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Urine: Toxicology (Cotinine)
There may be negative values for urinary toxicology results (e.g. `bio_bm_biosample_urine_bio_bm_biosample_urine_bio_c_cot_u`). Please note that negative values for these variables are not biologically plausible. We recommend users convert these values to 0 prior to analyzing their data.            
***Expected Fix: R1.1***    

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Urine: Negative Gestational Ages 
There are two participants with negative gestational ages in the urine biosample dataset due to inaccurate collection dates of the biosample. Please do not include these two observations in your analysis.        
***Expected Fix: R1.1***   

## EEG
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> HBCD-MADE Resting-State Derivatives
The HBCD-MADE summary statistics for resting-state EEG data contained in the derivative file `processed_data/*_task-RS_powerSummaryStats.csv` (see HBCD-MADE derivatives structure [here](../datacuration/derivatives.md#hbcd-made-made) for details) are incorrect due to a former bug in the pipeline and should not be used for analysis. Users should instead generate these files themselves using scripts provided via [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/en/stable/) for extracting summary statistics.          
***Expected Fix: R1.1***  

## Imaging Data
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Run ID Order May Be Incorrect
For HBCD BIDS data with multiple runs, the run number displayed in the `run-<label>` field is not guaranteed to reflect the chronological acquisition order. This applies to both raw and processed <span class="tooltip">file-based<span class="tooltiptext">imaging and biosignal data<br>(varied formats)</span></span> data, as well as derived <span class="tooltip">tabulated<span class="tooltiptext">instrument and derived data<br>(tabulated format)</span></span> data. Despite this, the data remain internally consistent — for example, the run IDs in the raw BIDS data match the corresponding runs in the processed BIDS data.               
***Expected Fix: R2.0***  

## Neurocognition & Language
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> SPM-2 T-Scores
The t-scores are currently not provided, as the original conversion from raw score to t-score was incorrect. The t-scores will be corrected and provided in a future data release.     
***Expected Fix: R1.1***     

## Pregnancy & Exposure, Including Substance Use
### Pregnancy & Infant Health
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> ICD Code Names/Labels Inconsistently Provided
In cases where ICD codes are provided, corresponding names/labels are sometimes not provided. This is a known issue to be fixed in future releases. In the meantime, users can consider existing packages to merge ICD labels in [Stata](https://www.stata.com/features/overview/icd/), [SAS](https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp), or [R](https://www.rdocumentation.org/packages/icd/versions/3.3).       
***Expected Fix: R2.0***

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Infant Health Check 
The fields `pex_bm_healthv2_inf_00<1|2|3|4|5>__00` are 'Descriptive' fields that were erroneously inclduded and will be removed in a future release. They can be safely ignored.        
***Expected Fix: R1.1***

### Mental Health
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> APA 1/2
Individual items for Level 1 and Level 2 domains are provided, but any summary scores and corresponding T-scores (where appropriate) are not provided for any Level 2 domains. This will be corrected in a future release. In the meantime, users can calculate their own summary scores and convert them to T-scores as appropriate based on the scoring procedures provided in the [user documentation](../instruments/pregexp/mh/apa12.md). Please note for Mania, the Level 2 individual items are currently coded on a scale of 1 to 5 and will need to be recoded as 0 to 4 prior to summary score calculation. This will be corrected in a future release.   
***Expected Fix: R1.1***     

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Edinburgh Postnatal Depression Scale (EPDS)
Users should be aware that each item for the EPDS is duplicated (for example, `epds_001` and `epds_001_01`); these duplicate columns contain the same data. Duplicate data will be removed in the future.       
***Expected Fix: R1.1***

### Substance Use
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> TLFB Substance Use Flags
The TLFB Substance Use Flags are intended to indicate whether a participant had **ever met the substance-specific use criteria** during or after pregnancy across visits V01 and V02 at the time of survey administration. Currently, **only the alcohol use flag** correctly follows this logic. All other substance use flags are incorrect and will be corrected in a future release. In the meantime, use the R code provided [here](https://github.com/nbdc-datahub/hbcd-tlfb-su-flags) to derive your own substance use flag variables.         
***Expected Fix: R1.1***

## Social & Environmental Determinants
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Blank Cells in PhenX Discrimination Survey
For the PhenX+ Discrimination survey, one of the multi-select questions (column `sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*) is blank for some participants.       
***Expected Fix: R2.0***

## Visit Information
###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Invalid Participant Withdrawal Dates for Participants Who Did Not Withdraw
Participants who have “no” for `par_visit_data_participant_withdrawal` systematically have a withdrawal date of 12/26/1999 for 
`par_visit_data_participant_withdrawal_date`. Participants who have “yes” for `par_visit_data_participant_withdrawal` have a valid date and are unimpacted.             
***Expected Fix: R1.1***

###### <span class="emoji" style="color: #9d4edd;"><i class="fas fa-bug"></i></span> Missing Substance Use Flags 
The substance use flags found in the Visit Information data are single summary variables to reflect substance use status (yes/no) based on any positive reports from the (1) Timeline Follow Back (self-report), (2) Healthy History (V02) (self-report), or (3) USDTL urine toxicology results. Nail toxicology results were not used in the creation of these substance use flags. Further, the substance use flag variable is missing for alcohol, opioid, cannabis, and nicotine, and will be integrated in future data releases. In the meantime, users can generate their own substance use flag summary variables using the individual components found in the “pregnancy exposures, including substances” and “biospecimens” domains.       
***Expected Fix: R1.1***
