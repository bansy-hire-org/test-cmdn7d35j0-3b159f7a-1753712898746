from fastapi.testclient import TestClient
from backend.main import app, API_KEY

client = TestClient(app)


def test_get_charging_stations():
    headers = {"api_key": API_KEY}
    response = client.get("/charging_stations", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_charging_stations_unauthorized():
    headers = {"api_key": "wrongkey"}
    response = client.get("/charging_stations", headers=headers)
    assert response.status_code == 401


def test_get_vehicles():
    headers = {"api_key": API_KEY}
    response = client.get("/vehicles", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_optimize_route():
    headers = {"api_key": API_KEY}
    response = client.post("/optimize_route", json={"start": "A", "end": "B"}, headers=headers)
    assert response.status_code == 200
    assert "route" in response.json()
