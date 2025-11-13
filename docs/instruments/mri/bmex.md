

This analysis examined two key questions:
Whether the BME-X Quality Index (QI) metric aligns with manual QC scores (both original QC (QU_motion) and enhanced image score (Enhanced_image_score_v2).

Enhanced_Image_Score_v2: manual QC after enhancement
QU_motion: manual QC for original images
QI_from_BMEX: automatic continuous quality metric

BME-X QI values were continuous scores ranging approximately from 0 to 2, where higher values indicate poorer image quality (e.g., 0 = best, >2 = worse quality or instability).

## BME-X

### Manual QC Ratings Pre- and Post-Enhancement
Manual QC ratings were coded numerically: Excellent = 0, Good = 1, Questionable = 2, Unusable = 3. Manual QC ratings are significantly improved following BME-X enhancement (paired T-test, t=-4.25, p < 0.001).

<img src="../images/bme-x.png" width="50%" height="auto" class="center">

Interestingly, the BME-X Quality Index (QI) showed no significant correlation with the enhanced manual QC scores (ρ=0.02, p=0.78) and a significant, but weak (R² < 0.03) negative correlation with original manual QC scores prior to enhancement (ρ = −0.21, p < 0.001), meaning slightly higher QI values were linked with better-rated original images. The overall strength of this relationship was small (R² < 0.03), indicating that QI is not a reliable predictor of human QC ratings.

