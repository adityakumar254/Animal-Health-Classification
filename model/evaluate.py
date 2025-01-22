import pandas as pd
import joblib
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def evaluate_model():
    # Load data
    data = pd.read_csv("Data/data.csv")
    symptom_columns = ["symptoms1", "symptoms2", "symptoms3", "symptoms4", "symptoms5"]
    encoder = joblib.load("symptoms_encoder.pkl")
    X = encoder.transform(data[symptom_columns])
    y = data["Dangerous"].map({"Yes": 1, "No": 0})  # Binary encoding
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load the trained model
    model = joblib.load("random_forest_model.pkl")

    # Evaluate the model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate_model()
