from typing import Optional
from sqlalchemy.orm import Session
from app.models import Asociacion

def create_asociacion(session: Session, nombre: str, ciudad: Optional[str] = None, pais: Optional[str] = None):
    asociacion = Asociacion(nombre=nombre, ciudad=ciudad, pais=pais)
    session.add(asociacion)
    session.commit()
    return asociacion

def get_asociaciones(session: Session):
    return session.query(Asociacion).all()

def get_asociacion(session: Session, asociacion_id: int):
    return session.get(Asociacion, asociacion_id)

def update_asociacion(session: Session, asociacion_id: int,
                      nombre: Optional[str] = None,
                      ciudad: Optional[str] = None,
                      pais: Optional[str] = None):
    asociacion = session.get(Asociacion, asociacion_id)
    if asociacion:
        if nombre:
            asociacion.nombre = nombre
        if ciudad:
            asociacion.ciudad = ciudad
        if pais:
            asociacion.pais = pais
        session.commit()
    return asociacion

def delete_asociacion(session: Session, asociacion_id: int):
    asociacion = session.get(Asociacion, asociacion_id)
    if asociacion:
        session.delete(asociacion)
        session.commit()
        return asociacion
    return None
