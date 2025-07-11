from typing import Optional
from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.torneos import (
    create_torneo,
    get_torneo,
    get_torneos,
    update_torneo,
    delete_torneo,
)

router = APIRouter(prefix="/torneos", tags=["Torneos"])

@router.get("/")
def get_torneos_endpoint(session=Depends(get_db)):
    torneos = get_torneos(session)
    return [{"id": t.id, "nombre": t.nombre} for t in torneos]

@router.get("/{torneo_id}")
def get_torneo_endpoint(torneo_id: int, session=Depends(get_db)):
    torneo = get_torneo(session, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo not found")
    return {"id": torneo.id, "nombre": torneo.nombre}

@router.post("/")
def create_torneo_endpoint(
    nombre: str,
    fecha_inscripcion_inicio: date,
    fecha_inscripcion_fin: date,
    fecha_competencia_inicio: date,
    fecha_competencia_fin: date,
    mesas_disponibles: int,
    session=Depends(get_db),
):
    torneo = create_torneo(session, nombre, fecha_inscripcion_inicio,
                            fecha_inscripcion_fin, fecha_competencia_inicio,
                            fecha_competencia_fin, mesas_disponibles)
    return {"id": torneo.id, "nombre": torneo.nombre}

@router.put("/{torneo_id}")
def update_torneo_endpoint(
    torneo_id: int,
    nombre: Optional[str] = None,
    fecha_inscripcion_inicio: Optional[date] = None,
    fecha_inscripcion_fin: Optional[date] = None,
    fecha_competencia_inicio: Optional[date] = None,
    fecha_competencia_fin: Optional[date] = None,
    mesas_disponibles: Optional[int] = None,
    session=Depends(get_db),
):
    torneo = update_torneo(session, torneo_id, nombre,
                           fecha_inscripcion_inicio, fecha_inscripcion_fin,
                           fecha_competencia_inicio, fecha_competencia_fin,
                           mesas_disponibles)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo not found")
    return {"id": torneo.id, "nombre": torneo.nombre}

@router.delete("/{torneo_id}")
def delete_torneo_endpoint(torneo_id: int, session=Depends(get_db)):
    torneo = delete_torneo(session, torneo_id)
    if not torneo:
        raise HTTPException(status_code=404, detail="Torneo not found")
    return {"detail": "Torneo deleted successfully"}