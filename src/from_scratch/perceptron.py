import numpy as np

def perceptron_predict(X, w):
    X = np.c_[np.ones(len(X)), X]       
    return np.where(X @ w > 0, 1, -1)


def perceptron_fit(X, y, lr, epochs, shuffle=False, seed=None):
    X = np.c_[np.ones(len(X)), X]
    w = np.zeros(X.shape[1])
    rng = np.random.default_rng(seed)
    
    for epoch in range(epochs):
        if shuffle:
            idx = rng.permutation(len(X))
        else:
            idx = np.arange(len(X))
            
        for xi, ti in zip(X[idx], y[idx]):
            if np.dot(xi, w) > 0:
                o = 1
            else:
                o = -1             
            w = w + lr * (ti - o) * xi
            
    return w