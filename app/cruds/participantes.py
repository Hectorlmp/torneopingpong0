from sqlalchemy.orm import Session
from app.models import Participante

def create_participante(session: Session, jugador_id: int, torneo_id: int, categoria_id: int):
    participante = Participante(
        jugador_id=jugador_id,
        torneo_id=torneo_id,
        categoria_id=categoria_id
    )
    session.add(participante)
    session.commit()
    return participante

def get_participantes(session: Session):
    return session.query(Participante).all()

def get_participante(session: Session, participante_id: int):
    return session.get(Participante, participante_id)

def update_participante(session: Session,
                         participante_id: int,
                         jugador_id: int = None,
                         torneo_id: int = None,
                         categoria_id: int = None):
    participante = session.get(Participante, participante_id)
    if participante:
        if jugador_id is not None:
            participante.jugador_id = jugador_id
        if torneo_id is not None:
            participante.torneo_id = torneo_id
        if categoria_id is not None:
            participante.categoria_id = categoria_id
        session.commit()
    return participante

def delete_participante(session: Session, participante_id: int):
    participante = session.get(Participante, participante_id)
    if participante:
        session.delete(participante)
        session.commit()
        return participante
    return None