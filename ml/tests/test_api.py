import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Kairos API"}

def test_predict_endpoint():
    response = client.post("/predict", json={"data": [1, 2, 3]})
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_train_endpoint():
    response = client.post("/train", json={"data": [1, 2, 3], "labels": [0, 1, 0]})
    assert response.status_code == 200
    assert response.json() == {"message": "Training completed successfully"}