from fastapi import FastAPI
from app.utils.validation import validate_schema_consistency
from app.utils.model_helper import predict

app = FastAPI(title="Fraud Prediction API")

@app.get("/")
def root():
    return {"message": "Fraud Prediction API is running"}

from fastapi import FastAPI

app = FastAPI()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is running!"}

@app.post("/predict")
def predict_endpoint(data: dict):
    # contoh sederhana: langsung return data
    return {"prediction": data}



