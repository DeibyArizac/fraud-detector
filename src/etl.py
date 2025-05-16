import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple
import os

def load_data(data_path: str = "../data/raw/creditcard.csv") -> pd.DataFrame:
    """
    Load the credit card fraud detection dataset
    
    Args:
        data_path: Path to the CSV file
        
    Returns:
        DataFrame containing the dataset
    """
    return pd.read_csv(data_path)

def prepare_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Prepare data for training by splitting features and target, and creating train/test sets
    
    Args:
        df: Input DataFrame
        test_size: Proportion of dataset to include in the test split
        random_state: Random state for reproducibility
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    # Separate features (X) and target (y)
    X = df.drop('Class', axis=1)
    y = df['Class']
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Example usage
    data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw", "creditcard.csv")
    df = load_data(data_path)
    X_train, X_test, y_train, y_test = prepare_data(df)
    print(f"Training set shape: {X_train.shape}")
    print(f"Testing set shape: {X_test.shape}")
    print(f"Fraud cases in training set: {sum(y_train)}")
    print(f"Fraud cases in testing set: {sum(y_test)}")
