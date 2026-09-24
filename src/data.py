import numpy as np

DATA_DIR = "data/raw/UCI HAR Dataset"
SEED = 42
VAL_SUBJECTS = [3, 16, 22, 23]


def load(split):
    X = np.loadtxt(f"{DATA_DIR}/{split}/X_{split}.txt")
    y = np.loadtxt(f"{DATA_DIR}/{split}/y_{split}.txt", dtype=int)
    s = np.loadtxt(f"{DATA_DIR}/{split}/subject_{split}.txt", dtype=int)
    return X, y, s


def load_har():
    X, y, s = load("train")
    X_test, y_test, s_test = load("test")

    val_subjects = VAL_SUBJECTS
    if val_subjects is None:
        rng = np.random.default_rng(SEED)
        val_subjects = rng.choice(np.unique(s), 4, replace=False)

    is_val = np.isin(s, val_subjects)
    train = (X[~is_val], y[~is_val], s[~is_val])
    val = (X[is_val], y[is_val], s[is_val])
    test = (X_test, y_test, s_test)
    return train, val, test


if __name__ == "__main__":
    train, val, test = load_har()
    for name, (X, y, s) in zip(["train", "val", "test"], [train, val, test]):
        print(name, X.shape, sorted(set(s.tolist())))

    assert not set(train[2]) & set(val[2])
    assert not set(train[2]) & set(test[2])
    assert not set(val[2]) & set(test[2])
    print("ok")
