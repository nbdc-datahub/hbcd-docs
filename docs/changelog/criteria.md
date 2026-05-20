# Population & Exclusion Criteria

## Participant Population

HBCD enrolls at least 25% of participants who have more than minimal substance use during pregnancy, including opioids ([Si et al. 2024](https://doi.org/10.1016/j.dcn.2024.101432)). In addition, HBCD enrollment strategies aimed at yielding a study population that is representative of the individual and geographic characteristics of reproductive-aged women in the United States who had a birth in the past 12 months, and include an adequate comparison group for substance exposed individuals ([Nelson et al. 2024](https://doi.org/10.1016/j.dcn.2024.101441)). There are siblings enrolled in HBCD, some of whom are twins or triplets (multiples). IDs for multiples are provided in the *HBCD Private Release Notes* - see <a href="../../instruments/demo/visitinfo/#multiple-birth-participants" target="_blank">Multiple Birth Participants</a> under Visit Information for details.

##  Exclusion Criteria & Filters

### Participants & Participant Information

- Visit data collected prior to the January 2026 data freeze are excluded from Release 2.X data 
 <!-- Excluded visits with 'LaunchPad Complete' Status set to 'Complete' after 2026-01-XX -->
- Participants with no brain rating or brain rating noted as "atypical" excluded
- Inactive participants/sessions excluded
- Sex is set to 'Other' for participants with only one active Visit 1 (V01) visit
- 'Candidate_Age' values are replaced with 'n/a' for Visit 1 (V01)
<!-- - Excluded visits with 'LaunchPad Complete' Status set to 'Complete' after 2024-07-01 -->

### Instrument & Field Exclusions

- ERICA forms — `mh_cg_erica_{fcm_adm_}{3_7m|7_9m}`  
- GABI Setup/Receipt — `nt_pa_gabi_{setup|rcpt}`    
- MRI Data & Scan Summary Forms (pre/post scan prep) — `mri_ra_chkl_{data|scan}`  
- NIH Baby ToolBox — `ncl_ch_nbtb`
- Participant / RA Feedback — `adm_cg_fb` / `adm_ra_fb`    
- Urgent Events & Participant Alerts — `adm_fd_urgent` / `admin_alert`
- Fields including *examiner*, *REDCap Complete status*, *timestamps*, *visit stage*, and *visit start*
