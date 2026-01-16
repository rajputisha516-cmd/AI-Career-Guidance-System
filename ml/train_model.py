import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------
# LOAD DATASET
# ---------------------------
DATA_PATH = "data/raw/career_dataset_v3.csv"

df = pd.read_csv(DATA_PATH)

# ---------------------------
# SPLIT FEATURES & TARGET
# ---------------------------
X = df.drop("role", axis=1)
y = df["role"]

# ---------------------------
# ENCODE TARGET
# ---------------------------
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# ---------------------------
# TRAIN-TEST SPLIT
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded
)

# ---------------------------
# MODEL
# ---------------------------
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# ---------------------------
# EVALUATION
# ---------------------------
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\n🎯 Model Accuracy: {accuracy:.2f}")

print("📊 Classification Report:\n")
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))

print("\n🧩 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# ---------------------------
# SAVE MODEL & ENCODER
# ---------------------------
import os
os.makedirs("models", exist_ok=True)   # ✅ YE LINE YAHAN ADD KARO

with open("models/career_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("\n✅ Model training completed successfully!")
print("📁 Saved files:")
print(" - models/career_model.pkl")
print(" - models/label_encoder.pkl")
