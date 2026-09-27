import os

import numpy as np
import pytest
from scipy.stats import entropy as scipy_entropy
from sklearn.metrics import mutual_info_score

from src.from_scratch.decision_tree import entropy, information_gain

HAS_DATA = os.path.exists("data/raw/UCI HAR Dataset")

y = np.array(["+", "+", "-", "+", "-", "-"])
a1 = np.array(["T", "T", "T", "F", "F", "F"])
a2 = np.array(["T", "T", "F", "F", "T", "T"])


def test_entropy_mitchell():
    assert np.isclose(entropy(y), 1.0)


def test_gain_mitchell():
    assert np.isclose(information_gain(y, a2), 0.0)
    assert np.isclose(information_gain(y, a1), 0.0817, atol=1e-4)


def test_entropy_pure():
    assert np.isclose(entropy(np.array(["+", "+", "+"])), 0.0)


@pytest.mark.skipif(not HAS_DATA, reason="UCI HAR not downloaded")
def test_entropy_har_matches_scipy():
    from src.data import load_har

    (X, y_har, _), _, _ = load_har()
    _, counts = np.unique(y_har, return_counts=True)
    assert np.isclose(entropy(y_har), scipy_entropy(counts, base=2))


@pytest.mark.skipif(not HAS_DATA, reason="UCI HAR not downloaded")
def test_gain_har_matches_sklearn():
    from src.data import load_har

    (X, y_har, _), _, _ = load_har()
    x = X[:, 3] < -0.9
    assert np.isclose(information_gain(y_har, x), mutual_info_score(y_har, x) / np.log(2))