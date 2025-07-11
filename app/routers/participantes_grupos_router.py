from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.participantes_grupos import (
    create_participante_grupo,
    get_participante_grupo,
    get_participantes_grupos,
    update_participante_grupo,
    delete_participante_grupo,
)

router = APIRouter(prefix="/participantes-grupos", tags=["Participantes Grupos"])

@router.get("/")
def get_participantes_grupos_endpoint(session=Depends(get_db)):
    relaciones = get_participantes_grupos(session)
    return [{"id": r.id, "participante_id": r.participante_id, "grupo_id": r.grupo_id} for r in relaciones]

@router.get("/{relacion_id}")
def get_participante_grupo_endpoint(relacion_id: int, session=Depends(get_db)):
    relacion = get_participante_grupo(session, relacion_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="ParticipanteGrupo not found")
    return {"id": relacion.id, "participante_id": relacion.participante_id, "grupo_id": relacion.grupo_id}

@router.post("/")
def create_participante_grupo_endpoint(participante_id: int, grupo_id: int, session=Depends(get_db)):
    relacion = create_participante_grupo(session, participante_id, grupo_id)
    return {"id": relacion.id, "participante_id": relacion.participante_id, "grupo_id": relacion.grupo_id}

@router.put("/{relacion_id}")
def update_participante_grupo_endpoint(relacion_id: int, participante_id: int = None, grupo_id: int = None, session=Depends(get_db)):
    relacion = update_participante_grupo(session, relacion_id, participante_id, grupo_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="ParticipanteGrupo not found")
    return {"id": relacion.id, "participante_id": relacion.participante_id, "grupo_id": relacion.grupo_id}

@router.delete("/{relacion_id}")
def delete_participante_grupo_endpoint(relacion_id: int, session=Depends(get_db)):
    relacion = delete_participante_grupo(session, relacion_id)
    if not relacion:
        raise HTTPException(status_code=404, detail="ParticipanteGrupo not found")
    return {"detail": "ParticipanteGrupo deleted successfully"}