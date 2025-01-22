# Animal Health Classification

The Animal Health Classification project is designed to assist in determining the health risk associated with various animals based on a set of symptoms. It leverages machine learning algorithms to classify conditions as either **"Dangerous"** or **"Not Dangerous."** This classification can serve as a valuable tool for veterinarians, animal handlers, and wildlife researchers to prioritize attention to potentially critical health conditions.

## 🛠️ Features

- **User-Friendly Interface**: Built with Streamlit for a clean and interactive user experience.
- **Model Integration**: Utilizes a trained Random Forest Classifier for health prediction.
- **Symptom-Based Classification**: Accepts up to 5 symptoms as input for classification.
- **Interactive Elements**: Includes health tips, videos, and helpful information for animal care.
- **Deployment**: Fully deployed and accessible online.

## 🌐 Live Project

[Live Demo](https://animal-health-classification-preciptions-a-07.streamlit.app)

---

## 🚀 Installation and Usage

### Prerequisites

- Python 3.8+
- Libraries: `pandas`, `joblib`, `streamlit`, `scikit-learn`

### 📁 File Structure

```
├── .streamlit
│   └── secrets.toml            # Streamlit configuration file
├── Data
│   └── data.csv                # Dataset used for training
├── model
│   ├── evaluate.py             # Model evaluation logic
│   ├── predict.py              # Prediction functionality
│   ├── train_model.py          # Model training code
├── Tests
│   ├── __init__.py             # Test initialization
│   ├── test_project.py         # Unit test cases
├── app.py                      # Main Streamlit application
├── random_forest_model.pkl     # Serialized Random Forest model
├── README.md                   # Project documentation
├── requirements.txt            # Dependencies
├── symptoms_encoder.pkl        # Encoded symptoms for model usage
```
---

## 📚 How It Works

1. The user inputs 5 symptoms via the app interface.
2. Symptoms are encoded using the `symptoms_encoder.pkl` file.
3. The encoded input is fed into a pre-trained Random Forest Classifier model.
4. The model predicts whether the condition is **Dangerous** or **Not Dangerous**.
5. The results are displayed interactively, with animations and visual cues.

---

## 🖥️ Application Preview

1. Open the app in your browser after running locally.
2. Select symptoms from the dropdown menu.
3. Click **Predict** to analyze if the condition is dangerous.
4. Explore additional resources like health tips and videos.

---

## 📊 Example Output

### Input Symptoms:
```
["Symptom1", "Symptom2", "Symptom3", "Symptom4", "Symptom5"]
```

### Prediction:
```
Result: The condition is Dangerous / Not Dangerous.
```

---

## 🛠️ Technologies Used

- **Python 3.8**
- **Streamlit** for the web interface
- **Scikit-learn** for machine learning
- **Pandas** for data processing
- **Joblib** for model serialization
- **Gemini API** for health prescriptions

---

## 📷 Logos and Badges

### Example Project Logo

![Animal Health Logo](https://s.tmimgcdn.com/scr/1204x1146/157100/animal-health-logo-template_157138-original.png)

---

## 🌐 Deployment

The application is deployed and maintained by **Aditya Chauhan**.

Stay informed, stay safe!

---

## 📋 Acknowledgments

Special thanks to:

- The open-source community for their resources.
- Streamlit for enabling rapid UI development.
