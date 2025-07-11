from sqlalchemy.orm import Session
from app.models import Set
from typing import Optional

def create_set(session: Session, partido_id: int, numero_set: int, puntos_jugador1: int, puntos_jugador2: int):
    nuevo_set = Set(
        partido_id=partido_id,
        numero_set=numero_set,
        puntos_jugador1=puntos_jugador1,
        puntos_jugador2=puntos_jugador2
    )
    session.add(nuevo_set)
    session.commit()
    return nuevo_set

def get_sets(session: Session):
    return session.query(Set).all()

def get_set(session: Session, set_id: int):
    return session.get(Set, set_id)

def update_set(session: Session, set_id: int, numero_set: Optional[int] = None,
               puntos_jugador1: Optional[int] = None, puntos_jugador2: Optional[int] = None):
    set_obj = session.get(Set, set_id)
    if set_obj:
        if numero_set is not None:
            set_obj.numero_set = numero_set
        if puntos_jugador1 is not None:
            set_obj.puntos_jugador1 = puntos_jugador1
        if puntos_jugador2 is not None:
            set_obj.puntos_jugador2 = puntos_jugador2
        session.commit()
    return set_obj

def delete_set(session: Session, set_id: int):
    set_obj = session.get(Set, set_id)
    if set_obj:
        session.delete(set_obj)
        session.commit()
        return set_obj
    return None