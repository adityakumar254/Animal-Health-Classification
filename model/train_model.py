import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import joblib

def preprocess_data(file_path):
    # Handle missing target values
    data = pd.read_csv(file_path)
    data = data.dropna(subset=["Dangerous"])
    
    # Encode symptoms and target variable
    symptom_columns = ["symptoms1", "symptoms2", "symptoms3", "symptoms4", "symptoms5"]
    ohe = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
    encoded_symptoms = ohe.fit_transform(data[symptom_columns])
    # Save the encoder for prediction use
    joblib.dump(ohe, "symptoms_encoder.pkl")
    
    # Prepare features (X) and target (y)
    X = encoded_symptoms
    y = data["Dangerous"].map({"Yes": 1, "No": 0})  # Binary encoding

    return X, y

def train_model():
    # Preprocess data
    X, y = preprocess_data(file_path="Data/data.csv")

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Save the trained model
    joblib.dump(model, "random_forest_model.pkl")

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    train_model()