from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from app.db import get_db
from app.cruds.categorias import (
    create_categoria,
    get_categoria,
    get_categorias,
    update_categoria,
    delete_categoria,
)

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/")
def get_categorias_endpoint(session=Depends(get_db)):
    categorias = get_categorias(session)
    return [{"id": c.id, "nombre": c.nombre} for c in categorias]

@router.get("/{categoria_id}")
def get_categoria_endpoint(categoria_id: int, session=Depends(get_db)):
    categoria = get_categoria(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return {"id": categoria.id, "nombre": categoria.nombre}

@router.post("/")
def create_categoria_endpoint(
    nombre: str,
    edad_minima: int,
    edad_maxima: int,
    genero: str,
    sets_por_partido: int,
    puntos_por_set: int,
    session=Depends(get_db),
):
    categoria = create_categoria(session, nombre, edad_minima, edad_maxima, genero, sets_por_partido, puntos_por_set)
    return {"id": categoria.id, "nombre": categoria.nombre}

@router.put("/{categoria_id}")
def update_categoria_endpoint(
    categoria_id: int,
    nombre: Optional[str] = None,
    edad_minima: Optional[int] = None,
    edad_maxima: Optional[int] = None,
    genero: Optional[str] = None,
    sets_por_partido: Optional[int] = None,
    puntos_por_set: Optional[int] = None,
    session=Depends(get_db),
):
    categoria = update_categoria(session, categoria_id, nombre, edad_minima, edad_maxima, genero, sets_por_partido, puntos_por_set)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return {"id": categoria.id, "nombre": categoria.nombre}

@router.delete("/{categoria_id}")
def delete_categoria_endpoint(categoria_id: int, session=Depends(get_db)):
    categoria = delete_categoria(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return {"detail": "Categoria deleted successfully"}