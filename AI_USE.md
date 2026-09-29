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

## W05 - 2026-09-28
### 1. What to read for overfitting and pruning
- **Question:** Which parts of Mitchell and Müller do I need for the decision tree curve and the pruning comparison?
- **Before AI:** my handwritten diagnostic (`d31049a`) showed gaps in overfitting, pruning and continuous attributes.
- **Tool / purpose:** Claude, asked for a reading list; after reading, asked it to summarise Mitchell Ch. 3 (§3.2–§3.7.2) into revision notes for my exam notebook (kept outside the repo).
- **What I got:** section and page numbers in both books, and a short summary of Ch. 3.
- **Checked against:** I read Mitchell (1997) §3.2–§3.7.2 myself, and Müller & Guido (2017) pp. 26–29 and 70–77.
- **What changed:** I understood the formal definition of overfitting, pre- vs post-pruning, reduced-error pruning, and how thresholds are chosen for continuous attributes.
- **Can I redo it without AI:** yes.

### 2. Decision tree validation curve (`dt_validation_curve_max_depth.py`)
- **Question:** How do I find where the tree starts to overfit on my data?
- **Before AI:** I wrote and ran a single tree with max_depth=3 myself (`d0dcacb`).
- **Tool / purpose:** Claude, asked what a validation curve is and how the Python syntax works (for loop, list append, zip, matplotlib), explained with unrelated examples. I wrote the code myself.
- **What I got:** the idea of the curve and syntax examples; after I ran it, bug hints: my print loop printed the last depth 20 times, the figure name ended with `.png.png`, and the axis labels should say max_depth and Macro-F1.
- **Checked against:** Mitchell (1997) Fig. 3.6 and Müller & Guido (2017) p. 29.
- **What changed:** fixed the bugs (`7c6357b`). I learned that my plot uses max_depth and Macro-F1 instead of the number of nodes and accuracy like Fig. 3.6, and why the curve is flat after depth 19.
- **Can I redo it without AI:** yes.

## W05 - 2026-09-28/29

### 1. Catch-up post
- **Question:** What should go into each section of the catch-up?
- **Before AI:** my results, my diagnostic corrections file.
- **Tool / purpose:** Claude, used to explain what each section needs and based on it i wrote catch-up myself.
- **What I got:** A recommendation topic from AI.
- **What changed:** I depended on the recommendation and wrote catch-up.
- **Can I redo it without AI:** Yes; I can explain every section.

### 2.Progress dashboard
- **Question:**What links does PROGRESS.md need?
- **Before AI:** my experiment outputs.
- **Tool / purpose:** Claude, used to fill in the links in PROGRESS.md.
- **What I got:* the W01–W04 links in PROGRESS.md.
- **Checked against:** I clicked every link.
- **What changed:** dashboard (`7c08f35`).
- **Can I redo it without AI:** yes.

## W05 - 2026-09-29 (Perceptron)

### 1. Drill question set
- **Question:** Which questions should the W05 drill cover?
- **Before AI:** nothing.
- **Tool / purpose:** Claude, used to build the question set (no answers): three self-made questions. Explained the answer of each questions after i did correction based on Mitchell, Machine Learning (1997) by myself.
- **What I got:** the question list.
- **Checked against:** the spec's W05 drill topics.
- **What changed:** I did the drill closed-book and then wrote corrections from the book. Claude only help me explain and recheck the answer .
- **Can I redo it without AI:** yes.

### 2 Perceptron tests and experiment
- **Question:** How do I test perceptron, and compare it with sklearn on HAR?
- **Before AI:** I wrote `perceptron_predict` and `perceptron_fit` from the book (`6093eb1`) and the one-vs-rest code myself.
- **Tool / purpose:** Claude, used for the recommendation where test code and experiment code should live, sklearn's default settings, and bug.
- **What I got:** bug: my first experiment loaded the official test set (moved to `load_har()` and val before committing), wrong module name and unpacking in the experiment (`73f7fe8`), the syntax example pasted into `perceptron_fit`, and `epochs`/`shuffle` passed in the wrong positions. Also guiding questions on why shuffle and epochs matter.
- **Checked against:** my unit tests (AND learned 4/4, XOR < 1), sklearn `Perceptron` on the same split, Mitchell §4.4.2.
- **What changed:** added a shuffle option (`e2ede4d`) and the epochs/shuffle comparison (`5a2ea17`).
- **Other AI used:** None
- **Can I redo it without AI:** yes.

