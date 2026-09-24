# AI use log

## W05 – 2026-09-24

### 1. Understanding the assignment
- **Question:** What exactly do I need to hand in, and when? The spec mixes W03/W05 numbering and I wasn't sure what R0 meant.
- **Before AI:** nothing (setup week).
- **Tool / purpose:** Claude, asked it to explain the spec.
- **What I got:** a summary of R0, Part I / Part II deadlines and the weekly workflow.
- **Checked against:** the spec itself (sections 1.2, 5, 10).
- **What changed:** I made a checklist for R0 and W05.
- **Can I redo it without AI:** yes.

### 2. Repository skeleton
- **Question:** How should the repo be laid out?
- **Before AI:** nothing (setup week).
- **Tool / purpose:** Claude, used to create the folders and empty template files from section 5.
- **What I got:** the folder structure and blank templates (README, PROGRESS, MODEL_LOG, SUBMISSION files, weekly post template).
- **Checked against:** the tree in section 5 of the spec.
- **What changed:** the repo now has the required structure. I fill in the content myself.
- **Can I redo it without AI:** yes.

### 3. Loading UCI HAR and the subject split (`src/data.py`)
- **Question:** How do I split the data so the same person never ends up in both train and test?
- **Before AI:** nothing. 
- **Tool / purpose:** Claude, used to write the loading and split code.
- **What I got:** the code for `src/data.py`. It uses `np.isin` on subject IDs to move whole subjects into validation, and asserts that no subject appears in two splits.
- **Checked against:** I ran the script: 7352 train / 2947 test windows, 561 features, and no overlapping subjects. I also read the dataset's `README.txt`.
- **What changed:** I froze the validation subjects as `[3, 16, 22, 23]`.
- **Can I redo it without AI:** yes.
