import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay


# ============================================================
# IRONHUB - AI STARTUP VALIDATION ENGINE
# RANDOM FOREST CLASSIFICATION
# ============================================================


# 1. LOAD DATASET
df = pd.read_csv("startup_validation_dataset.csv")

print("=" * 60)
print("IRONHUB - STARTUP VALIDATION DATASET")
print("=" * 60)

print(df.head())

print("\nTotal startup records:", len(df))


# 2. CHECK DATA
print("\nMISSING VALUES")
print("=" * 60)
print(df.isnull().sum())


# 3. SELECT FEATURES
features = [
    "MarketSize",
    "CustomerInterest",
    "CompetitionLevel",
    "ProfitMargin"
]

X = df[features]

y = df["ValidationLabel"]


# 4. CHECK LABELS
print("\nVALIDATION LABELS")
print("=" * 60)
print(y.value_counts())


# 5. SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))


# 6. CREATE RANDOM FOREST MODEL
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# 7. TRAIN MODEL
model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully.")


# 8. MAKE PREDICTIONS
y_pred = model.predict(X_test)


# 9. MODEL ACCURACY
accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nMODEL ACCURACY")
print("=" * 60)
print(f"Accuracy: {accuracy:.2%}")


# 10. CLASSIFICATION REPORT
print("\nCLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# 11. CONFUSION MATRIX
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred
)

plt.title(
    "Random Forest - Startup Validation"
)

plt.tight_layout()

plt.savefig(
    "IronHub_Random_Forest_Confusion_Matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 12. FEATURE IMPORTANCE
importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE")
print("=" * 60)
print(importance)


# 13. FEATURE IMPORTANCE CHART
plt.figure(figsize=(8, 5))

plt.bar(
    importance["Feature"],
    importance["Importance"]
)

plt.title(
    "Random Forest - Feature Importance"
)

plt.xlabel(
    "Validation Factor"
)

plt.ylabel(
    "Importance"
)

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "IronHub_Random_Forest_Feature_Importance.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 14. FINAL MESSAGE
print("\n" + "=" * 60)
print("RANDOM FOREST ANALYSIS COMPLETED")
print("=" * 60)

print(
    "Confusion matrix saved as:"
)

print(
    "IronHub_Random_Forest_Confusion_Matrix.png"
)

print(
    "\nFeature importance chart saved as:"
)

print(
    "IronHub_Random_Forest_Feature_Importance.png"
)