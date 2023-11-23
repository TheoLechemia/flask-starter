from datetime import datetime

from geoprocedure.env import db

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, raiseload, joinedload, relationship


from sqlalchemy.sql.expression import Select


class Demarche(db.Model):
    __tablename__ = "demarche"
    __table_args__ = {"schema": "ds"}

    id_demarche: Mapped[int] = mapped_column(Integer, primary_key=True)


class Dossier(db.Model):
    __tablename__ = "dossier"
    __table_args__ = {"schema": "ds"}

    id_dossier: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_demarche: Mapped[int] = mapped_column(
        Integer, ForeignKey("ds.demarche.id_demarche")
    )
    demarche: Mapped[Demarche] = relationship()
    statut: Mapped[str] = mapped_column()


class Champs(db.Model):
    __tablename__ = "champs"
    __table_args__ = {"schema": "ds"}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_dossier: Mapped[int] = mapped_column()
    label: Mapped[str] = mapped_column()
    string_value: Mapped[str] = mapped_column()
    string_value: Mapped[str] = mapped_column()
    updated_at: Mapped[datetime] = mapped_column()


class GeoArea(db.Model):
    __tablename__ = "geo_area"
    __table_args__ = {"schema": "ds"}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_champ: Mapped[int] = mapped_column(ForeignKey("ds.champs.id"))
    geojson: Mapped[str] = mapped_column()


class File(db.Model):
    __tablename__ = "file"
    __table_args__ = {"schema": "ds"}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_champ: Mapped[int] = mapped_column(ForeignKey("ds.champs.id"))
    url: Mapped[str] = mapped_column()
