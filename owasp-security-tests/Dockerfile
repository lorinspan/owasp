# Folosim imaginea oficială Python
FROM python:3.11

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele de test și dependențele
COPY requirements.txt .

# Instalăm pachetele necesare
RUN pip install --no-cache-dir -r requirements.txt

# Copiem toate fișierele de test
COPY . .

# Comanda implicită pentru rularea testelor
CMD ["pytest", "-s"]