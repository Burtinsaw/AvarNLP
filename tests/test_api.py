from fastapi.testclient import TestClient
from src.api.server import app

client = TestClient(app)

def test_health_endpoint():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_translate_endpoint_structure():
    resp = client.post("/translate", json={"text": "Салам", "direction": "av-tr"})
    assert resp.status_code == 200
    data = resp.json()
    assert "translation" in data
    assert "direction" in data

def test_translate_invalid_direction():
    resp = client.post("/translate", json={"text": "Hello", "direction": "en-fr"})
    assert resp.status_code == 400
