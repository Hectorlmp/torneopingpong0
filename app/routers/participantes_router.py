from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.participantes import (
    create_participante,
    get_participante,
    get_participantes,
    update_participante,
    delete_participante,
)

router = APIRouter(prefix="/participantes", tags=["Participantes"])

@router.get("/")
def get_participantes_endpoint(session=Depends(get_db)):
    participantes = get_participantes(session)
    return [{"id": p.id, "jugador_id": p.jugador_id, "torneo_id": p.torneo_id, "categoria_id": p.categoria_id} for p in participantes]

@router.get("/{participante_id}")
def get_participante_endpoint(participante_id: int, session=Depends(get_db)):
    participante = get_participante(session, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante not found")
    return {"id": participante.id, "jugador_id": participante.jugador_id, "torneo_id": participante.torneo_id, "categoria_id": participante.categoria_id}

@router.post("/")
def create_participante_endpoint(
    jugador_id: int,
    torneo_id: int,
    categoria_id: int,
    session=Depends(get_db),
):
    participante = create_participante(session, jugador_id, torneo_id, categoria_id)
    return {"id": participante.id, "jugador_id": participante.jugador_id}

@router.put("/{participante_id}")
def update_participante_endpoint(
    participante_id: int,
    jugador_id: int = None,
    torneo_id: int = None,
    categoria_id: int = None,
    session=Depends(get_db),
):
    participante = update_participante(session, participante_id, jugador_id, torneo_id, categoria_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante not found")
    return {"id": participante.id, "jugador_id": participante.jugador_id}

@router.delete("/{participante_id}")
def delete_participante_endpoint(participante_id: int, session=Depends(get_db)):
    participante = delete_participante(session, participante_id)
    if not participante:
        raise HTTPException(status_code=404, detail="Participante not found")
    return {"detail": "Participante deleted successfully"}