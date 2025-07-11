from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
from app.db import get_db
from app.cruds.llaves import (
    create_llave,
    get_llave,
    get_llaves,
    update_llave,
    delete_llave,
)

router = APIRouter(prefix="/llaves", tags=["Llaves"])

@router.get("/")
def get_llaves_endpoint(session=Depends(get_db)):
    llaves = get_llaves(session)
    return [{"id": l.id, "ronda_id": l.ronda_id, "posicion": l.posicion, "es_bye": l.es_bye} for l in llaves]

@router.get("/{llave_id}")
def get_llave_endpoint(llave_id: int, session=Depends(get_db)):
    llave = get_llave(session, llave_id)
    if not llave:
        raise HTTPException(status_code=404, detail="Llave not found")
    return {
        "id": llave.id,
        "ronda_id": llave.ronda_id,
        "posicion": llave.posicion,
        "participante_id": llave.participante_id,
        "equipo_id": llave.equipo_id,
        "es_bye": llave.es_bye,
    }

@router.post("/")
def create_llave_endpoint(
    ronda_id: int,
    posicion: int,
    participante_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
    es_bye: bool = False,
    session=Depends(get_db),
):
    llave = create_llave(session, ronda_id, posicion, participante_id, equipo_id, es_bye)
    return {"id": llave.id, "ronda_id": llave.ronda_id, "posicion": llave.posicion}

@router.put("/{llave_id}")
def update_llave_endpoint(
    llave_id: int,
    ronda_id: Optional[int] = None,
    posicion: Optional[int] = None,
    participante_id: Optional[int] = None,
    equipo_id: Optional[int] = None,
    es_bye: Optional[bool] = None,
    session=Depends(get_db),
):
    llave = update_llave(session, llave_id, ronda_id, posicion, participante_id, equipo_id, es_bye)
    if not llave:
        raise HTTPException(status_code=404, detail="Llave not found")
    return {"id": llave.id, "ronda_id": llave.ronda_id, "posicion": llave.posicion}

@router.delete("/{llave_id}")
def delete_llave_endpoint(llave_id: int, session=Depends(get_db)):
    llave = delete_llave(session, llave_id)
    if not llave:
        raise HTTPException(status_code=404, detail="Llave not found")
    return {"detail": "Llave deleted successfully"}