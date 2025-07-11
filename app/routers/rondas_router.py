from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.db import get_db
from app.cruds.rondas import (
    create_ronda,
    get_ronda,
    get_rondas,
    update_ronda,
    delete_ronda,
)

router = APIRouter(prefix="/rondas", tags=["Rondas"])

@router.get("/")
def get_rondas_endpoint(session=Depends(get_db)):
    rondas = get_rondas(session)
    return [{"id": r.id, "torneo_id": r.torneo_id, "numero": r.numero, "nombre": r.nombre} for r in rondas]

@router.get("/{ronda_id}")
def get_ronda_endpoint(ronda_id: int, session=Depends(get_db)):
    ronda = get_ronda(session, ronda_id)
    if not ronda:
        raise HTTPException(status_code=404, detail="Ronda not found")
    return {"id": ronda.id, "torneo_id": ronda.torneo_id, "numero": ronda.numero, "nombre": ronda.nombre}

@router.post("/")
def create_ronda_endpoint(torneo_id: int, numero: int, nombre: str, session=Depends(get_db)):
    ronda = create_ronda(session, torneo_id, numero, nombre)
    return {"id": ronda.id, "torneo_id": ronda.torneo_id, "numero": ronda.numero, "nombre": ronda.nombre}

@router.put("/{ronda_id}")
def update_ronda_endpoint(ronda_id: int, numero: Optional[int] = None, nombre: Optional[str] = None, session=Depends(get_db)):
    ronda = update_ronda(session, ronda_id, numero, nombre)
    if not ronda:
        raise HTTPException(status_code=404, detail="Ronda not found")
    return {"id": ronda.id, "torneo_id": ronda.torneo_id, "numero": ronda.numero, "nombre": ronda.nombre}

@router.delete("/{ronda_id}")
def delete_ronda_endpoint(ronda_id: int, session=Depends(get_db)):
    ronda = delete_ronda(session, ronda_id)
    if not ronda:
        raise HTTPException(status_code=404, detail="Ronda not found")
    return {"detail": "Ronda deleted successfully"}