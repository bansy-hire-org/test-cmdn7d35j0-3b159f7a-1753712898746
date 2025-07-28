from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Dict
import os

app = FastAPI()

# Mock data for charging stations
charging_stations = {
    1: {"id": 1, "location": "Bangalore", "capacity": 10, "available": 5},
    2: {"id": 2, "location": "Chennai", "capacity": 5, "available": 2},
}

# Mock data for vehicles
vehicles = {
    "V1": {"id": "V1", "location": "Bangalore", "battery": 80},
    "V2": {"id": "V2", "location": "Chennai", "battery": 30},
}

API_KEY = os.environ.get("API_KEY", "supersecretkey")

def api_key_auth(api_key: str = Depends(lambda api_key: api_key if api_key == API_KEY else None)):
    if not api_key:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key


class ChargingStation(BaseModel):
    id: int
    location: str
    capacity: int
    available: int


class Vehicle(BaseModel):
    id: str
    location: str
    battery: int


@app.get("/charging_stations", response_model=List[ChargingStation], dependencies=[Depends(api_key_auth)])
async def get_charging_stations():
    return list(charging_stations.values())


@app.get("/vehicles", response_model=List[Vehicle], dependencies=[Depends(api_key_auth)])
async def get_vehicles():
    return list(vehicles.values())


# Mock AI Agent - Simplest version. Better implementations include LLMs.
async def mock_ai_route_optimization(data: Dict):
    print(f"Received data for route optimization: {data}")
    # In reality, we would do LLM, RAG, and Pinecone searches here to get relevant routes.
    # This assumes we want to send the route to charging station with id 1.
    best_route = {"route": ["Depot", "Charging Station 1", "Destination"], "cost": 15}

    return best_route


@app.post("/optimize_route", dependencies=[Depends(api_key_auth)])
async def optimize_route(data: Dict):
    # Missing validation here. We should validate input data.
    result = await mock_ai_route_optimization(data)
    return result
