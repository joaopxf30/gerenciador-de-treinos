import uuid

from typing import List

from sqlalchemy import (
    Date,
    Time,
    ForeignKey,
    Integer,
    Float,
    String,
    UUID,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date

from model.base import GerenciadorTreinosBase


class Esportista(GerenciadorTreinosBase):
    __tablename__ = "esportista"

    nome_completo: Mapped[str] = mapped_column(String(50), primary_key=True)
    idade: Mapped[int] = mapped_column(Integer)
    altura: Mapped[float] = mapped_column(Float, nullable=True)
    peso: Mapped[float] = mapped_column(Float, nullable=True)
    treinos: Mapped[List["Treino"]] = relationship(
        back_populates="esportista",
        cascade="all, delete",
    )


class Treino(GerenciadorTreinosBase):
    __tablename__ = "treino"

    nome_esportista: Mapped[str] = mapped_column(
        String(50), ForeignKey("esportista.nome_completo", ondelete="CASCADE",),
        primary_key=True
    )
    data_treino: Mapped[date] = mapped_column(Date, primary_key=True)
    esporte: Mapped[str] = mapped_column(String(50), primary_key=True)
    duracao: Mapped[time] = mapped_column(Time, nullable=True)
    calorias: Mapped[int] = mapped_column(Integer, nullable=True)
    bpm: Mapped[int] = mapped_column(Integer, nullable=True)
    esportista: Mapped["Esportista"] = relationship(back_populates="treinos")