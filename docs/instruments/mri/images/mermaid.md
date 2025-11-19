---
config:
  layout: elk
  look: neo
  theme: redux
---
flowchart LR
    n1(["<b>V02</b>"]) --> n3["<b>BIBSNet</b><br>"] & n10["<b>BIBSNet</b><br>"]
    n3 --> n4["bibsnet/"]
    n4 --> n5@{ label: "<b>Infant fMRIPrep<br></b><i style=\"--tw-scale-x:\">M-CRIB-S surf recon</i>" }
    n5 --> n6["nibabies-0f306a2f/<br>mcribs-0f306a2f/<br>freesurfer-0f306a2f/"]
    n6 --> n7["<b>XCP-D</b><br>"]
    n7 --> n8["xcp_d-0f306a2f+0ef9c88a/"]
    n9(["<b>V03 &amp; V04</b>"]) --> n10
    n10 --> n11["bibsnet/"]
    n11 --> n12@{ label: "<b>Infant fMRIPrep<br></b><i style=\"--tw-scale-x:\"><span style=\"--tw-scale-x:\">Infant FS surf recon</span></i>" }
    n12 --> n13["nibabies-2afa9081/<br>freesurfer-2afa9081/"]
    n13 --> n14["<b>XCP-D</b><br>"]
    n14 --> n15["xcp_d-2afa9081+0ef9c88a/"]
    n3@{ shape: rounded}
    n10@{ shape: rounded}
    n4@{ shape: text}
    n5@{ shape: rounded}
    n6@{ shape: text}
    n7@{ shape: rounded}
    n8@{ shape: text}
    n11@{ shape: text}
    n12@{ shape: rounded}
    n13@{ shape: text}
    n14@{ shape: rounded}
    n15@{ shape: text}
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#FFCDD2,stroke:#D50000
    style n10 fill:#FFCDD2,stroke:#D50000
    style n4 color:#2962FF
    style n5 fill:#FFCDD2,stroke:#D50000
    style n6 color:#2962FF
    style n7 fill:#FFCDD2,stroke:#D50000
    style n8 color:#2962FF
    style n9 fill:#E1BEE7,stroke:#AA00FF
    style n11 color:#2962FF
    style n12 fill:#FFCDD2,stroke:#D50000
    style n13 color:#2962FF
    style n14 fill:#FFCDD2,stroke:#D50000
    style n15 color:#2962FF
