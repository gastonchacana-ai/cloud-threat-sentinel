from fastapi import FastAPI
import urllib.request
import json

# 1. Creamos la instancia de nuestra API
app = FastAPI(title="Centro de Monitoreo de Seguridad")

# 2. Rutas básicas de estado
@app.get("/")
def inicio():
    return {
        "sistema": "Servidor de Detección de Amenazas",
        "estado": "Operativo",
        "agente": "Gaston",
        "nivel": 4
    }

@app.get("/saludo")
def saludar():
    return {"mensaje": "¡Hola Mundo desde mi primer Servidor API!"}

# 3. 🚨 NUEVA RUTA: Centro de Detección de Amenazas en Vivo
@app.get("/amenazas")
def obtener_amenazas():
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