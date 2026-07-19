import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Import classifiers
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier


def train_and_evaluate():
    # 1. Load dataset
    dataset_path = "data/flood_prediction.csv"

    if not os.path.exists(dataset_path):
        print(f"Dataset not found at {dataset_path}! Please download the dataset first.")
        return

    df = pd.read_csv(dataset_path)

    # ✅ Rename columns to match frontend field names exactly
    df = df.rename(columns={
        "Temp": "temp",
        "Humidity": "humidity",
        "Cloud Cover": "cloud_cover",
        "ANNUAL": "annual_rainfall",
        "Jan-Feb": "jan_feb",
        "Mar-May": "mar_may",
        "Jun-Sep": "jun_sep",
        "Oct-Dec": "oct_dec",
        "avgjune": "avgjune",
        "sub": "sub",
        "flood": "Flood_Risk"
    })

    print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # 2. Handle Missing Values
    for col in df.columns[:-1]:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    # Remove remaining null values
    df = df.dropna()

    # 3. Split Features and Target
    X = df.drop(columns=["Flood_Risk"])
    y = df["Flood_Risk"]

    print(f"\nFeatures Shape: {X.shape}")
    print("\nTarget Distribution:")
    print(y.value_counts())
    # 4. Train Test Split
    X_train, X_test, y_train, y_test = train_test_split
    X,
    y,
    test_size=0.2,
    random_state=42,
 stratify=y


    # 5. Feature Scaling
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 6. Define Models
    models = {
        "Decision Tree": DecisionTreeClassifier(
            random_state=42,
            max_depth=15
        ),
        "Random Forest": RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=15
        ),
        "K-Nearest Neighbors": KNeighborsClassifier(
            n_neighbors=5
        ),
        "XGBoost": XGBClassifier(
            n_estimators=100,
            random_state=42,
            eval_metric="logloss"
        )
    }

    best_model = None
    best_model_name = ""
    best_accuracy = 0

    print("\n" + "=" * 60)
    print("MODEL COMPARISON")
    print("=" * 60)

    # 7. Train and Compare Models
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        predictions = model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, predictions)

        print(f"\n{name}")
        print(f"Accuracy: {accuracy * 100:.2f}%")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model
            best_model_name = name

    print("\n" + "=" * 60)
    print(f"Best Model : {best_model_name}")
    print(f"Best Accuracy : {best_accuracy * 100:.2f}%")
    print("=" * 60)

    # 8. Evaluate Best Model
    best_predictions = best_model.predict(X_test_scaled)

    print("\nClassification Report")
    print(classification_report(y_test, best_predictions))

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, best_predictions))

    # 9. Save Model and Scaler
    os.makedirs("models", exist_ok=True)

    joblib.dump(best_model, "models/flood_model.joblib")
    joblib.dump(scaler, "models/scaler.joblib")

    print("\nModel saved successfully!")
    print("Saved as: models/flood_model.joblib")
    print("Saved as: models/scaler.joblib")


if __name__ == "__main__":
    train_and_evaluate()
