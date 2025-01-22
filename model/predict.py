import joblib
import pandas as pd

def predict(input_symptoms):
    # Use relative paths
    model = joblib.load(r"random_forest_model.pkl")
    encoder = joblib.load(r"symptoms_encoder.pkl")

    # Create a DataFrame with the same structure as training symptoms
    symptom_columns = ["symptoms1", "symptoms2", "symptoms3", "symptoms4", "symptoms5"]
    input_df = pd.DataFrame([input_symptoms], columns=symptom_columns)
    
    # Transform input symptoms using the encoder
    input_features = encoder.transform(input_df)
    
    # Predict
    predictions = model.predict(input_features)
    return "Yes" if predictions[0] == 1 else "No"

if __name__ == "__main__":
    # Example input
    example_symptoms = ["Mild Cough", "Normal Appetite", "Active Behavior", "Normal Temperature", "No Vomiting"]
    print("Prediction:", predict(example_symptoms))