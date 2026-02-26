# Speaker Identification

## Overview

You are given **3,604 audio files**.
Each file contains a short speech segment:
All audio files are provided in a single directory:

```
.
├── e9105299-285b-4df7-8c66-e4b3b721e8c8.mp3
├── 016a2324-dc96-4f59-8d96-fb387afb1fff.mp3
├── 57e9178b-7153-4e43-8fe4-6aacea3c9118.mp3
├── ...
└── ef43d054-a0a8-4ce3-9362-498cf58093b2.mp3
```
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

Each row should map an `audio_file` to a predicted `speaker_id`.

If the speaker cannot be confidently identified, you may assign:

```
unknown
```

### Example CSV format

```csv
audio_file,speaker_id
e9105299-285b-4df7-8c66-e4b3b721e8c8.mp3,3943d8f3-d820-44ff-aba6-23c796fda87b
016a2324-dc96-4f59-8d96-fb387afb1fff.mp3,845cbfc6-af92-4fa0-8b33-4e4e0e3b002a
57e9178b-7153-4e43-8fe4-6aacea3c9118.mp3,unknown
ef43d054-a0a8-4ce3-9362-498cf58093b2.mp3,6531a140-1e3f-40f4-b3be-7871fed19a85
```

### Same example as a table

| audio_file                               | speaker_id                           |
| ---------------------------------------- | ------------------------------------ |
| e9105299-285b-4df7-8c66-e4b3b721e8c8.mp3 | 3943d8f3-d820-44ff-aba6-23c796fda87b |
| 016a2324-dc96-4f59-8d96-fb387afb1fff.mp3 | 845cbfc6-af92-4fa0-8b33-4e4e0e3b002a |
| 57e9178b-7153-4e43-8fe4-6aacea3c9118.mp3 | unknown                              |
| ef43d054-a0a8-4ce3-9362-498cf58093b2.mp3 | 6531a140-1e3f-40f4-b3be-7871fed19a85 |
