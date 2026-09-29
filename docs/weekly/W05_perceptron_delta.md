# Perceptron (W05)

_Date written:_ 2026-09-29

## Question
Can a from-scratch perceptron (one-vs-rest, 6 classes) reach the level of logistic regression (macro-F1 0.93) on UCI HAR, or will it be much lower?
My prediction before running: noticeably lower than logistic regression. The data is not fully linearly separable, so the perceptron will keep changing w and never settle. I expected shuffling to help only a little.

## A. Concept capsule
- The perceptron outputs o = sgn(w·x): +1 if w·x > 0, otherwise −1. The extra input x₀ = 1 lets w₀ act as the bias.
- The boundary is w·x = 0. Picture w as a flagpole standing perpendicular to this line and pointing to the + side.
- Update rule: wᵢ ← wᵢ + η(t − o)xᵢ. Nothing changes when the prediction is right. When it is wrong, w moves toward x (if t = +1) or away from it (if t = −1).

## B. Derivation / worked example
- Start with w = (0, 1, −1), x = (1, 1, 2) including x₀, t = +1, η = 0.1.
- w·x = 0 + 1 − 2 = −1, so o = −1 and the example is wrong.
- Δw = 0.1·2·(1, 1, 2) = (0.2, 0.2, 0.4), so w_new = (0.2, 1.2, −0.6).
- w_new·x = 0.2 + 1.2 − 1.2 = 0.2 > 0, so the example is now right. w·x went up by η(t − o)‖x‖² = 1.2.

## C. Code-to-theory trace
| Code | Theory |
|---|---|
| `np.insert(x, 0, 1)` (perceptron_ovr.py) | x₀ = 1, bias w₀ |
| `np.where(y_train == k, 1, -1)` | class k vs the rest |
| `np.dot(x_bias, w)` | score w·x |
| `np.argmax(scores) + 1` | pick the class with the highest w·x |
| weight update line in `perceptron_fit` (perceptron.py) | wᵢ ← wᵢ + η(t − o)xᵢ |

Unit tests (`tests/test_perceptron.py`) check the drill example, AND (learned 4/4) and XOR (accuracy < 1, Fig. 4.3b).

## D. Controlled experiment
Validation set = 4 held-out subjects.

| Model | Epochs | Shuffle | Macro-F1 | Acc | Commit |
|---|---|---|---|---|---|
| Perceptron OvR scratch | 10 | no | 0.8426 | 0.8443 | 5a2ea17 |
| Perceptron OvR scratch | 30 | no | 0.9359 | 0.9321 | 5a2ea17 |
| Perceptron OvR scratch | 10 | yes | 0.9325 | 0.9286 | 5a2ea17 |
| Perceptron OvR scratch | 30 | yes | **0.9424** | **0.9386** | 5a2ea17 |
| sklearn Perceptron | default | yes | 0.9258 | 0.9200 | 5a2ea17 |
| Logistic regression (R0) | – | – | 0.9322 | 0.9279 | dece186 |

- **Why shuffle helps so much:** at 10 epochs, shuffling adds +0.09 macro-F1. The training file is sorted by person and time, and the perceptron updates after every sample, so without shuffling the last block of data pulls w toward itself right before training stops.
- **Why 30ep + shuffle beats sklearn (+0.017), and should I trust it?** Not fully. The data is not linearly separable, so w keeps moving and the final w depends on when training stops (one seed only). sklearn stops early when the loss stops improving. The validation set has only 4 people, and I picked the best setup on it, so the score is a bit optimistic.
- **Why the perceptron is close to logistic regression:** both are linear classifiers with a flat boundary w·x = 0; they only learn w differently. A gap of 0.01 on 4 people is not a real win.

## E. Failure / misconception
- In the drill I forgot x₀ = 1, so I never updated w₀.
- I passed `epochs` and `shuffle` in the wrong positions. The call must be `(X, y, lr, epochs, shuffle=..., seed=...)`.
- My first draft of the experiment loaded the official test set directly. I switched it to `load_har()` and the validation split before committing.

## F. Written-exam capsule
1. A perceptron computes a weighted sum of the inputs plus a bias, then outputs +1 or −1 depending on the sign.
2. The boundary w·x = 0 is a hyperplane, and w is perpendicular to it.
3. It only updates when it makes a mistake, moving w toward the correct side; if the data is linearly separable and η is small, it finds a separating line in a finite number of steps.
4. XOR is not linearly separable, so one perceptron fails and two layers are needed.
5. The delta rule uses the output before the threshold and minimizes squared error, so it converges even without separability.

## G. Reflection
- For online learning, data order matters as much as the number of epochs.
- A simple linear model can match logistic regression when the features are good, and a small validation set can make a tie look like a win.
- Next time: shuffle from the start, run several seeds and report mean ± std, and touch the test set only once, at the end.

## H. Inquiry trail (if AI used)
- AI helped with: the drill question set, pointing out bugs (import, unpacking, argument order), sklearn's default settings, guiding questions for the analysis. See `AI_USE.md`.
- I did myself: the drill, the perceptron and one-vs-rest code, every experiment, all the numbers in `metrics.csv`, and the conclusions.
