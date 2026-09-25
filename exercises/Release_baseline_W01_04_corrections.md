# Release baseline diagnostic – corrections

First attempt: [Release_baseline_diagnostic_w01_04.pdf](Release_baseline_diagnostic_w01_04.pdf) (commit `d31049a`)
Corrected on: 2026-09-26

## Q1 – Entropy and information gain (Mitchell Ex. 3.2)
- **My answer:** Entropy(S) = 1; Gain = 1 − (4/6·1 + 2/6·1) = 0
- **Result:** correct
- **Correction:** notation only – should be Gain(S, a2), not Gain(Entropy, a2)
- **Source:** Mitchell (1997), Section 3.4.1, pp. 55–58

## Q2 – Decision trees for boolean functions (Mitchell Ex. 3.1)
- **My answer:** trees for (a)–(d)
- **Result:** correct; (d) not minimal
- **Correction:** (d) branch A=0: B irrelevant (both B subtrees identical) → A=0 → C → D
- **Source:** Mitchell (1997), Section 3.2, pp. 52–53

## Q3 – Overfitting and tree size
- **My answer:** "predicts well on training set but fails on test set"; marked overfit where the two curves separate
- **Result:** partly correct
- **Correction:**
  - formal def: h overfits if ∃ h' with higher training error but lower error over the whole distribution
  - overfit starts where test accuracy peaks and starts to drop (train keeps rising), not where curves separate
- **Source:** Mitchell (1997), Section 3.7.1, pp. 66–67, Figure 3.6

## Q4 – Avoiding overfitting, reduced-error pruning
- **My answer:** pre-pruning / post-pruning; "replaces leaf which enhances accuracy"
- **Result:** partly correct
- **Correction:**
  - separate validation set
  - replace an internal node by a leaf with the majority class
  - prune only if validation accuracy does not decrease
- **Source:** Mitchell (1997), Section 3.7.1.1, pp. 69–70

## Q5 – Continuous attributes and missing values
- **My answer:** (a) "use regression tree"; (b) don't know
- **Result:** wrong / not answered
- **Correction:**
  - regression tree = continuous target, not continuous attribute
  - boolean test A < c; candidate c between adjacent sorted values where class changes; pick c with max gain
  -most common value at the node / most common among same-class examples / fractional examples with weights (C4.5)
- **Source:** Mitchell (1997), Sections 3.7.2 and 3.7.4, pp. 72 and 75

## Q6 – Model complexity; logistic vs linear regression
- **My answer:** (a) train increases, test decreases; (b) linear = linear function, logistic = non-linear (sigmoid)
- **Result:** partly correct
- **Correction:**
  - test increases then peak then decreases, left = underfit, right of peak = overfit
  - linear regression → continuous value; logistic → probability in (0, 1)
  - classification by threshold (e.g. 0.5)
  - decision boundary still linear → logistic is a linear classifier
- **Source:** Müller & Guido (2017), Ch. 2, pp. 26–29 (Figure 2-1), pp. 56–58

## Summary
- **What I got right:** entropy / information gain; boolean functions as trees
- **Main gaps:**
  - formal overfitting definition, where overfitting starts
  - reduced-error pruning details (validation set)
  - continuous attributes (confused with regression tree), missing values
  - underfitting region; logistic regression is still a linear classifier
- **What I will review next:** Mitchell 3.7; pruning + learning-curve experiment on UCI HAR (catch-up)