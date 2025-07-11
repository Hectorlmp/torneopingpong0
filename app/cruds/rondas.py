from sqlalchemy.orm import Session
from typing import Optional
from app.models import Ronda

def create_ronda(session: Session, torneo_id: int, numero: int, nombre: str):
    ronda = Ronda(torneo_id=torneo_id, numero=numero, nombre=nombre)
    session.add(ronda)
    session.commit()
    return ronda

def get_rondas(session: Session):
    return session.query(Ronda).all()

def get_ronda(session: Session, ronda_id: int):
    return session.get(Ronda, ronda_id)

def update_ronda(session: Session, ronda_id: int, numero: Optional[int] = None, nombre: Optional[str] = None):
    ronda = session.get(Ronda, ronda_id)
    if ronda:
        if numero is not None:
            ronda.numero = numero
        if nombre is not None:
            ronda.nombre = nombre
        session.commit()
    return ronda

def delete_ronda(session: Session, ronda_id: int):
    ronda = session.get(Ronda, ronda_id)
    if ronda:
        session.delete(ronda)
        session.commit()
        return ronda
    return None