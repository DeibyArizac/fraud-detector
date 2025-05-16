import sys
import os
import pytest
from typing import Dict

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "src"))
from predict import FraudDetector

@pytest.fixture
def model_path() -> str:
    """Fixture for model path"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "model.pkl")

@pytest.fixture
def sample_transaction() -> Dict[str, float]:
    """Fixture for a sample transaction"""
    # Create a sample transaction with neutral values
    features = {f'V{i}': 0.0 for i in range(1, 29)}
    features.update({
        'Time': 0,
        'Amount': 100.0
    })
    return features

def test_model_loading(model_path):
    """Test that the model can be loaded"""
    try:
        detector = FraudDetector(model_path)
        assert detector.model is not None
    except Exception as e:
        pytest.fail(f"Failed to load model: {str(e)}")

def test_prediction_shape(model_path, sample_transaction):
    """Test that the prediction has the correct format"""
    detector = FraudDetector(model_path)
    result = detector.predict(sample_transaction)
    
    assert isinstance(result, dict)
    assert "prediction" in result
    assert isinstance(result["prediction"], int)
    assert result["prediction"] in [0, 1]

def test_prediction_consistency(model_path, sample_transaction):
    """Test that predictions are consistent for the same input"""
    detector = FraudDetector(model_path)
    result1 = detector.predict(sample_transaction)
    result2 = detector.predict(sample_transaction)
    
    assert result1 == result2
