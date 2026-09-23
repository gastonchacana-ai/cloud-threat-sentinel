from fastapi.testclient import TestClient
from servidor import app
import os

client = TestClient(app)

def test_inicio_operativo():
    """Verifica que la raíz de la API responda 200 OK y esté operativa."""
    response = client.get("/")
    assert response.status_code == 200
    datos = response.json()
    assert datos["estado"] == "Operativo"
    assert datos["nivel"] == 6

def test_amenazas_sin_token_rechazado():
    """Verifica el blindaje: Si no se envía token, debe rechazar con 401."""
    response = client.get("/amenazas")
    assert response.status_code == 401
    assert "Acceso denegado" in response.json()["detail"]

def test_amenazas_con_token_query_exitoso():
    """Verifica acceso autorizado mediante query param ?token=..."""
    response = client.get("/amenazas?token=super-secreto-cloud-2026")
    assert response.status_code == 200
    datos = response.json()
    assert "total_amenazas" in datos
    assert "amenazas" in datos
    assert isinstance(datos["amenazas"], list)

def test_amenazas_con_header_exitoso():
    """Verifica acceso autorizado mediante HTTP Header X-API-Token."""
    headers = {"X-API-Token": "super-secreto-cloud-2026"}
    response = client.get("/amenazas", headers=headers)
    assert response.status_code == 200
    datos = response.json()
    assert datos["total_amenazas"] >= 1
