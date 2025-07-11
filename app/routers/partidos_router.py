from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from datetime import datetime
from app.db import get_db
from app.cruds.partidos import (
    create_partido,
    get_partido,
    get_partidos,
    update_partido,
    delete_partido,
)

router = APIRouter(prefix="/partidos", tags=["Partidos"])

@router.get("/")
def get_partidos_endpoint(session=Depends(get_db)):
    partidos = get_partidos(session)
    return [{"id": p.id, "tipo": p.tipo} for p in partidos]

@router.get("/{partido_id}")
def get_partido_endpoint(partido_id: int, session=Depends(get_db)):
    partido = get_partido(session, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido not found")
    return {"id": partido.id, "tipo": partido.tipo, "horario": partido.horario.isoformat()}

@router.post("/")
def create_partido_endpoint(
    torneo_id: int,
    tipo: str,
    horario: datetime,
    mesa: int,
    jugador1_id: Optional[int] = None,
    jugador2_id: Optional[int] = None,
    equipo1_id: Optional[int] = None,
    equipo2_id: Optional[int] = None,
    session=Depends(get_db),
):
    partido = create_partido(session, torneo_id, tipo, horario, mesa, jugador1_id, jugador2_id, equipo1_id, equipo2_id)
    return {"id": partido.id, "tipo": partido.tipo}

@router.put("/{partido_id}")
def update_partido_endpoint(
    partido_id: int,
    tipo: Optional[str] = None,
    horario: Optional[datetime] = None,
    mesa: Optional[int] = None,
    jugador1_id: Optional[int] = None,
    jugador2_id: Optional[int] = None,
    equipo1_id: Optional[int] = None,
    equipo2_id: Optional[int] = None,
    session=Depends(get_db),
):
    partido = update_partido(session, partido_id, tipo, horario, mesa, jugador1_id, jugador2_id, equipo1_id, equipo2_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido not found")
    return {"id": partido.id, "tipo": partido.tipo}

@router.delete("/{partido_id}")
def delete_partido_endpoint(partido_id: int, session=Depends(get_db)):
    partido = delete_partido(session, partido_id)
    if not partido:
        raise HTTPException(status_code=404, detail="Partido not found")
    return {"detail": "Partido deleted successfully"}