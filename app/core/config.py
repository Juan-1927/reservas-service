import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Microservicio Reservas / Disponibilidad"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/reservas_db")
    INTEGRATIONS_ENABLED: bool = os.getenv("INTEGRATIONS_ENABLED", "false").lower() == "true"
    
    # URLs de servicios externos para la reunión de integración
    USUARIOS_SERVICE_URL: str = os.getenv("USUARIOS_SERVICE_URL", "http://localhost:8002")
    VIAJES_SERVICE_URL: str = os.getenv("VIAJES_SERVICE_URL", "http://localhost:8006")

settings = Settings()