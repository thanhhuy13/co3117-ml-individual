import numpy as np

def perceptron_predict(X, w):
    X = np.c_[np.ones(len(X)), X]       
    return np.where(X @ w > 0, 1, -1)

def perceptron_fit(X, y, lr, epochs):
    X = np.c_[np.ones(len(X)), X]
    w = np.zeros(X.shape[1])
    for _ in range(epochs):
        for xi, ti in zip(X, y):
            o = 1 if xi @ w > 0 else -1
            w += lr * (ti - o) * xi
    return w