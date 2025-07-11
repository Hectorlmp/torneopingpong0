from sqlalchemy.orm import Session
from app.models import ParticipanteGrupo

def create_participante_grupo(session: Session, participante_id: int, grupo_id: int):
    relacion = ParticipanteGrupo(participante_id=participante_id, grupo_id=grupo_id)
    session.add(relacion)
    session.commit()
    return relacion

def get_participantes_grupos(session: Session):
    return session.query(ParticipanteGrupo).all()

def get_participante_grupo(session: Session, relacion_id: int):
    return session.get(ParticipanteGrupo, relacion_id)

def update_participante_grupo(session: Session, relacion_id: int, participante_id: int = None, grupo_id: int = None):
    relacion = session.get(ParticipanteGrupo, relacion_id)
    if relacion:
        if participante_id is not None:
            relacion.participante_id = participante_id
        if grupo_id is not None:
            relacion.grupo_id = grupo_id
        session.commit()
    return relacion

def delete_participante_grupo(session: Session, relacion_id: int):
    relacion = session.get(ParticipanteGrupo, relacion_id)
    if relacion:
        session.delete(relacion)
        session.commit()
        return relacion
    return None