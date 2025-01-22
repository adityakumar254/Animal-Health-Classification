# Animal Health Classification

The Animal Health Classification project is designed to assist in determining the health risk associated with various animals based on a set of symptoms. It leverages machine learning algorithms to classify conditions as either "Dangerous" or "Not Dangerous." This classification can serve as a valuable tool for veterinarians, animal handlers, and wildlife researchers to prioritize attention to potentially critical health conditions.

## Features
- **Symptom-based Classification**: Given a set of symptoms, the model predicts whether the condition is dangerous.
- **Random Forest Model**: The classification is done using a Random Forest model.
- **Model Training**: The model can be trained using the provided dataset, and predictions can be made on new input data.

## Directory Structure
```
project-root/
├── .github/                  # GitHub-related files
├── .pytest_cache/            # Pytest cache files
├── Data/                     # Folder containing the dataset
│   └── data.csv              # Dataset containing animal health data (symptoms and dangerous labels)
├── model/                   
│   ├── train_model.py        # Script for training the model
│   ├── predict.py            # Script for making predictions
│   └── evaluate.py           # Script for evaluating the model
├── Tests/                    # Folder containing test scripts
│   └── test_project.py       # Test file for training, prediction, and evaluation
├── random_forest_model.pkl   # Trained model file
├── symptoms_encoder.pkl      # Encoder file for symptom transformation
├── requirements.txt          # List of required Python dependencies
├── README.md                 # Project documentation (this file)
├── Command of CMD.txt        # Notes or commands for CMD usage
└── .gitignore                # Git ignore file
```

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/animal-health-classification.git
cd animal-health-classification
```

### 2. Install Dependencies
Install the required Python libraries using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Dataset
The dataset (`data.csv`) should be placed in the `Data/` folder. It contains the animal names, symptoms, and whether the condition is dangerous (target variable).

Example dataset columns:
- `AnimalName`: Name of the animal
- `symptoms1`, `symptoms2`, `symptoms3`, `symptoms4`, `symptoms5`: Symptoms of the animal
- `Dangerous`: Target variable (Yes/No)

## Usage

### 1. Training the Model
To train the model, run the following script:
```bash
python model/train_model.py
```
This will:
- Load the dataset (`Data/data.csv`).
- Train a Random Forest model on the data.
- Save the trained model as `random_forest_model.pkl`.
- Save the encoder for transforming symptoms into numerical features as `symptoms_encoder.pkl`.

### 2. Making Predictions
After training the model, you can use it to make predictions on new symptom data. To make a prediction, run:
```bash
python model/predict.py
```
The script will use the trained model and encoder to predict whether the condition based on the symptoms provided is dangerous.

### 3. Evaluating the Model
To evaluate the model's performance, use the following command:
```bash
python model/evaluate.py
```
This will:
- Split the data into training and testing sets.
- Evaluate the model on the test set and print metrics such as accuracy and the classification report.

### 4. Running Tests
The project includes a set of tests to verify that the training, prediction, and evaluation work correctly. To run the tests, use:
```bash
pytest Tests/test_project.py
```
This will run the following tests:
- `test_train_model`: Verifies that the model and encoder are generated after training.
- `test_predict`: Tests the prediction functionality.
- `test_evaluate_model`: Validates the evaluation process.

## Example Usage
The following code demonstrates how to make predictions using the trained model:

```python
from model.predict import predict

example_symptoms = ["Fever", "Diarrhea", "Vomiting", "Weight loss", "Dehydration"]
prediction = predict(example_symptoms)
print(f"Prediction: {prediction}")
```

### Expected Output
```
Prediction: Yes
```

## Requirements
The following Python libraries are required to run the project:
- `pandas`
- `scikit-learn`
- `joblib`
- `pytest`

You can install the required libraries with:
```bash
pip install -r requirements.txt
```
