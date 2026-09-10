# 1. El cimiento: Una versión oficial y ultra liviana de Linux con Python 3.12
FROM python:3.12-slim

# 2. Carpeta de trabajo adentro del contenedor

# 3. Copiamos la lista de ingredientes e instalamos las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos nuestro código y el archivo de log adentro de la caja
COPY servidor.py .
COPY servidor_auth.log .

# 5. Avisamos que el contenedor escucha en el puerto 8000
EXPOSE 8000

# 6. El comando que arranca el servidor automáticamente
CMD ["uvicorn", "servidor:app", "--host", "0.0.0.0", "--port", "8000"]
