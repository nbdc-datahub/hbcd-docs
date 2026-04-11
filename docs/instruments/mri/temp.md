# MR Raw BIDS

## Overview

**This page describes:**

* How raw MR data are converted to BIDS
* What files are included in each BIDS subfolder
* How to interpret file naming and structure

➡️ Use this page as a **reference** when navigating raw imaging data.


---

<div class="table-banner">
<i class="fa fa-circle-info"></i>
<span>New to file trees? <a href="../../../datacuration/overview/#filetrees" target="_blank">How to read them →</a></span>
</div>


---

## Anatomical (`anat/`)

**Includes:**

* T1-weighted (T1w) images
* T2-weighted (T2w) images
* QALAS (`inv-0` → `inv-4`)
* MRS localizers (`aqc-mrsLocAx`, `aqc-mrsLocCor`)

**All files include sidecar JSON metadata.**

```bash
hbcd/
└── rawdata/
    └── sub-{ID}/
        └── ses-{V0X}/
            └── anat/
                # Structural MRI
                ├── *_T1w.nii.gz
                ├── *_T2w.nii.gz

                # Quantitative MRI
                ├── *_acq-mrsLocAx_T2w.nii.gz
                ├── *_acq-mrsLocCor_T2w.nii.gz
                └── *_inv-<0–4>_QALAS.nii.gz
```

---

## Functional (`func/`) & Fieldmaps (`fmap/`)

**Includes:**

* Resting-state BOLD runs (`func/`)
* EPI fieldmaps in AP/PA directions (`fmap/`)
* B1+ fieldmaps (vendor-dependent)

**Notes:**

* Each BOLD run is associated with a pair of fieldmaps (AP/PA)
* B1 acquisition methods vary by vendor (see qMRI documentation)

```bash
hbcd/
└── rawdata/
    └── sub-{ID}/
        └── ses-{V0X}/
            ├── func/
            │   └── *_task-rest_dir-PA_run-{X}_bold.nii.gz
            │
            └── fmap/
                ├── *_dir-<AP|PA>_run-{X}_epi.nii.gz
                ├── *_acq-anat_run-{X}_TB1TFL.nii.gz   # Siemens
                └── *_acq-<tr1|tr2>_run-{X}_TB1AFI.nii.gz  # GE / Philips
```

---

## Diffusion (`dwi/`)

**Includes:**

* DWI volumes (`*_dwi.nii.gz`)
* Gradient magnitudes (`.bval`)
* Gradient directions (`.bvec`)
* Single-band reference images (`*_sbref.nii.gz`)

All acquisitions are collected in **AP and PA phase encoding directions**.

```bash
hbcd/
└── rawdata/
    └── sub-{ID}/
        └── ses-{V0X}/
            └── dwi/
                ├── *_dir-<AP|PA>_run-{X}_dwi.nii.gz
                ├── *_dir-<AP|PA>_run-{X}_dwi.bval
                ├── *_dir-<AP|PA>_run-{X}_dwi.bvec
                └── *_dir-<AP|PA>_run-{X}_sbref.nii.gz
```

---

## MRS (`mrs/`)

**Includes:**

* Metabolite spectra (`*_svs.nii.gz`)
* Water reference scans (`*_ref.nii.gz`)

**Acquisition types:**

* Short echo time (`acq-shortTE`, TE = 35 ms)
* HERCULES edited spectra (`acq-hercules`, TE = 80 ms)

**Notes:**

* Dimension 5: coil elements
* Dimension 6: transients

```bash
hbcd/
└── rawdata/
    └── sub-{ID}/
        └── ses-{V0X}/
            └── mrs/
                ├── *_acq-shortTE_run-{X}_svs.nii.gz
                ├── *_acq-shortTE_run-{X}_ref.nii.gz
                ├── *_acq-hercules_run-{X}_svs.nii.gz
                └── *_acq-hercules_run-{X}_ref.nii.gz
```
