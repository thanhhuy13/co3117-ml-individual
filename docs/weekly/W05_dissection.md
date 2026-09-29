# W05 – Dissection of ML-From-Scratch perceptron

Reference: Erik Linder-Norén, ML-From-Scratch, `mlfromscratch/supervised_learning/perceptron.py` (branch master, accessed 2026-09-30)

My code: `src/from_scratch/perceptron.py`, `experiments/part1_pre_midterm/perceptron_ovr.py`

| Step | Formula / idea | ML-From-Scratch | My code | Difference |
|---|---|---|---|---|
| Output | o = f(w·x) | L47–48 `linear_output = X.dot(self.W) + self.w0`, `y_pred = self.activation_func(linear_output)`; L60 in `predict` | `perceptron_predict`: `np.where(X @ w > 0, 1, -1)` | Same w·x + w₀. Theirs passes it through sigmoid, so o is a continuous value in (0, 1); mine thresholds it to ±1. |
| Bias & initialisation | w₀, starting w | L41–43: W random uniform in ±1/√n, `w0` zeros kept separately | extra column x₀ = 1, all weights start at 0 | Bias gives the same result either way; only the code layout differs. The real difference is the start: random W vs all zeros. |
| Error / gradient | Δw from error | L50: `loss.gradient(y, y_pred) * activation_func.gradient(linear_output)`; L52–53: `X.T.dot(error_gradient)` | `learning_rate * (t - o) * x` in `perceptron_fit` | Theirs is the chain rule for a sigmoid unit, −(t − o)·o(1 − o)·x, which is almost never zero. Mine is (t − o)·x with thresholded o, which is zero whenever the prediction is right. |
| Update | w ← w − η·∇E | L55–56: `W -= learning_rate * grad_wrt_w` once per iteration, over all samples | one update after each sample, only when wrong | Theirs is batch gradient descent: every sample contributes to every step. Mine is online: one sample at a time, only on mistakes. Subtracting the gradient turns −(t − o) back into +(t − o). Because the batch gradient sums over the whole training set, data order and shuffling do not matter for theirs, while for mine shuffling raised val Macro-F1 from 0.8426 to 0.9325 at 10 epochs (post section D). |
| Multi-class | 6 classes | L38, L42: y is one-hot (`n_outputs` columns), W has shape (n_features, n_outputs), all classes trained together | loop over 6 separate perceptrons in `perceptron_ovr.py`, then `argmax` | Same one-vs-rest idea. Theirs trains all 6 units at once in one matrix with targets 0/1; mine trains them one by one with targets ±1. |

**Conclusion:** despite its name, the ML-From-Scratch `Perceptron` is a sigmoid unit trained by batch gradient descent on squared error, not the perceptron training rule. This is the same perceptron-rule vs gradient-descent difference as in my drill answer D1.
    