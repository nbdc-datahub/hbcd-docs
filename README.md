Docs website for HEALthy Brain and Child Development (HBCD) Study Data Release documentation: [https://docs.hbcdstudy.org](https://docs.hbcdstudy.org).


## Current workflow for parsing tables from google sheets and airtable

Either use the scripts under `/scripts` or the following in the root directory:

`python3 autoparse-all.py`

this script:

- pulls all info for static and dynamic tables from google sheets
- pulls all Airtable instrument info


The relevant pages are then updated automatically via macros

FUTURE TO DO: make autoparsing happen on build (likely need to clean things up to be more efficient otherwise will go over API call budget on Airtable), e.g. in `.readthedocs.yaml`:

```
build:
  os: ubuntu-24.04
  tools:
    python: "3.13"
  jobs:
    pre_build:
      - python autoparse-all.py
```

