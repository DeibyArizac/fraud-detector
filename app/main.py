from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "src"))
from predict import FraudDetector

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="""
    API for detecting fraudulent credit card transactions.
    Developed by Deiby Ariza as part of ML projects portfolio.
    
    This system uses an optimized XGBoost model to detect fraud patterns
    in real-time, achieving over 99% accuracy.
    """,
    version="1.0.0",
    contact={
        "name": "Deiby Ariza",
        "url": "https://github.com/deibyariza",
        "email": "deibyariza@example.com"  # Replace with your actual email
    }
)

class Transaction(BaseModel):
    """
    Pydantic model for transaction input validation
    """
    Time: float = Field(..., description="Time elapsed between this transaction and the first transaction")
    Amount: float = Field(..., description="Transaction amount")
    V1: float = Field(..., description="PCA component 1")
    V2: float = Field(..., description="PCA component 2")
    V3: float = Field(..., description="PCA component 3")
    V4: float = Field(..., description="PCA component 4")
    V5: float = Field(..., description="PCA component 5")
    V6: float = Field(..., description="PCA component 6")
    V7: float = Field(..., description="PCA component 7")
    V8: float = Field(..., description="PCA component 8")
    V9: float = Field(..., description="PCA component 9")
    V10: float = Field(..., description="PCA component 10")
    V11: float = Field(..., description="PCA component 11")
    V12: float = Field(..., description="PCA component 12")
    V13: float = Field(..., description="PCA component 13")
    V14: float = Field(..., description="PCA component 14")
    V15: float = Field(..., description="PCA component 15")
    V16: float = Field(..., description="PCA component 16")
    V17: float = Field(..., description="PCA component 17")
    V18: float = Field(..., description="PCA component 18")
    V19: float = Field(..., description="PCA component 19")
    V20: float = Field(..., description="PCA component 20")
    V21: float = Field(..., description="PCA component 21")
    V22: float = Field(..., description="PCA component 22")
    V23: float = Field(..., description="PCA component 23")
    V24: float = Field(..., description="PCA component 24")
    V25: float = Field(..., description="PCA component 25")
    V26: float = Field(..., description="PCA component 26")
    V27: float = Field(..., description="PCA component 27")
    V28: float = Field(..., description="PCA component 28")

# Initialize the model
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "models", "model.pkl")
detector = FraudDetector(model_path)

@app.post("/predict", response_model=Dict[str, int])
async def predict_fraud(transaction: Transaction):
    """
    Predict whether a transaction is fraudulent
    
    Args:
        transaction: Transaction details
        
    Returns:
        Dictionary with prediction (0 for legitimate, 1 for fraud)
    """
    try:
        features = transaction.dict()
        result = detector.predict(features)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Credit Card Fraud Detection API",
        "version": "1.0.0",
        "description": "API for detecting fraudulent credit card transactions"
    }
