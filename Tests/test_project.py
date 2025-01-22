import unittest
import sys
import os

# Add the project root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.predict import predict

class TestAnimalHealthClassification(unittest.TestCase):
    
    def test_predict_function(self):
        """Test prediction with valid input data"""
        input_data = ["Mild Cough", "Normal Appetite", "Active Behavior", "Normal Temperature", "No Vomiting"]
        
        result = predict(input_data)
        print(f"Prediction result for input {input_data}: {result}")
        
        self.assertIn(result, ["Yes", "No"])  # Ensure output is Yes or No

    def test_empty_input(self):
        """Test prediction with empty input data"""
        input_data = []
        with self.assertRaises(ValueError):
            predict(input_data)

    def test_invalid_input(self):
        """Test prediction with invalid input types"""
        input_data = ["Mild Cough", None, 123, {}, []]
        with self.assertRaises(TypeError):
            predict(input_data)

if __name__ == "__main__":
    unittest.main()
