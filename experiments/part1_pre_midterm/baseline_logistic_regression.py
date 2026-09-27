from src.data import load_har, SEED
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, classification_report

train, val, _ = load_har()
X_train, y_train, _ = train
X_val, y_val, _ = val

scaler = StandardScaler() 
X_train_standard_scaler = scaler.fit_transform(X_train)
X_val_standard_scaler = scaler.transform(X_val)

model = LogisticRegression(max_iter = 1000, random_state = SEED)
model.fit(X_train_standard_scaler, y_train)
pred = model.predict(X_val_standard_scaler)

f1 = f1_score(y_val, pred,average="macro")
accuracy = accuracy_score(y_val, pred)
confusion_matrix = confusion_matrix(y_val, pred)
print(classification_report(y_val, pred))

print(f"Macro-F1 = {f1:.4f}")
print(f"Accuracy = {accuracy:.4f}")
print("Confusion matrix \nx", confusion_matrix)

