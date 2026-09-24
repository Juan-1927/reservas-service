from fastapi import FastAPI

from app.core.config import settings
from app.core.database import Base, engine
from app.api.v1.routes import router as api_router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


app.include_router(
    api_router,
    prefix=settings.API_V1_STR
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": settings.PROJECT_NAME
    } 