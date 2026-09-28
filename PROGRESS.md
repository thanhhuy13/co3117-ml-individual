# PROGRESS – Instructor dashboard

| Period | Topic | Post | Drill | First evidence | Revision commit | Tag | Status |
|---|---|---|---|---|---|---|---|
| W01–W04 | PRE-RELEASE catch-up (Foundations, Decision Tree) | [catch-up post](docs/pre-release/PRE_RELEASE_CATCHUP.md) | [release baseline](exercises/Release_baseline_diagnostic_w01_04.pdf) | [`d31049a`](https://github.com/thanhhuy13/co3117-ml-individual/commit/d31049a) handwritten baseline, [`1a48d1d`](https://github.com/thanhhuy13/co3117-ml-individual/commit/1a48d1d) own entropy/gain | [corrections](exercises/Release_baseline_W01_04_corrections.md) [`ddf4dc5`](https://github.com/thanhhuy13/co3117-ml-individual/commit/ddf4dc5), code fix [`694f411`](https://github.com/thanhhuy13/co3117-ml-individual/commit/694f411) | `release-baseline` | PRE-RELEASE |
| W05 | Perceptron / Delta rule + onboarding | | | | | `w05` | ACTIVE |
| W06 | | | | | | `w06` | |
| W07 | | | | | | `w07` | |
| W08 | MIDTERM (16 Oct 2026) | midterm entry | timed rehearsal | — | reflection | `w08-midterm` | MIDTERM |
| W09 | | | | | | `w09` | |
| W10 | | | | | | `w10` | |
| W11 | | | | | | `w11` | |
| W12 | | | | | | `w12` | |
| W13 | | | | | | `w13` | |
| W14 | | | | | | `w14` | |
| W15 | | | | | | `w15` | |

## R0 release checkpoint
- Data protocol (frozen): [data/README.md](data/README.md), loader [src/data.py](src/data.py)
- Baseline: [logistic regression](experiments/part1_pre_midterm/baseline_logistic_regression.py) – val Macro-F1 0.9322
- Own impurity routine: [src/from_scratch/decision_tree.py](src/from_scratch/decision_tree.py), tests [tests/test_decision_tree.py](tests/test_decision_tree.py)
- Decision tree validation curve: [code](experiments/part1_pre_midterm/dt_validation_curve_max_depth.py), [figure](results/figures/dt_validation_curve_max_depth.png)
- Stopping/pruning comparison: [code](experiments/part1_pre_midterm/dt_pruning_comparison.py)
- All results: [results/metrics.csv](results/metrics.csv)
- AI use log: [AI_USE.md](AI_USE.md)

## Graded parts
| Part | Deadline | Tag | Status |
|---|---|---|---|
| Part I | 14 Oct 2026 | `part1-final` | |
| Part II | 2 days before final exam | `part2-final` | |
