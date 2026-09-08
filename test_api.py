import urllib.request
import json

# La IP del atacante que encontramos en nuestro log
ip_atacante = "45.33.32.156"
url = f"http://ip-api.com/json/{ip_atacante}"

print(f"🛰️ Conectando con la API para rastrear la IP: {ip_atacante}...")

# 1. Hacemos la llamada HTTP a la API
respuesta = urllib.request.urlopen(url)

# 2. Convertimos el texto JSON a un Diccionario de Python
datos = json.loads(respuesta.read().decode())

# 3. Leemos los datos como cualquier diccionario
print("-----------------------------------------")
print(f"🌍 País del atacante: {datos['country']}")
print(f"🏙️ Ciudad:            {datos['city']}")
print(f"🏢 Proveedor (ISP):   {datos['isp']}")
print("-----------------------------------------")
