from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.schemas.reserva import (
    ReservaCreate,
    ReservaResponse,
    DisponibilidadResponse
)
from app.services.reserva_service import ReservaService
from app.clients.viajes_client import ViajesClient


router = APIRouter()


@router.post(
    "/reservas",
    response_model=ReservaResponse,
    status_code=status.HTTP_201_CREATED
)
async def crear_reserva(
    datos: ReservaCreate,
    db: Session = Depends(get_db)
):
    viaje_info = await ViajesClient.verificar_viaje_y_cupos(
        datos.viaje_id
    )

    if viaje_info.get("cupos_disponibles", 0) <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No hay cupos disponibles para realizar la reserva."
        )

    return ReservaService.crear_reserva(db, datos)


@router.get(
    "/reservas/{reserva_id}",
    response_model=ReservaResponse
)
def obtener_reserva(
    reserva_id: int,
    db: Session = Depends(get_db)
):
    reserva = ReservaService.obtener_por_id(
        db,
        reserva_id
    )

    if not reserva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reserva no encontrada."
        )

    return reserva


@router.get(
    "/reservas/usuario/{usuario_id}",
    response_model=List[ReservaResponse]
)
def obtener_reservas_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    return ReservaService.obtener_por_usuario(
        db,
        usuario_id
    )


@router.put(
    "/reservas/{reserva_id}/cancelar",
    response_model=ReservaResponse
)
def cancelar_reserva(
    reserva_id: int,
    db: Session = Depends(get_db)
):
    reserva = ReservaService.cancelar_reserva(
        db,
        reserva_id
    )

    if not reserva:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Reserva no encontrada."
        )

    return reserva


@router.get(
    "/viajes/{viaje_id}/disponibilidad",
    response_model=DisponibilidadResponse
)
async def consultar_disponibilidad(viaje_id: int):
    viaje_info = await ViajesClient.verificar_viaje_y_cupos(
        viaje_id
    )

    return {
        "viaje_id": viaje_id,
        "capacidad": viaje_info.get("capacidad", 0),
        "cupos_disponibles": viaje_info.get(
            "cupos_disponibles",
            0
        ),
        "disponible": viaje_info.get(
            "cupos_disponibles",
            0
        ) > 0
    }