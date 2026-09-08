
# 1. Abrimos el archivo de logs en modo lectura
with open("servidor_auth.log", "r") as archivo:
        lineas = archivo.readlines()
    
    # Diccionario para agrupar las IPs y contar intentos
conteo_ips = {}
    
    # 2. Recorremos el archivo línea por línea
for linea in lineas:
    if "ERROR" in linea:
            palabras = linea.split()
            ip = palabras[-1]
            
            # Si la IP ya estaba en el diccionario, sumamos 1. Si no, arranca en 1
            if ip in conteo_ips:
                conteo_ips[ip] = conteo_ips[ip] + 1
            else:
                conteo_ips[ip] = 1

# 3. Reporte final agrupado
print("--------------------------------")
print("📊 REPORTE DE AMENAZAS DETECTADAS:")
for ip, cantidad in conteo_ips.items():
    print(f"🚨 IP: {ip} -> {cantidad} intentos fallidos")
print("--------------------------------")
