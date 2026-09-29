import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import f1_score, accuracy_score
from src.data import load_har, SEED
from src.from_scratch.perceptron import perceptron_fit, perceptron_predict

train, val, _ = load_har()
x_train, y_train, _ = train
x_val, y_val, _ = val

configs = [
    ("scratch 10ep", 10, False),
    ("scratch 30ep", 30, False),
    ("scratch 10ep shuffle", 10, True),
    ("scratch 30ep shuffle", 30, True),
]

for name, epochs, shuffle in configs:
    W = []
    for k in range(1, 7):
        y_binary = np.where(y_train == k, 1, -1)
        w_k = perceptron_fit(x_train, y_binary, 0.01, epochs, shuffle, seed=SEED)
        W.append(w_k)

    y_pred_scratch = []
    for x in x_val:
        x_bias = np.insert(x, 0, 1)  
        scores = [np.dot(x_bias, w) for w in W]
        pred_class = np.argmax(scores) + 1 
        y_pred_scratch.append(pred_class)

    f1_scratch = f1_score(y_val, y_pred_scratch, average='macro')
    acc_scratch = accuracy_score(y_val, y_pred_scratch)
    print(f"{name:20s} - Macro-F1: {f1_scratch:.4f} and Accuracy: {acc_scratch:.4f}")

clf = Perceptron(random_state=SEED)
clf.fit(x_train, y_train)
y_pred_sklearn = clf.predict(x_val)

f1_sklearn = f1_score(y_val, y_pred_sklearn, average='macro')
acc_sklearn = accuracy_score(y_val, y_pred_sklearn)

print(f"Perceptron (Sklearn) - Macro-F1: {f1_sklearn:.4f} and Accuracy: {acc_sklearn:.4f}")