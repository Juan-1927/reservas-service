import httpx
from app.core.config import settings
from fastapi import HTTPException, status


class ViajesClient:

    @staticmethod
    async def verificar_viaje_y_cupos(viaje_id: int):

        if not settings.INTEGRATIONS_ENABLED:
            # Simulación local
            return {
                "viaje_id": viaje_id,
                "capacidad": 4,
                "cupos_disponibles": 2,
                "valido": True
            }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    f"{settings.VIAJES_SERVICE_URL}/api/v1/viajes/{viaje_id}"
                )

                if response.status_code == 404:
                    raise HTTPException(
                        status_code=404,
                        detail="El viaje especificado no existe."
                    )

                if response.status_code != 200:
                    raise HTTPException(
                        status_code=500,
                        detail="Error al consultar el servicio de viajes."
                    )

                return response.json()

            except httpx.RequestError:
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="El servicio de Rutas/Viajes no se encuentra disponible."
                )