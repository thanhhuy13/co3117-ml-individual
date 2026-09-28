# PRE-RELEASE catch-up (W01–W04)

_Date written:_ 2026-09-27 (started) - 2026-09-29 (ended)

## 1. Baseline pipeline
My baseline is logistic regression. The data is loaded with load_har() from src/data.py, which gives me a train set and a validation set (the test set is kept separate). I scale the features with StandardScaler and then train `LogisticRegression` (seed 42). On the validation set it gets Macro-F1 = 0.9322 and accuracy = 0.9279.
Code: experiments/part1_pre_midterm/baseline_logistic_regression.py.
## 2. Leakage checklist
- The data is split into a train part and a validation part; the test set is separate.
- The scaler is fitted on the train set only, and then used to transform the validation set.
- I have not used the test set yet.
## 3. Model taxonomy
- Logistic regression separates the classes with a straight line (a linear decision boundary).
- A decision tree splits the data node by node, each node testing one feature.
## 4. Train/validation-curve diagnosis
Figure: results/figures/dt_validation_curve_max_depth.png
(code: experiments/part1_pre_midterm/dt_validation_curve_max_depth.py)

From depth 1 to 3, both train and validation Macro-F1 are low, so the tree is underfitting. Validation Macro-F1 is highest at depth 4 (0.8702). After that the tree overfits: train Macro-F1 keeps going up to 1.0, but validation Macro-F1 does not go back up to 0.87. After depth 19 both lines are flat, because the full tree only has depth 19, so a larger `max_depth` changes nothing.
## 5. Decision Tree
### 5.1 Own impurity/split routine
I wrote my own entropy and information_gain functions in src/from_scratch/decision_tree.py, with tests in tests/test_decision_tree.py. My first version (commit `1a48d1d`) had two mistakes: I typed `np.log6` instead of `np.log2`, and in the information gain I used the class count arrays instead of the subset size `len(y_v)/len(y)` as the weight. Both are fixed in commit `694f411`.
### 5.2 Dissection of a full tree implementation
Reference: Erik Linder-Norén, ML-From-Scratch (branch master, accessed 2026-09-27)

| Step | Formula / idea | ML-From-Scratch | My code | Difference |
|---|---|---|---|---|
| Entropy | −Σ p log2 p | `utils/data_operation.py` L7–16 | `src/from_scratch/decision_tree.py` `entropy` | In ML-From-Scratch repo, Erik used log2 as the result of log(x)/log(2), while i used np.log2(p) directly. He also used for loop to calculate the entropy, while i used np.sum() |
| Information gain | Entropy(S) − Σ \|S_v\|/\|S\| · Entropy(S_v) | `decision_tree.py` L257–265 | `information_gain` | In ML-From-Scratch repo, because Erik used for loop to calculate entropy, so in information_gain function he just called entropy function, while i used for loop to calculate infomation gain directly |
| Best split (continuous) | test A ≥ c, pick c with max gain | `decision_tree.py` L88–124 + `utils/data_manipulation.py` L28–40 | not implemented yet | ML-From-Scratch tries every unique value as the threshold. Mitchell sorts the examples by A and only tries a threshold c between adjacent values where the class changes, then picks the c with the highest gain. |

Notes:
- Candidate thresholds: For every feature it tries every unique value as a threshold (L93–98) and splits with >= threshold (data_manipulation.py). This is correct but brute force. On UCI HAR (~5,900 unique values × 561 features per node, with list comprehensions over all samples) this is far too slow, which is why I use sklearn for the experiments.
- Pruning: It only does pre-pruning: max_depth, min_samples_split, min_impurity. There is no post-pruning or reduced-error pruning. With the defaults, the tree grows until the leaves are almost pure, so it will overfit  .
### 5.3 Stopping/pruning comparison
Code: `experiments/part1_pre_midterm/dt_pruning_comparison.py`

| Tree | Train Macro-F1 | Val Macro-F1 | Depth | Leaves |
|---|---|---|---|---|
| full tree | 1.0000 | 0.8136 | 19 | 143 |
| max_depth=4 | 0.8931 | 0.8702 | 4 | 9 |
| min_samples_leaf=20 | 0.9610 | 0.8476 | 10 | 61 |
| ccp_alpha=0.005 | 0.9385 | 0.8832 | 7 | 15 |

The ccp_alpha tree is the best on the validation set (0.8832). All four trees are still worse than logistic regression (0.9322). CCP achieved the highest validation score in this run, which aligns with post-pruning theory. However, the difference is smaller than the variance in validation scores, and the hyperparameter tuning across methods wasn't entirely fair, so CCP cannot be definitively declared the best option.
## 6. Reflection
My handwritten diagnostic and its corrections are in exercises/Release_baseline_diagnostic_w01_04.pdf and exercises/Release_baseline_W01_04_corrections.md. I got entropy, information gain and boolean trees right. My main gaps were: the formal definition of overfitting and where it starts, the details of reduced-error pruning, continuous attributes (I confused them with regression trees), missing values, and that logistic regression is still a linear classifier. The experiments in this catch-up helped me see where overfitting starts on my own data.