# Credit Card Fraud Detection System

![Fraud Detection](https://img.shields.io/badge/ML-Fraud%20Detection-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Build](https://img.shields.io/badge/Build-Passing-success)

A production-ready machine learning system designed to detect fraudulent credit card transactions in real-time. This project implements a complete ML pipeline from data processing to API deployment, with a focus on real-world applications.

## 📚 Documentation
- [Technical Documentation](docs/technical_documentation.md) - Detailed explanation of the system architecture and components
- [Implementation Guide](docs/implementation_guide.md) - Step-by-step guide for real-world implementation
- [API Documentation](http://localhost:8000/docs) - Interactive API documentation (when server is running)

## Overview
Developed by Deiby Ariza as part of a data science and machine learning portfolio. This project showcases advanced predictive modeling techniques for identifying fraud patterns in real-time transactions.

### Key Features:
- Real-time data processing
- Optimized XGBoost model
- REST API with FastAPI
- Detailed metric analysis
- Automated testing

## Project Structure

```
fraud-detector/
├── data/
│   └── raw/creditcard.csv
├── models/
│   └── model.pkl
├── src/
│   ├── etl.py
│   ├── train.py
│   ├── predict.py
├── app/
│   └── main.py
├── notebooks/
│   └── metrics.ipynb
├── tests/
│   └── test_predict.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/deibyariza/fraud-detector.git
cd fraud-detector
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download the dataset:
- Download `creditcard.csv` from [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Place it in the `data/raw/` directory

## Usage

### Training the Model

To train the model:

```bash
cd src
python train.py
```

This will:
- Load and preprocess the data
- Train an XGBoost classifier
- Save the model to `models/model.pkl`
- Print performance metrics

### Running the API

To start the FastAPI server:

```bash
cd app
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Making Predictions

You can make predictions using curl:

```bash
curl -X POST "http://localhost:8000/predict" -H "Content-Type: application/json" -d "{\"Time\":0,\"Amount\":100.0,\"V1\":0.0,\"V2\":0.0,...}"
```

Or use the Swagger UI at `http://localhost:8000/docs`

### Running Tests

To run the test suite:

```bash
pytest tests/
```

## Model Analysis

The `notebooks/metrics.ipynb` Jupyter notebook contains:
- Exploratory data analysis
- Model performance metrics
- Visualizations of results

To view the notebook:
```bash
jupyter notebook notebooks/metrics.ipynb
```

## API Documentation

### Endpoints

- `GET /`: API information
- `POST /predict`: Make fraud prediction
  - Input: JSON with transaction features
  - Output: `{"prediction": 0}` for legitimate or `{"prediction": 1}` for fraud

## Technologies Used

- Python 3.8+
- XGBoost
- FastAPI
- scikit-learn
- pandas
- Jupyter
- pytest

## Author

**Deiby Ariza**
- GitHub: [@deibyariza](https://github.com/deibyariza)
- Portfolio Project
- Built in 2025

## License

MIT

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
