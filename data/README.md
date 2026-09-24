# Data

- **Source:** UCI Human Activity Recognition Using Smartphones – https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones
- **Version / download date:** UCI HAR Dataset (Anguita et al., 2012), downloaded 2026-09-24 from the UCI archive (`human+activity+recognition+using+smartphones.zip`)
- **Local path:** `data/raw/UCI HAR Dataset/` (not committed)
- **Size:** 10,299 windows (train 7,352 / test 2,947), 561 pre-computed features, 30 subjects
- **Target:** activity label, 6 classes – WALKING, WALKING_UPSTAIRS, WALKING_DOWNSTAIRS, SITTING, STANDING, LAYING
- **Split policy:** subject-aware.
  - Test = official 9 test subjects {2, 4, 9, 10, 12, 13, 18, 20, 24} – sealed until final comparison.
  - Train = official 21 train subjects {1, 3, 5, 6, 7, 8, 11, 14, 15, 16, 17, 19, 21, 22, 23, 25, 26, 27, 28, 29, 30} minus validation subjects.
  - Validation = subjects {3, 16, 22, 23} – subjects chosen once with seed 42, frozen in `src/data.py`_
- **Primary metric:** Macro-F1 (secondary: accuracy, confusion matrix)
- **Seeds:** 42
- **Leakage controls:** subject-aware split (asserted in `src/data.py`); preprocessing fitted on train only; tuning on val only, test used once at the end.
