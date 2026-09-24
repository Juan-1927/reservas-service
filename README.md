# Microservicio #4 - Reservas / Disponibilidad

Microservicio desarrollado en Python con FastAPI y PostgreSQL para el sistema distribuido UniRide.

## Requisitos
- Python 3.10+
- Docker y Docker Compose

## Ejecución Local
1. Crear entorno virtual: `python -m venv .venv`
2. Activar entorno virtual e instalar dependencias: `pip install -r requirements.txt`
3. Levantar base de datos: `docker compose up -d`
4. Iniciar servidor: `uvicorn app.main:app --reload --port 8004`