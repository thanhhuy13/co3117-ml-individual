# W05 Perceptron drill – corrections

First attempt: [w05_perceptron_drill_first_attempt.pdf](w05_perceptron_drill_first_attempt.pdf) (commit `1e7ad1d`)  
Corrected on: 2026-09-29

## Q1 – Perceptron update (self-made)
- **My answer:**
  - (a) wrote the rule wᵢ ← wᵢ + η(t − o)xᵢ.
  - (b) got w·x = −1, so o = −1.
  - (c) got Δw = (0; 0.2; 0.4) and w_new = (0; 1.2; −1.4).
  - (d) got w_new·x = 1 and said "increase the weight".
- **Result:** partly correct
- **Correction:**
  - (a) and the value in (b) are right. For (b) I should also have said it outright: o = −1 but t = +1, so the example is misclassified.
  - (c) The bias has input x₀ = 1, so w₀ gets updated too. Δw = 0.1·2·(1, 1, 2) = (0.2, 0.2, 0.4), which gives w_new = (0.2, 1.2, −0.6). I also made an arithmetic slip: −1 + 0.4 = −0.6, not −1.4.
  - (d) What I actually computed was Δw·x (and without x₀), not w_new·x. The correct value is w_new·x = 0.2 + 1.2 − 1.2 = 0.2 > 0, so the output is now +1.
  - Why it increases: when t = +1 and o = −1, the update pushes w in the direction of x. That means w·x goes up by exactly η(t − o)‖x‖² = 0.2·6 = 1.2, from −1 to 0.2.
- **Source:** Mitchell (1997), Section 4.4.2, pp. 88–89; output definition pp. 86–87

## Q2 – Exercise 4.1
- **My answer:** assumed w₀ = c, got "w·x = −2" and "w₀ = 2", and never found w₁ or w₂.
- **Result:** wrong / not finished
- **Correction:**
  - The decision surface is w₀ + w₁x₁ + w₂x₂ = 0, so both intercept points must satisfy w·x = 0, not −2:
    - At (−1, 0): w₀ − w₁ = 0, so w₁ = w₀.
    - At (0, 2): w₀ + 2w₂ = 0, so w₂ = −w₀/2.
  - To choose the sign, I look at Fig. 4.3a. The "+" points are on the upper-left of the line and the origin is on the "−" side, so w₀ < 0.
  - Picking w₀ = −2 gives (w₀, w₁, w₂) = (−2, −2, 1). Check with (−1, 2): −2 + 2 + 2 = 2 > 0 (right).
  - Any positive multiple of these weights also works. Flipping every sign keeps the same line but swaps which side is +.
- **Source:** Mitchell (1997), Section 4.4 and Figure 4.3, pp. 86–87

## Q3 – Exercise 4.2
- **My answer:** for A ∧ ¬B, wrote the four inequalities over the (0/1) inputs. Did not pick actual weights and did not do the XOR network.
- **Result:** partly correct
- **Correction:**
  - My inequalities were right. I just needed to pick numbers that satisfy them. With 0/1 inputs: A ∧ ¬B: w₀ = −0.5, w₁ = 1, w₂ = −1. Negating B just means flipping the sign of its weight.
  - XOR = (A ∧ ¬B) ∨ (¬A ∧ B), built as a 2-layer network:
    - h₁ = A ∧ ¬B: (−0.5, 1, −1)
    - h₂ = ¬A ∧ B: (−0.5, −1, 1)
    - output = OR(h₁, h₂): (−0.5, 1, 1)
  - Checked all four inputs: (0,0)→0, (1,0)→1, (0,1)→1, (1,1)→0 ✓
  - Note on conventions: I used output 1/0 and "≥ 0", while Mitchell uses ±1 and "> 0". Either works as long as I stay consistent.
- **Source:** Mitchell (1997), Section 4.4.1, pp. 87–88

## Q4 – Why XOR fails (self-made)
- **My answer:** not in my drill, so not attempted.
- **Result:** wrong / not done
- **Correction:**
  - A single perceptron can only draw one straight line. In XOR, the positives (0,1) and (1,0) sit on one diagonal and the negatives (0,0) and (1,1) sit on the other (Fig. 4.3b), so no single line separates them. XOR is not linearly separable.
  - Short proof using the same inequality method as in C1:
    - The two positives give w₀ + w₁ > 0 and w₀ + w₂ > 0. Adding them: 2w₀ + w₁ + w₂ > 0.
    - The two negatives give w₀ ≤ 0 and w₀ + w₁ + w₂ ≤ 0. Adding them: 2w₀ + w₁ + w₂ ≤ 0.
    - These contradict each other, so no weights exist.
  - The fix is a 2-layer network, as in C1.
- **Source:** Mitchell (1997), Section 4.4.1, pp. 86–88 (Figure 4.3b)

## Q5 – Perceptron rule vs delta rule (self-made)
- **My answer:**
  - Wrote the perceptron rule, but for the delta rule only wrote o(x) = w·x.
  - (a) perceptron uses a discrete output, delta uses a linear output.
  - (b) perceptron converges to zero error only if the data are linearly separable; delta converges to minimum squared error either way.
- **Result:** partly correct
- **Correction:**
  - I never actually wrote the delta rule. It looks the same, Δwᵢ = η(t − o)xᵢ, but here o = w·x (no threshold). It comes from gradient descent on E = ½Σ(t_d − o_d)². The batch version sums over all examples; the stochastic version updates after each one.
  - (a) is right. The perceptron rule uses the error of the thresholded output sgn(w·x). The delta rule uses the error of the raw linear output w·x.
  - (b) is right in spirit, with two things missing:
    - The perceptron rule needs linear separability and a small enough η, and then it finishes in a finite number of steps.
    - The delta rule only converges asymptotically and needs a small enough η. Also, the weights that minimize squared error don't necessarily minimize the number of misclassified examples.
- **Source:** Mitchell (1997), Section 4.4.3, pp. 89–92, and Section 4.4.4, pp. 94–95

## Summary
- **What I got right:**
  - The perceptron training rule and computing o = sgn(w·x).
  - Turning a truth table into inequalities on the weights.
  - The core difference between the two rules: thresholded vs linear output, and "linearly separable" vs "minimum squared error".
- **Main gaps:**
  - Forgetting x₀ = 1 when updating and computing w·x, which caused the errors in A(c) and A(d).
  - Not using the idea that the boundary is exactly where w·x = 0, and not checking which side is positive (B).
  - Getting the direction of more_general_than backwards: more general means more instances are positive.
  - Leaving answers unfinished: no concrete weights, no XOR network, no written delta rule, and no C2.
