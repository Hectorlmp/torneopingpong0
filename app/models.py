from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    ForeignKey,
    Boolean,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.db import Base


class Asociacion(Base):
    __tablename__ = "asociaciones"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    pais = Column(String, nullable=False)

    jugadores = relationship("Jugador", back_populates="asociacion")


class Jugador(Base):
    __tablename__ = "jugadores"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    genero = Column(String, nullable=False)
    ciudad = Column(String, nullable=True)
    pais = Column(String, nullable=True)
    asociacion_id = Column(Integer, ForeignKey("asociaciones.id"), nullable=True)

    asociacion = relationship("Asociacion", back_populates="jugadores")


class Torneo(Base):
    __tablename__ = "torneos"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    fecha_inicio_inscripcion = Column(DateTime, nullable=False)
    fecha_fin_inscripcion = Column(DateTime, nullable=False)
    fecha_inicio_competencia = Column(DateTime, nullable=False)
    mesas_disponibles = Column(Integer, nullable=False)

    categorias = relationship("Categoria", secondary="torneos_categorias", back_populates="torneos")
    grupos = relationship("Grupo", back_populates="torneo")
    rondas = relationship("Ronda", back_populates="torneo")


class Categoria(Base):
    __tablename__ = "categorias"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    edad_minima = Column(Integer, nullable=False)
    edad_maxima = Column(Integer, nullable=False)
    genero = Column(String, nullable=False)
    sets_por_partido = Column(Integer, nullable=False)
    puntos_por_set = Column(Integer, nullable=False)

    torneos = relationship("Torneo", secondary="torneos_categorias", back_populates="categorias")


class TorneoCategoria(Base):
    __tablename__ = "torneos_categorias"
    __table_args__ = {"schema": "public"}
    torneo_id = Column(Integer, ForeignKey("torneos.id"), primary_key=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), primary_key=True)


class Participante(Base):
    __tablename__ = "participantes"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    jugador_id = Column(Integer, ForeignKey("jugadores.id"), nullable=True)
    torneo_id = Column(Integer, ForeignKey("torneos.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    jugador = relationship("Jugador")
    torneo = relationship("Torneo")
    categoria = relationship("Categoria")


class EquipoDoble(Base):
    __tablename__ = "equipos_dobles"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    jugador1_id = Column(Integer, ForeignKey("jugadores.id"), nullable=False)
    jugador2_id = Column(Integer, ForeignKey("jugadores.id"), nullable=False)
    torneo_id = Column(Integer, ForeignKey("torneos.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    jugador1 = relationship("Jugador", foreign_keys=[jugador1_id])
    jugador2 = relationship("Jugador", foreign_keys=[jugador2_id])
    torneo = relationship("Torneo")
    categoria = relationship("Categoria")


class Partido(Base):
    __tablename__ = "partidos"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    torneo_id = Column(Integer, ForeignKey("torneos.id"), nullable=False)
    tipo = Column(String, nullable=False)  # 'individual' o 'dobles'
    horario = Column(DateTime, nullable=False)
    mesa = Column(Integer, nullable=False)

    jugador1_id = Column(Integer, ForeignKey("jugadores.id"), nullable=True)
    jugador2_id = Column(Integer, ForeignKey("jugadores.id"), nullable=True)
    equipo1_id = Column(Integer, ForeignKey("equipos_dobles.id"), nullable=True)
    equipo2_id = Column(Integer, ForeignKey("equipos_dobles.id"), nullable=True)

    jugador1 = relationship("Jugador", foreign_keys=[jugador1_id])
    jugador2 = relationship("Jugador", foreign_keys=[jugador2_id])
    equipo1 = relationship("EquipoDoble", foreign_keys=[equipo1_id])
    equipo2 = relationship("EquipoDoble", foreign_keys=[equipo2_id])
    torneo = relationship("Torneo")


class Set(Base):
    __tablename__ = "sets"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    partido_id = Column(Integer, ForeignKey("partidos.id"), nullable=False)
    numero_set = Column(Integer, nullable=False)
    puntos_jugador1 = Column(Integer, nullable=False)
    puntos_jugador2 = Column(Integer, nullable=False)

    partido = relationship("Partido")


class Grupo(Base):
    __tablename__ = "grupos"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    torneo_id = Column(Integer, ForeignKey("torneos.id"), nullable=False)
    nombre = Column(String, nullable=False)

    torneo = relationship("Torneo", back_populates="grupos")


class ParticipanteGrupo(Base):
    __tablename__ = "participantes_grupos"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    participante_id = Column(Integer, ForeignKey("participantes.id"), nullable=False)
    grupo_id = Column(Integer, ForeignKey("grupos.id"), nullable=False)


class Ronda(Base):
    __tablename__ = "rondas"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    torneo_id = Column(Integer, ForeignKey("torneos.id"), nullable=False)
    numero = Column(Integer, nullable=False)
    nombre = Column(String, nullable=False)

    torneo = relationship("Torneo", back_populates="rondas")


class Llave(Base):
    __tablename__ = "llaves"
    __table_args__ = {"schema": "public"}
    id = Column(Integer, primary_key=True, index=True)
    ronda_id = Column(Integer, ForeignKey("rondas.id"), nullable=False)
    posicion = Column(Integer, nullable=False)
    participante_id = Column(Integer, ForeignKey("participantes.id"), nullable=True)
    equipo_id = Column(Integer, ForeignKey("equipos_dobles.id"), nullable=True)
    es_bye = Column(Boolean, default=False)

    ronda = relationship("Ronda")
