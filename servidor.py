from fastapi import FastAPI, Header, Query, HTTPException, status
import urllib.request
import json
import os

# 1. Creamos la instancia de nuestra API
app = FastAPI(
    title="Centro de Monitoreo de Seguridad",
    description="API Centinela protegida por Azure Key Vault",
    version="2.0.0"
)

# 2. Obtenemos el secreto inyectado desde Azure Key Vault (o valor por defecto local)
API_SECRET = os.getenv("API_SECRET_TOKEN", "super-secreto-cloud-2026")

# 3. Rutas básicas de estado
@app.get("/")
def inicio():
    return {
        "sistema": "Servidor de Detección de Amenazas",
        "estado": "Operativo",
        "agente": "Gaston",
        "nivel": 6,
        "seguridad": "Azure Key Vault Activo 🔐"
    }

@app.get("/saludo")
def saludar():
    return {"mensaje": "¡Hola Mundo desde mi primer Servidor API!"}

# 4. 🚨 RUTA BLINDADA: Centro de Detección de Amenazas (Requiere Token)
@app.get("/amenazas")
def obtener_amenazas(
    token: str = Query(None, description="Token secreto de acceso"),
    x_api_token: str = Header(None, alias="X-API-Token", description="Header de seguridad")
):
    token_recibido = token or x_api_token

    # 🛑 Control de Acceso: Si el token no coincide, rechazamos con HTTP 401
    if token_recibido != API_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="⛔ Acceso denegado: Token de seguridad inválido o ausente."
        )
    # Leemos el archivo de log
    with open("servidor_auth.log", "r") as archivo:
        lineas = archivo.readlines()

    # Contamos intentos por cada IP
    conteo_ips = {}
    for linea in lineas:
        if "ERROR" in linea:
            palabras = linea.split()
            ip = palabras[-1]
            conteo_ips[ip] = conteo_ips.get(ip, 0) + 1

    # Consultamos la API externa para cada IP sospechosa
    lista_amenazas = []
    for ip, cantidad in conteo_ips.items():
        url = f"http://ip-api.com/json/{ip}"
        respuesta = urllib.request.urlopen(url)
        datos = json.loads(respuesta.read().decode())

        lista_amenazas.append({
            "ip": ip,
            "intentos": cantidad,
            "pais": datos.get("country", "Desconocido"),
            "ciudad": datos.get("city", "Desconocida"),
            "isp": datos.get("isp", "Desconocido")
        })

    # Devolvemos el reporte completo estructurado
    return {
        "total_amenazas": len(lista_amenazas),
        "amenazas": lista_amenazas
    }