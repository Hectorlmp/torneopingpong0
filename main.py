import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import (
    asociaciones_router,
    jugadores_router,
    torneos_router,
    categorias_router,
    participantes_router,
    equipos_dobles_router,
    partidos_router,
    sets_router,
    grupos_router,
    participantes_grupos_router,
    rondas_router,
    llaves_router,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(level=logging.INFO)
    logging.info("Aplicación iniciada")
    yield
    logging.info("Aplicación cerrada")


FASTAPI_CONFIG = {
    "title": "API Torneos Tenis de Mesa",
    "description": "API para gestión de torneos de tenis de mesa",
    "openapi_url": "/openapi.json",
    "version": "0.1.0",
    "swagger_ui_parameters": {"defaultModelsExpandDepth": -1},
}

MIDDLEWARE_CONFIG = {
    "allow_origins": ["*"],  # Puedes cambiar por dominios específicos
    "allow_credentials": True,
    "allow_methods": ["*"],
    "allow_headers": ["*"],
}

app = FastAPI(**FASTAPI_CONFIG, lifespan=lifespan)
app.add_middleware(CORSMiddleware, **MIDDLEWARE_CONFIG)

# Registrando routers
app.include_router(asociaciones_router.router, prefix="/asociaciones", tags=["Asociaciones"])
app.include_router(jugadores_router.router, prefix="/jugadores", tags=["Jugadores"])
app.include_router(torneos_router.router, prefix="/torneo", tags=["Torneo"])
app.include_router(categorias_router.router, prefix="/categorias", tags=["Categorías"])
app.include_router(participantes_router.router, prefix="/participantes", tags=["Participantes"])
app.include_router(equipos_dobles_router.router, prefix="/equipos-dobles", tags=["Equipos Dobles"])
app.include_router(partidos_router.router, prefix="/partidos", tags=["Partidos"])
app.include_router(sets_router.router, prefix="/sets", tags=["Sets"])
app.include_router(grupos_router.router, prefix="/grupos", tags=["Grupos"])
app.include_router(participantes_grupos_router.router, prefix="/participantes-grupos", tags=["Participantes Grupos"])
app.include_router(rondas_router.router, prefix="/rondas", tags=["Rondas"])
app.include_router(llaves_router.router, prefix="/llaves", tags=["Llaves"])


@app.get("/")
def root():
    return {"message": "API Torneos Tenis de Mesa - OK"}
