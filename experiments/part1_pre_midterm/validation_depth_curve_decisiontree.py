from src.data import load_har, SEED
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

train, val, _ = load_har()
x_train, y_train, _ = train 
x_val, y_val, _ = val 

model = DecisionTreeClassifier(max_depth=3, random_state=SEED)
model.fit(x_train, y_train)
pred_train = model.predict(x_train)
pred_val = model.predict(x_val)
f1_on_train = f1_score(y_train, pred_train, average="macro")
f1_on_val = f1_score(y_val, pred_val, average="macro")

print(f"f1 on train: {f1_on_train:.4f}\n")
print(f"f1 on val: {f1_on_val:.4f}\n")