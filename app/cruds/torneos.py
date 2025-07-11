from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from app.models import Torneo

def create_torneo(session: Session, nombre: str,
                  fecha_inscripcion_inicio: date,
                  fecha_inscripcion_fin: date,
                  fecha_competencia_inicio: date,
                  fecha_competencia_fin: date,
                  mesas_disponibles: int):
    torneo = Torneo(
        nombre=nombre,
        fecha_inscripcion_inicio=fecha_inscripcion_inicio,
        fecha_inscripcion_fin=fecha_inscripcion_fin,
        fecha_competencia_inicio=fecha_competencia_inicio,
        fecha_competencia_fin=fecha_competencia_fin,
        mesas_disponibles=mesas_disponibles
    )
    session.add(torneo)
    session.commit()
    return torneo

def get_torneos(session: Session):
    return session.query(Torneo).all()

def get_torneo(session: Session, torneo_id: int):
    return session.get(Torneo, torneo_id)

def update_torneo(session: Session, torneo_id: int,
                  nombre: Optional[str] = None,
                  fecha_inscripcion_inicio: Optional[date] = None,
                  fecha_inscripcion_fin: Optional[date] = None,
                  fecha_competencia_inicio: Optional[date] = None,
                  fecha_competencia_fin: Optional[date] = None,
                  mesas_disponibles: Optional[int] = None):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        if nombre:
            torneo.nombre = nombre
        if fecha_inscripcion_inicio:
            torneo.fecha_inscripcion_inicio = fecha_inscripcion_inicio
        if fecha_inscripcion_fin:
            torneo.fecha_inscripcion_fin = fecha_inscripcion_fin
        if fecha_competencia_inicio:
            torneo.fecha_competencia_inicio = fecha_competencia_inicio
        if fecha_competencia_fin:
            torneo.fecha_competencia_fin = fecha_competencia_fin
        if mesas_disponibles is not None:
            torneo.mesas_disponibles = mesas_disponibles
        session.commit()
    return torneo

def delete_torneo(session: Session, torneo_id: int):
    torneo = session.get(Torneo, torneo_id)
    if torneo:
        session.delete(torneo)
        session.commit()
        return torneo
    return None
