
<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

### 2.1 Resolved Known Issues







<!-- BIOSPEC -->
<tr>
<td>BIO</td>
<td>Nails</td>
<td><i class="fas fa-bug icon-bug"></i>  Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
</tr>

<tr>
<td>BIO</td>
<td>Urine</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>  Add creatinine results (<code>bio_creat_u</code>).</td>
</tr>

<tr>
<td>BIO</td>
<td>Nails & Urine</td>
<td><i class="fas fa-bug icon-bug"></i>  Remove quotes from level values to prevent double quotes in downloaded data (e.g. 1=""positive"").</td>
</tr>

<tr>
<td>BIO</td>
<td>Olink</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>  Addition of Olink Explore 384 Inflammation 1 Panel, proteomics measure of maternal inflammation during pregnancy</td>
</tr>

<!-- DEMO -->
<tr>
<td>Demo</td>
<td>Visit Info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> SU flags will include Nail toxicology results in addition to Urine.</td>
</tr>

<tr>
<td>Demo</td>
<td>.set files</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> 
Add <code>work_{002–004}_post</code> and <code>work_004__01</code> (adult table).
</td>
</tr>

<!-- EEG -->
<tr>
<td>EEG</td>
<td>MADE</td>
<td><i class="fas fa-bug icon-bug"></i>  N=3 V04 session derivatives are missing corresponding tabulated data for FACE/MMN tasks</td>
</tr>
<tr>
<td>EEG</td>
<td>.set files</td>
<td><i class="fas fa-bug icon-bug"></i>  Update EEG .set files to include subject release IDs.</td>
</tr>

<!-- MRI -->
<tr>
<td>MRI</td>
<td>Summary Forms</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fa-solid fa-rotate icon-rotate"></i>  Add MRI Scan Session + Data Summary Forms (information from the MRI technician obtained on day of scan).</td>
</tr>

<tr>
<td>MRI</td>
<td>BrainSwipes</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fa-solid fa-rotate icon-rotate"></i>   BrainSwipes QC results updated with latest results available in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
</tr>

<tr>
<td>MRI</td>
<td>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug icon-bug"></i>  Metadata values for <code>sub_domain</code> were corrected to <code>Structural MRI</code> for tabulated XCP-D Myers-Labonte <code>*morph.tsv</code> files.</td>
</tr>

<tr>
<td>MRI</td>
<td>Raw BIDS</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug icon-bug"></i>  Resolved 2 corrupted bold runs in V02 raw BIDS (see filepaths in <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>).</td>
</tr>

<!-- NCL -->
<tr>
<td>NCL</td>
<td>Bayley-4</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add item-level scores.</td>
</tr>
<tr>
<td>NCL</td>
<td>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug icon-bug"></i>  Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "Â Â Â")</td>
</tr>

<tr>
<td>NCL</td>
<td>Vineland</td>
<td><i class="fas fa-bug icon-bug"></i>  Correct subset of variables with typo in the spelling of "receptive."<br>
<i class="fa-solid fa-rotate icon-rotate"></i>   Addition of language field to <code>ncl_cg_vabs</code>.</td>
</tr>

<!-- PH -->
<tr>
<td>PH</td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>
  <i class="fas fa-bug icon-bug"></i> Remove <code>ph_ch_anthro_002</code><br>
  <i class="fa-solid fa-rotate icon-rotate"></i>  Add age-based z-scores to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Z-Scores Excluded</a>).
</td>
</tr>

<!-- SED -->
<tr>
<td>SED</td>
<td>C-PACEs</td>
<td><i class="fas fa-bug icon-bug"></i>  Summary scores are inaccurate; until corrected, users can compute scores following the provided scoring documentation.</td>
</tr>

<tr>
<td>SED</td>
<td>Demographics</td>
<td>
  <i class="fa-solid fa-rotate icon-rotate"></i>  Add variables on Other Biological Parent (adult table).
  <br>
  <i class="fa-solid fa-rotate icon-rotate"></i>  
Add V01 household income (<code>income_002</code>) (adult table)
<br>
<i class="fas fa-bug icon-bug"></i>  Remove descriptive fields (e.g. <code>roster_001__00</code>) <em>[BR data only]</em>.
</td>
</tr>

<tr>
<td>SED</td>
<td>Demographics</td>
<td><i class="fas fa-bug icon-bug"></i>  Add back <code>sed_bm_demo_residence_{001|002}</code> (present in prior release then missing).<br>
<i class="fa-solid fa-rotate icon-rotate"></i>  Child Demo: Household roster updated to clarify that counts exclude the main child.
</td>
</tr>

</tbody>
</table>

</body>
</html>
