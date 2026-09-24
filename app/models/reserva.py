from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.core.database import Base

class ReservaModel(Base):
    __tablename__ = "reservas"

    reserva_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, nullable=False, index=True)
    viaje_id = Column(Integer, nullable=False, index=True)
    fecha_reserva = Column(DateTime, default=datetime.utcnow, nullable=False)
    estado = Column(String(20), default="CONFIRMADA", nullable=False)  # PENDIENTE, CONFIRMADA, CANCELADA