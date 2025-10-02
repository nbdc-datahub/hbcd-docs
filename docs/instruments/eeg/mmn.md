# Auditory Mismatch Negativity Task 

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">
    Additional Resources
  </span>
</div>
<div class="notification-static-content">
<p> 
• <a href="..">Overview & EEG Protocols</a><br>
• <a href="../qc">Quality Control Procedures</a><br>
</p>
</div>
<p></p>

<p>
<div id="warning" class="warning-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-exclamation-triangle"></i></span>
  <span class="text-with-link">
  <span class="text">Data Warning</span>
  <a class="anchor-link" href="#warning" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="warning-collapsible-content">
<p>The interstimulus interval (ISI) for the Auditory Mismatch Negativity task changed between visits V03 and V04/V06 - see <a href="https://doi.org/10.1016/j.dcn.2024.101447">Fox et al. 2024</a> and <a href="https://doi.org/10.1097/00003446-200204000-00005">Morr et al. 2002</a> for details.</p>
</div>
</p>
 
The Auditory mismatch negativity (**MMN**) Task (v.11.29.23) facilitates examining auditory evoked potentials and habituation/dishabituation to auditory stimuli. The MMN captures differences in neural responses to standard (“ba”) and deviant (“da”) stimuli. From this task the MMN difference wave is computed, which is also known as the Mismatch Response (MMR). The amplitude/latency of this difference wave has been linked to language ([Choudhury & Benasich, 2011](https://doi.org/10.1016/j.clinph.2010.05.035)), temperament/personality ([Gurrera et al., 2001](https://doi.org/10.1016/S0006-3223(00)01067-2); [Marshall et al., 2009](https://doi.org/10.1111/j.1467-7687.2008.00808.x)), internalizing problems ([Reeb-Sutherland et al., 2009](https://doi.org/10.1111/j.1469-7610.2009.02170.x)), externalizing/attention problems ([Gumenyuk et al., 2005](https://doi.org/10.1016/j.neulet.2004.10.081)), and disorders including autism ([Lepistö et al., 2005](https://doi.org/10.1016/j.brainres.2005.10.052); [Schwartz et al., 2018](https://doi.org/10.1016/j.neubiorev.2018.01.008)) and reading ability/dyslexia ([Leppänen et al., 2010](https://doi.org/10.1016/j.cortex.2010.06.003); [Norton, Beach, et al., 2021](https://doi.org/10.3389/fnhum.2021.624617)). See [Fox et al. (2024)](https://doi.org/10.1016/j.dcn.2024.101447) for more information about the MMN task.

## Task Details

Standard ("ba") and deviant ("da") auditory stimuli are presented while a video is played on an iPad to serve as a visual distractor (brightness set to maximum, in airplane mode, and unplugged). The task may be paused if breaks are needed. The `.wav` files for the auditory stimuli are 196 ms long for the “ba” stimulus and 198 ms long for the “da” stimulus.

<ul>
<strong>Trial Count:</strong>
<li>Standard condition: 569</li>
<li>Deviant condition: 98 </li>
<li>Total: 667</li>
</ul>

<ul>
<strong>Timing Details:</strong>
<li>Stimulus duration: 200 ms</li>
<li>InterStimulus interval: 820 ms (V03), 600 ms (V04/V06)</li>
<li>Total trial length: 1020 ms (V03), 800 ms (V04/V06)</li>
</ul>

A schematic of the trial progression for Visit 3 is below. See [HBCD Study Protocols - EEG](https://hbcdstudy.org/wp-content/uploads/2023/06/EEG-Parameters.pdf) for additional details.
<img src="../images/MMN.png" width="100%" height="auto" class="center">

## Resources
- [HBCD EEG Utilities](https://hbcd-eeg-utilities.readthedocs.io/)
- [HBCD E-Prime Task Manual](https://docs.google.com/document/d/1PghQQpLbxjQavtVlHyIz7JVJxlyKcC4Do8z8j7srdaI/edit?usp=sharing)
- [HBCD EEG Acquisition Protocol](https://zenodo.org/records/14795030)


### References

<div class="references">
  <p>Choudhury, N., & Benasich, A. A. (2011). Maturation of auditory evoked potentials from 6 to 48 months: Prediction to 3 and 4 year language and cognitive abilities. <i>Clinical Neurophysiology</i>, 122(2), 320–338. <a href="https://doi.org/10.1016/j.clinph.2010.05.035" target="_blank">https://doi.org/10.1016/j.clinph.2010.05.035</a></p>
  <p>Fox, N. A., Pérez-Edgar, K., Morales, S., Brito, N. H., Campbell, A. M., Cavanagh, J. F., Gabard-Durnam, L. J., Hudac, C. M., Key, A. P., Larson-Prior, L. J., Pedapati, E. V., Norton, E. S., Reetzke, R., Roberts, T. P., Rutter, T. M., Scott, L. S., Shuffrey, L. C., Antúnez, M., Boylan, M. R., … Yoder, L. (2024). The development and structure of the Healthy Brain and Child Development (HBCD) study EEG Protocol. <i>Developmental Cognitive Neuroscience</i>, 69, 101447. <a href="https://doi.org/10.1016/j.dcn.2024.101447" target="_blank">https://doi.org/10.1016/j.dcn.2024.101447</a></p> 
  <p>Gumenyuk, V., Korzyukov, O., Escera, C., Hämäläinen, M., Huotilainen, M., Häyrinen, T., Oksanen, H., Näätänen, R., Von Wendt, L., & Alho, K. (2005). Electrophysiological evidence of enhanced distractibility in ADHD children. <i>Neuroscience Letters</i>, 374(3), 212–217. <a href="https://doi.org/10.1016/j.neulet.2004.10.081" target="_blank">https://doi.org/10.1016/j.neulet.2004.10.081</a></p>
  <p>Gurrera, R. J., O’Donnell, B. F., Nestor, P. G., Gainski, J., & McCarley, R. W. (2001). The P3 auditory event–related brain potential indexes major personality traits. <i>Biological Psychiatry</i>, 49(11), 922–929. <a href="https://doi.org/10.1016/S0006-3223(00)01067-2" target="_blank">https://doi.org/10.1016/S0006-3223(00)01067-2</a></p>
  <p>Lachmann, T., Berti, S., Kujala, T., & Schröger, E. (2005). Diagnostic subgroups of developmental dyslexia have different deficits in neural processing of tones and phonemes. <i>International Journal of Psychophysiology</i>, 55(2), 105–120. <a href="https://doi.org/10.1016/j.ijpsycho.2004.11.005" target="_blank">https://doi.org/10.1016/j.ijpsycho.2004.11.005</a></p>
  <p>Lepistö, T., Kujala, T., Vanhala, R., Alku, P., Huotilainen, M., & Näätänen, R. (2005). The discrimination of and orienting to speech and non-speech sounds in children with autism. <i>Brain Research</i>, 1066(1–2), 147–157. <a href="https://doi.org/10.1016/j.brainres.2005.10.052" target="_blank">https://doi.org/10.1016/j.brainres.2005.10.052</a></p>
  <p>Leppänen, P. H., Hämäläinen, J. A., Salminen, H. K., Eklund, K. M., Guttorm, T. K., Lohvansuu, K., Puolakanaho, A., & Lyytinen, H. (2010). Newborn brain event-related potentials revealing atypical processing of sound frequency and the subsequent association with later literacy skills in children with familial dyslexia. <i>Cortex</i>, 46(10), 1362–1376. <a href="https://doi.org/10.1016/j.cortex.2010.06.003" target="_blank">https://doi.org/10.1016/j.cortex.2010.06.003</a></p>
  <p>Marshall, P. J., Reeb, B. C., & Fox, N. A. (2009). Electrophysiological responses to auditory novelty in temperamentally different 9-month-old infants. <i>Developmental Science</i>, 12(4), 568–582. <a href="https://doi.org/10.1111/j.1467-7687.2008.00808.x" target="_blank">https://doi.org/10.1111/j.1467-7687.2008.00808.x</a></p>
  <p>Morr, M. L., Shafer, V. L., Kreuzer, J. A., & Kurtzberg, D. (2002). Maturation of mismatch negativity in typically developing infants and preschool children. <i>Ear and Hearing</i>, 23(2), 118–136. <a href="https://doi.org/10.1097/00003446-200204000-00005" target="_blank">https://doi.org/10.1097/00003446-200204000-00005</a></p>
  <p>Norton, E. S., Beach, S. D., Eddy, M. D., McWeeny, S., Ozernov-Palchik, O., Gaab, N., & Gabrieli, J. D. (2021). ERP mismatch negativity amplitude and asymmetry reflect phonological and rapid automatized naming skills in English-speaking kindergartners. <i>Frontiers in Human Neuroscience</i>, 15, 624617. <a href="https://doi.org/10.3389/fnhum.2021.624617" target="_blank">https://doi.org/10.3389/fnhum.2021.624617</a></p>
  <p>Reeb-Sutherland, B. C., Vanderwert, R. E., Degnan, K. A., Marshall, P. J., Pérez-Edgar, K., Chronis-Tuscano, A., Pine, D. S., & Fox, N. A. (2009). Attention to novelty in behaviorally inhibited adolescents moderates risk for anxiety. <i>Journal of Child Psychology and Psychiatry</i>, 50(11), 1365–1372. <a href="https://doi.org/10.1111/j.1469-7610.2009.02170.x" target="_blank">https://doi.org/10.1111/j.1469-7610.2009.02170.x</a></p>
  <p>Schwartz, S., Shinn-Cunningham, B., & Tager-Flusberg, H. (2018). Meta-analysis and systematic review of the literature characterizing auditory mismatch negativity in individuals with autism. <i>Neuroscience & Biobehavioral Reviews</i>, 87, 106–117. <a href="https://doi.org/10.1016/j.neubiorev.2018.01.008" target="_blank">https://doi.org/10.1016/j.neubiorev.2018.01.008</a></p>
</div>
<br>

