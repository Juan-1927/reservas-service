from pydantic import BaseModel
from datetime import datetime


class ReservaCreate(BaseModel):
    usuario_id: int
    viaje_id: int


class ReservaResponse(BaseModel):
    reserva_id: int
    usuario_id: int
    viaje_id: int
    fecha_reserva: datetime
    estado: str

    class Config:
        from_attributes = True


class DisponibilidadResponse(BaseModel):
    viaje_id: int
    capacidad: int
    cupos_disponibles: int
    disponible: bool