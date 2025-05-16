import requests
import json

# URL de la API
url = "http://localhost:8000/predict"

# Datos de ejemplo para la predicción
data = {
    "Time": 0,
    "Amount": 100.0,
    "V1": -1.9598071336738172,
    "V2": -0.0727811733098497,
    "V3": 2.536346738618042,
    "V4": 1.978155224101747,
    "V5": -0.338321856591981,
    "V6": 0.462387777762292,
    "V7": 0.239598554061257,
    "V8": 0.098697901967912,
    "V9": 0.363787375558171,
    "V10": 0.090794172742772,
    "V11": -0.851599533260813,
    "V12": -0.617800855762348,
    "V13": -0.991389847235408,
    "V14": -0.311169353699879,
    "V15": 1.468176972444344,
    "V16": -0.470400525259478,
    "V17": 0.807971241929242,
    "V18": 0.025790930276891,
    "V19": 0.403992960255733,
    "V20": 0.251412098239705,
    "V21": -0.018306777944153,
    "V22": 0.277837575558899,
    "V23": -0.110473910188767,
    "V24": 0.066928075074387,
    "V25": 0.128539358273528,
    "V26": -0.189114843888824,
    "V27": 0.433558376740387,
    "V28": -0.021053053283880
}

try:
    # Hacer la petición POST
    response = requests.post(url, json=data)
    
    # Verificar si la petición fue exitosa
    if response.status_code == 200:
        print("Predicción exitosa!")
        print(f"Resultado: {response.json()}")
        print(f"La transacción es: {'Fraudulenta' if response.json()['prediction'] == 1 else 'Legítima'}")
    else:
        print(f"Error: {response.status_code}")
        print(f"Mensaje: {response.text}")
        
except requests.exceptions.ConnectionError:
    print("Error: No se pudo conectar al servidor. Asegúrate de que el servidor FastAPI esté corriendo.")
except Exception as e:
    print(f"Error inesperado: {str(e)}")
