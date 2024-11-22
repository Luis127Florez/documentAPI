# Usa una imagen base ligera de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos al contenedor
COPY requirements.txt .

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código del proyecto al contenedor
COPY . .

# Expone el puerto donde correrá FastAPI (por defecto 8000)
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
