from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.db import get_db
from app.cruds.grupos import (
    create_grupo,
    get_grupo,
    get_grupos,
    update_grupo,
    delete_grupo,
)

router = APIRouter(prefix="/grupos", tags=["Grupos"])

@router.get("/")
def get_grupos_endpoint(session=Depends(get_db)):
    grupos = get_grupos(session)
    return [{"id": g.id, "torneo_id": g.torneo_id, "nombre": g.nombre} for g in grupos]

@router.get("/{grupo_id}")
def get_grupo_endpoint(grupo_id: int, session=Depends(get_db)):
    grupo = get_grupo(session, grupo_id)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo not found")
    return {"id": grupo.id, "torneo_id": grupo.torneo_id, "nombre": grupo.nombre}

@router.post("/")
def create_grupo_endpoint(torneo_id: int, nombre: str, session=Depends(get_db)):
    grupo = create_grupo(session, torneo_id, nombre)
    return {"id": grupo.id, "torneo_id": grupo.torneo_id, "nombre": grupo.nombre}

@router.put("/{grupo_id}")
def update_grupo_endpoint(grupo_id: int, nombre: Optional[str] = None, session=Depends(get_db)):
    grupo = update_grupo(session, grupo_id, nombre)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo not found")
    return {"id": grupo.id, "torneo_id": grupo.torneo_id, "nombre": grupo.nombre}

@router.delete("/{grupo_id}")
def delete_grupo_endpoint(grupo_id: int, session=Depends(get_db)):
    grupo = delete_grupo(session, grupo_id)
    if not grupo:
        raise HTTPException(status_code=404, detail="Grupo not found")
    return {"detail": "Grupo deleted successfully"}