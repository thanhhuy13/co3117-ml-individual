from src.data import load_har, SEED
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt

depth = []
f1_train = []
f1_val = []


train, val, _ = load_har()
x_train, y_train, _ = train 
x_val, y_val, _ = val 


for d in range(1, 51): 
    model = DecisionTreeClassifier(max_depth=d, random_state=SEED)
    model.fit(x_train, y_train)
    pred_train = model.predict(x_train)
    pred_val = model.predict(x_val)
    f1_on_train = f1_score(y_train, pred_train, average="macro")
    f1_on_val = f1_score(y_val, pred_val, average="macro")

    depth.append(d)
    f1_train.append(f1_on_train)
    f1_val.append(f1_on_val)

for x, y, z in zip(depth, f1_train, f1_val): 
    print(f"for depth = {x}, f1 on train: {y:.4f}, f1 on val: {z:.4f}\n")


plt.plot(depth, f1_train, marker = "o", label = "f1_score on training set")
plt.plot(depth, f1_val, marker="o", label = "f1_score on validation set")
plt.xlabel("depth (size of decision tree)")
plt.ylabel("f1_score")
plt.title("F1_score vs depth")
plt.legend()
plt.grid(True)
plt.savefig("results/figures/dt_validation_curve_max_depth.png", dpi=150)
