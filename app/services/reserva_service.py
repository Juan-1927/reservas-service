from sqlalchemy.orm import Session
from app.models.reserva import ReservaModel
from app.schemas.reserva import ReservaCreate
from datetime import datetime

class ReservaService:

    @staticmethod
    def crear_reserva(db: Session, datos: ReservaCreate) -> ReservaModel:
        nueva_reserva = ReservaModel(
            usuario_id=datos.usuario_id,
            viaje_id=datos.viaje_id,
            fecha_reserva=datetime.utcnow(),
            estado="CONFIRMADA"
        )
        db.add(nueva_reserva)
        db.commit()
        db.refresh(nueva_reserva)
        return nueva_reserva

    @staticmethod
    def obtener_por_id(db: Session, reserva_id: int) -> ReservaModel:
        return db.query(ReservaModel).filter(ReservaModel.reserva_id == reserva_id).first()

    @staticmethod
    def obtener_por_usuario(db: Session, usuario_id: int):
        return db.query(ReservaModel).filter(ReservaModel.usuario_id == usuario_id).all()

    @staticmethod
    def cancelar_reserva(db: Session, reserva_id: int) -> ReservaModel:
        reserva = ReservaService.obtener_por_id(db, reserva_id)
        if reserva:
            reserva.estado = "CANCELADA"
            db.commit()
            db.refresh(reserva)
        return reserva