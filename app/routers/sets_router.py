from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.db import get_db
from app.cruds.sets import (
    create_set,
    get_set,
    get_sets,
    update_set,
    delete_set,
)

router = APIRouter(prefix="/sets", tags=["Sets"])

@router.get("/")
def get_sets_endpoint(session=Depends(get_db)):
    sets = get_sets(session)
    return [{"id": s.id, "partido_id": s.partido_id, "numero_set": s.numero_set} for s in sets]

@router.get("/{set_id}")
def get_set_endpoint(set_id: int, session=Depends(get_db)):
    set_obj = get_set(session, set_id)
    if not set_obj:
        raise HTTPException(status_code=404, detail="Set not found")
    return {
        "id": set_obj.id,
        "partido_id": set_obj.partido_id,
        "numero_set": set_obj.numero_set,
        "puntos_jugador1": set_obj.puntos_jugador1,
        "puntos_jugador2": set_obj.puntos_jugador2,
    }

@router.post("/")
def create_set_endpoint(
    partido_id: int,
    numero_set: int,
    puntos_jugador1: int,
    puntos_jugador2: int,
    session=Depends(get_db),
):
    set_obj = create_set(session, partido_id, numero_set, puntos_jugador1, puntos_jugador2)
    return {"id": set_obj.id, "partido_id": set_obj.partido_id}

@router.put("/{set_id}")
def update_set_endpoint(
    set_id: int,
    numero_set: Optional[int] = None,
    puntos_jugador1: Optional[int] = None,
    puntos_jugador2: Optional[int] = None,
    session=Depends(get_db),
):
    set_obj = update_set(session, set_id, numero_set, puntos_jugador1, puntos_jugador2)
    if not set_obj:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"id": set_obj.id, "partido_id": set_obj.partido_id}

@router.delete("/{set_id}")
def delete_set_endpoint(set_id: int, session=Depends(get_db)):
    set_obj = delete_set(session, set_id)
    if not set_obj:
        raise HTTPException(status_code=404, detail="Set not found")
    return {"detail": "Set deleted successfully"}