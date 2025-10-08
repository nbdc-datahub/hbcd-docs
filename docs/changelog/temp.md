




## 🌍 Social & Environmental Determinants

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>Blank Cells in PhenX Discrimination Survey</b> <span class="badge" style="background-color:#f59e0b; color:white;">Fix: R2.0</span></summary>

For the PhenX+ Discrimination survey, the multi-select question  
(`sed_bm_phx__discr.006`: *"What do you think is the main reason for these experiences? If more than one main reason, check all that apply."*)  
is blank for some participants. This will be corrected in R2.0.

</details>

---

## 📅 Visit Information

<details>
<summary><span style="color:#f97316;"><i class="fas fa-bug"></i></span> <b>Invalid Participant Withdrawal Dates</b> <span class="badge" style="background-color:#9ca3af; color:white;">Expected Fix: TBD</span></summary>

Participants who did **not** withdraw from the study (value = “no” for `par_visit_data_participant_withdrawal`) have a sentinel value of `12/26/1999` in `par_visit_data_participant_withdrawal_date`.  
This indicates *no withdrawal* and can be safely ignored.  

Participants who withdrew (value = “yes”) have valid withdrawal dates and are unaffected.

</details>
