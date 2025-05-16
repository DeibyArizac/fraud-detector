import os
import joblib
import numpy as np
from typing import Dict, Union

class FraudDetector:
    def __init__(self, model_path: str = "../models/model.pkl"):
        """
        Initialize the fraud detector with the trained model.
        
        This model has been specifically optimized to detect fraud patterns
        in credit card transactions, using PCA-transformed features to protect
        the privacy of the original data. The model achieves high accuracy while
        maintaining data confidentiality through dimensionality reduction.
        
        Args:
            model_path: Path to the saved model file
        """
        self.model = joblib.load(model_path)
        
    def predict(self, features: Dict[str, float]) -> Dict[str, int]:
        """
        Make a prediction for a single transaction
        
        Args:
            features: Dictionary containing the 30 input features (V1-V28, Time, Amount)
            
        Returns:
            Dictionary with the prediction (0 for legitimate, 1 for fraud)
        """
        # Convert input features to numpy array in the correct order
        feature_names = ['Time', 'Amount'] + [f'V{i}' for i in range(1, 29)]
        X = np.array([features[name] for name in feature_names]).reshape(1, -1)
        
        # Make prediction
        prediction = int(self.model.predict(X)[0])
        return {"prediction": prediction}

if __name__ == "__main__":
    # Example usage
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(os.path.dirname(current_dir), "models", "model.pkl")
    
    # Create an instance of FraudDetector
    detector = FraudDetector(model_path)
    
    # Example feature vector (you would replace these values with real data)
    example_features = {f'V{i}': 0.0 for i in range(1, 29)}
    example_features.update({
        'Time': 0,
        'Amount': 100.0
    })
    
    # Make prediction
    result = detector.predict(example_features)
    print(f"Prediction: {'Fraud' if result['prediction'] == 1 else 'Legitimate'}")
