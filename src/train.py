import os
import joblib
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from etl import load_data, prepare_data

def train_model(X_train, X_test, y_train, y_test, model_path: str = "../models/model.pkl") -> None:
    """
    Train an XGBoost classifier and save it to disk
    
    Args:
        X_train: Training features
        X_test: Test features
        y_train: Training labels
        y_test: Test labels
        model_path: Path where to save the trained model
    """
    # Initialize and train the model
    model = XGBClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        random_state=42,
        use_label_encoder=False,
        eval_metric='logloss'
    )
    
    print("Training model...")
    model.fit(X_train, y_train)
    
    # Evaluate the model
    print("\nModel Performance:")
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Save the model
    print(f"\nSaving model to {model_path}")
    joblib.dump(model, model_path)
    print("Model saved successfully!")

if __name__ == "__main__":
    # Load and prepare data
    current_dir = os.path.dirname(__file__)
    data_path = os.path.join(os.path.dirname(current_dir), "data", "raw", "creditcard.csv")
    model_path = os.path.join(os.path.dirname(current_dir), "models", "model.pkl")
    
    print("Loading data...")
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = prepare_data(df)
    
    # Train and save model
    train_model(X_train, X_test, y_train, y_test, model_path)
