from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.equipos_dobles import (
    create_equipo_doble,
    get_equipo_doble,
    get_equipos_dobles,
    update_equipo_doble,
    delete_equipo_doble,
)

router = APIRouter(prefix="/equipos-dobles", tags=["Equipos Dobles"])

@router.get("/")
def get_equipos_dobles_endpoint(session=Depends(get_db)):
    equipos = get_equipos_dobles(session)
    return [{"id": e.id, "jugador1_id": e.jugador1_id, "jugador2_id": e.jugador2_id} for e in equipos]

@router.get("/{equipo_id}")
def get_equipo_doble_endpoint(equipo_id: int, session=Depends(get_db)):
    equipo = get_equipo_doble(session, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo Doble not found")
    return {"id": equipo.id, "jugador1_id": equipo.jugador1_id, "jugador2_id": equipo.jugador2_id}

@router.post("/")
def create_equipo_doble_endpoint(
    jugador1_id: int,
    jugador2_id: int,
    torneo_id: int,
    categoria_id: int,
    session=Depends(get_db),
):
    equipo = create_equipo_doble(session, jugador1_id, jugador2_id, torneo_id, categoria_id)
    return {"id": equipo.id, "jugador1_id": equipo.jugador1_id}

@router.put("/{equipo_id}")
def update_equipo_doble_endpoint(
    equipo_id: int,
    jugador1_id: int = None,
    jugador2_id: int = None,
    torneo_id: int = None,
    categoria_id: int = None,
    session=Depends(get_db),
):
    equipo = update_equipo_doble(session, equipo_id, jugador1_id, jugador2_id, torneo_id, categoria_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo Doble not found")
    return {"id": equipo.id, "jugador1_id": equipo.jugador1_id}

@router.delete("/{equipo_id}")
def delete_equipo_doble_endpoint(equipo_id: int, session=Depends(get_db)):
    equipo = delete_equipo_doble(session, equipo_id)
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo Doble not found")
    return {"detail": "Equipo Doble deleted successfully"}