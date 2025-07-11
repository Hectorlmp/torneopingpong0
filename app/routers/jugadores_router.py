from typing import Optional
from datetime import date
from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.jugadores import (
    create_jugador,
    get_jugador,
    get_jugadores,
    update_jugador,
    delete_jugador,
)

router = APIRouter(prefix="/jugadores", tags=["Jugadores"])

@router.get("/")
def get_jugadores_endpoint(session=Depends(get_db)):
    jugadores = get_jugadores(session)
    return [{"id": j.id, "nombre": j.nombre} for j in jugadores]

@router.get("/{jugador_id}")
def get_jugador_endpoint(jugador_id: int, session=Depends(get_db)):
    jugador = get_jugador(session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return {"id": jugador.id, "nombre": jugador.nombre}

@router.post("/")
def create_jugador_endpoint(
    nombre: str,
    fecha_nacimiento: date,
    genero: str,
    ciudad: Optional[str] = None,
    pais: Optional[str] = None,
    asociacion_id: Optional[int] = None,
    session=Depends(get_db),
):
    jugador = create_jugador(session, nombre, fecha_nacimiento, genero,
                              ciudad=ciudad, pais=pais, asociacion_id=asociacion_id)
    return {"id": jugador.id, "nombre": jugador.nombre}

@router.put("/{jugador_id}")
def update_jugador_endpoint(
    jugador_id: int,
    nombre: Optional[str] = None,
    fecha_nacimiento: Optional[date] = None,
    genero: Optional[str] = None,
    ciudad: Optional[str] = None,
    pais: Optional[str] = None,
    asociacion_id: Optional[int] = None,
    session=Depends(get_db),
):
    jugador = update_jugador(session, jugador_id, nombre, fecha_nacimiento, genero,
                              ciudad, pais, asociacion_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return {"id": jugador.id, "nombre": jugador.nombre}

@router.delete("/{jugador_id}")
def delete_jugador_endpoint(jugador_id: int, session=Depends(get_db)):
    jugador = delete_jugador(session, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador not found")
    return {"detail": "Jugador deleted successfully"}