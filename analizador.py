import urllib.request
import json

# 1. Abrimos el archivo de logs en modo lectura
with open("servidor_auth.log", "r") as archivo:
    lineas = archivo.readlines()

# Diccionario para agrupar las IPs y contar intentos
conteo_ips = {}

# 2. Recorremos el archivo línea por línea buscando atacantes
for linea in lineas:
    if "ERROR" in linea:
        palabras = linea.split()
        ip = palabras[-1]
        
        # Si la IP ya estaba en el diccionario sumamos 1, sino empieza en 1
        if ip in conteo_ips:
            conteo_ips[ip] = conteo_ips[ip] + 1
        else:
            conteo_ips[ip] = 1

# 3. Reporte final con Inteligencia de Amenazas en Vivo
print("----------------------------------------------------------------------")
print("🛡️  REPORTE DE CIBERSEGURIDAD: AMENAZAS DETECTADAS Y GEOLOCALIZADAS")
print("----------------------------------------------------------------------")

for ip, cantidad in conteo_ips.items():
    # Consultamos a la API de internet para ESTA IP específica
    url = f"http://ip-api.com/json/{ip}"
    respuesta = urllib.request.urlopen(url)
    datos = json.loads(respuesta.read().decode())
    
    pais = datos.get("country", "Desconocido")
    ciudad = datos.get("city", "Desconocida")
    isp = datos.get("isp", "Desconocido")

    print(f"🚨 IP: {ip} | Intentos: {cantidad} | Origen: {pais} ({ciudad}) | Red: {isp}")

print("----------------------------------------------------------------------")
