import pickle
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

with open("scaler_average_weight.pkl", "rb") as f:
    scaler_average_weight = pickle.load(f)

with open("scaler_revenue.pkl", "rb") as f:
    scaler_revenue = pickle.load(f)
    
with open("model_revenue.pkl", "rb") as f:
    model_revenue = pickle.load(f)
    
with open("model_average_weight.pkl", "rb") as f:
    model_average_weight = pickle.load(f)

class revenue_data(BaseModel):
    size: float
    weight: float
    number_of_shrimp: float

class average_weight_data(BaseModel):
    tray_number: float
    quantity: float
    fasting: float

@app.get('/')
def main():
    return {'message': 'Welcome to GeeksforGeeks!'}

@app.post("/predict/revenue")
async def predict_revenue(data_info: revenue_data):
    data = []
    data.append(data_info.size)
    data.append(data_info.weight)
    data.append(data_info.number_of_shrimp)
    scaled = scaler_revenue.transform([data])
    predictions = model_revenue.predict(scaled)
    
    return {
        "predictions" : predictions[0]
    }
    
@app.post("/predict/weight")
async def predict_revenue(data_info: average_weight_data):
    data = []
    data.append(data_info.tray_number)
    data.append(data_info.quantity)
    data.append(data_info.fasting)
    scaled = scaler_average_weight.transform([data])
    predictions = model_average_weight.predict(scaled)
    
    return {
        "predictions" : predictions[0]
    }