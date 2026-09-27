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

## W05 - 2026-09-25
### 1. Diagnostic questions and Q1 explanation
- **Question:** Which exercises should I use for the release diagnostic?
- **Before AI:** the handwritten diagnostic was done closed-book.
- **Tool / purpose:** Claude, used to write the self-made questions (no answers). After the attempt, asked it to explain questions.
- **What I got:** a list of exercises and question prompts; after the attempt, an explanation of the answer of each question.
- **Checked against:** Mitchell (1997), Section 3.4.1.
- **What changed:** I understood that entropy is always computed on the class labels, and the attribute is only used to split. And my knowledge about foundations is enhanced.
- **Can I redo it without AI:** yes.

## W05 - 2026-09-27
### 1. Entropy and information gain testcase
- **Question:** Which usecase should I use to test entropy and gain info function?
- **Before AI:** I coded entropy and information_gain myself and committed.
- **Tool / purpose:** Claude, used to learn the NumPy, point out bugs in my code, and write the test file..
- **What I got:** syntax explanations; bug hints (log6p → np.log2(p), weight must be |S_v|/|S| instead of per-label counts); recommends usecase that i used.
- **Checked against:** my hand calculation of Mitchell Ex. 3.2 (entropy = 1, gain(a2) = 0, gain(a1) ≈ 0.0817); `scipy.stats.entropy` and `sklearn.metrics.mutual_info_score` on UCI HAR (the tests pass); Mitchell (1997), Section 3.4.1.
- **What changed:** fixed my entropy (use np.log2(p)). In information_gain, I changed the weight from `count_y_v / count_y` to `len(y_v) / len(y)`, because the weight is the group size over the total, not a per-label ratio. I also learned that v is a value of the attribute, not a label, and that continuous HAR features need a threshold (x < c) first.
- **Can I redo it without AI:** yes.