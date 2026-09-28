from src.data import load_har, SEED
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

train, val, _ = load_har()
x_train, y_train, _ = train 
x_val, y_val, _ = val 

models = [
    ("full tree", DecisionTreeClassifier(random_state=SEED)), 
    ("max_depth_4", DecisionTreeClassifier(max_depth=4, random_state=SEED)), 
    ("min_samples_leaf", DecisionTreeClassifier(min_samples_leaf=20, random_state=SEED)), 
    ("ccp", DecisionTreeClassifier(ccp_alpha=0.005, random_state=SEED))
]

for name, model in models: 
    model.fit(x_train, y_train)
    pred_train = model.predict(x_train)
    pred_val = model.predict(x_val)
    f1_on_train = f1_score(y_train, pred_train, average="macro")
    f1_on_val = f1_score(y_val, pred_val, average="macro")
    print(f"model's name: {name},f1_score on training set {f1_on_train:.4f}, f1_score on val set: {f1_on_val:.4f}, model's depth: {model.get_depth()}, model's leafs {model.get_n_leaves()}")