from fastapi import FastAPI
    
# 1. Creamos la instancia de nuestra API
app = FastAPI(title="Centro de Monitoreo de Seguridad")

# 2. Definimos la ruta raíz (cuando alguien entra a la dirección principal)
@app.get("/")
def inicio():
    return {
        "sistema": "Servidor de Detección de Amenazas",
        "estado": "Operativo",
        "agente": "Gaston",
        "nivel": 4
    }

# 3. Definimos una ruta adicional de prueba
@app.get("/saludo")
def saludar():
    return {"mensaje": "¡Hola Mundo desde mi primer Servidor API!"}