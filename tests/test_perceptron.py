import numpy as np
from src.from_scratch.perceptron import perceptron_fit, perceptron_predict

X_gate = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([-1, -1, -1, 1])
y_xor = np.array([-1, 1, 1, -1])


def test_predict_drill_question_a():
    w = np.array([0, 1, -1])
    x = np.array([[1, 2]])
    assert perceptron_predict(x, w)[0] == -1


def test_and():
    w = perceptron_fit(X_gate, y_and, 0.1, 20)
    pred = perceptron_predict(X_gate, w)
    assert np.array_equal(pred, y_and)


def test_xor():
    w = perceptron_fit(X_gate, y_xor, 0.1, 20)
    pred = perceptron_predict(X_gate, w)
    assert np.mean(pred == y_xor) < 1.0