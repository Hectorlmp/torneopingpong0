from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.asociaciones import (
    create_asociacion,
    get_asociacion,
    get_asociaciones,
    update_asociacion,
    delete_asociacion,
)

router = APIRouter(prefix="/asociaciones", tags=["Asociaciones"])

@router.get("/")
def get_asociaciones_endpoint(session=Depends(get_db)):
    asociaciones = get_asociaciones(session)
    return [{"id": a.id, "nombre": a.nombre} for a in asociaciones]

@router.get("/{asociacion_id}")
def get_asociacion_endpoint(asociacion_id: int, session=Depends(get_db)):
    asociacion = get_asociacion(session, asociacion_id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociacion not found")
    return {"id": asociacion.id, "nombre": asociacion.nombre}

@router.post("/")
def create_asociacion_endpoint(
    nombre: str,
    ciudad: Optional[str] = None,
    pais: Optional[str] = None,
    session=Depends(get_db),
):
    asociacion = create_asociacion(session, nombre, ciudad, pais)
    return {"id": asociacion.id, "nombre": asociacion.nombre}

@router.put("/{asociacion_id}")
def update_asociacion_endpoint(
    asociacion_id: int,
    nombre: Optional[str] = None,
    ciudad: Optional[str] = None,
    pais: Optional[str] = None,
    session=Depends(get_db),
):
    asociacion = update_asociacion(session, asociacion_id, nombre, ciudad, pais)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociacion not found")
    return {"id": asociacion.id, "nombre": asociacion.nombre}

@router.delete("/{asociacion_id}")
def delete_asociacion_endpoint(asociacion_id: int, session=Depends(get_db)):
    asociacion = delete_asociacion(session, asociacion_id)
    if not asociacion:
        raise HTTPException(status_code=404, detail="Asociacion not found")
    return {"detail": "Asociacion deleted successfully"}