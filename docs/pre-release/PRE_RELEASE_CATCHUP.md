# PRE-RELEASE catch-up (W01–W04)

_Date written:_ 2026-09-27

## 1. Baseline pipeline

## 2. Leakage checklist

## 3. Model taxonomy

## 4. Train/validation-curve diagnosis

## 5. Decision Tree
### 5.1 Own impurity/split routine
### 5.2 Dissection of a full tree implementation
Reference: Erik Linder-Norén, ML-From-Scratch (branch master, accessed 2026-09-27)

| Step | Formula / idea | ML-From-Scratch | My code | Difference |
|---|---|---|---|---|
| Entropy | −Σ p log2 p | `utils/data_operation.py` L7–16 | `src/from_scratch/decision_tree.py` `entropy` | In ML-From-Scratch repo, Erik used log2 as the result of log(x)/log(2), while i used np.log2(p) directly. He also used for loop to calculate the entropy, while i used np.sum() |
| Information gain | Entropy(S) − Σ \|S_v\|/\|S\| · Entropy(S_v) | `decision_tree.py` L257–265 | `information_gain` | In ML-From-Scratch repo, because Erik used for loop to calculate entropy, so in information_gain function he just called entropy function, while i used for loop to calculate infomation gain directly |
| Best split (continuous) | test A ≥ c, pick c with max gain | `decision_tree.py` L88–124 + `utils/data_manipulation.py` L28–40 | not implemented yet | ... |

Notes:
- Candidate thresholds: For every feature it tries every unique value as a threshold (L93–98) and splits with >= threshold (data_manipulation.py). This is correct but brute force. On UCI HAR (~5,900 unique values × 561 features per node, with list comprehensions over all samples) this is far too slow, which is why I use sklearn for the experiments.
- Pruning: It only does pre-pruning: max_depth, min_samples_split, min_impurity. There is no post-pruning or reduced-error pruning. With the defaults, the tree grows until the leaves are almost pure, so it will overfit  .
### 5.3 Stopping/pruning comparison

## 6. Reflection
