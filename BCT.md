# Brain CT Triage

## Overview

You are given **68 brain CT series**, each stored in its own directory.
Every directory represents one complete CT series made up of multiple DICOM slices.

---

## Data Structure

Each folder corresponds to a single CT series:

```
.
├── series_0
│   ├── slice0.dcm
│   ├── ...
│   └── slicen.dcm
├── series_1
│   ├── file0.dcm
│   ├── ...
│   └── filen.dcm
├── ...
└── series_n
```

Each directory contains all slices required to reconstruct and analyze that series.

---

## Submission Format

After implementing your solution in `submission.py`, generate predictions by running:

```bash
python submission.py --data-dir /path/to/data-dir --predictions-file-path /path/to/submission.csv
```

Once the script finishes, it should create:

```
submission.csv
```

### CSV Example

```csv
series_id,V_EDH,V_SDH,V_IPH,V_SAH,V_IVH,fracture_prob,MLS_mm
series_0,0.11,0.9,0.92,0.71,0.67,0.23,2.15
series_1,0.13,0.3,0.31,0.7,0.67,0.01,2.3
...
series_n,0.41,0.2,0.89,0.51,0.67,0.15,0.26
```

### Same Example as a Table

| series_id | V_EDH | V_SDH | V_IPH | V_SAH | V_IVH | fracture_prob | MLS_mm |
| --------- | ----- | ----- | ----- | ----- | ----- | ------------- | ------ |
| series_0  | 0.11  | 0.90  | 0.92  | 0.71  | 0.67  | 0.23          | 2.15   |
| series_1  | 0.13  | 0.30  | 0.31  | 0.70  | 0.67  | 0.01          | 2.30   |
| ...       | ...   | ...   | ...   | ...   | ...   | ...           | ...    |
| series_n  | 0.41  | 0.20  | 0.89  | 0.51  | 0.67  | 0.15          | 0.26   |
