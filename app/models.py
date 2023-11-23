from datetime import datetime

from app.env import db

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, raiseload, joinedload, relationship


from sqlalchemy.sql.expression import Select


class UserSelect(Select):
    inherit_cache = True

    def auto_joinload(self, model, fields=[]):
        query_option = [raiseload("*")]
        for f in fields:
            if f in model.__mapper__.relationships:
                query_option.append(joinedload(getattr(model, f)))
        self = self.options(*tuple(query_option))
        return self

    def where_identifant(self, value):
        return self.filter_by(identifiant=value)


class Organism(db.Model):
    __tablename__ = "bib_organismes"
    __table_args__ = {"schema": "utilisateurs"}
    id_organisme: Mapped[int] = mapped_column(Integer, primary_key=True)
    nom_organisme: Mapped[str] = mapped_column(String, unique=True, nullable=False)


class User(db.Model):
    __tablename__ = "t_roles"
    __table_args__ = {"schema": "utilisateurs"}
    __select_class__ = UserSelect

    id_role: Mapped[int] = mapped_column(Integer, primary_key=True)
    identifiant: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    id_organisme: Mapped[int] = mapped_column(
        String, ForeignKey("utilisateurs.bib_organismes.id_organisme")
    )
    active = db.Column(db.Boolean)
    organism: Mapped["Organism"] = relationship()


class Champs(db.Model):
    __tablename__ = "champs"
    __table_args__ = {"schema": "ds"}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_dossier: Mapped[int] = mapped_column()
    label: Mapped[str] = mapped_column()
    string_value: Mapped[str] = mapped_column()
    string_value: Mapped[str] = mapped_column()
    updated_at: Mapped[datetime] = mapped_column()


class GeoArea(Champs, db.Model):
    __tablename__ = "geo_area"
    __table_args__ = {"schema": "ds"}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_champ: Mapped[int] = mapped_column(ForeignKey("ds.champs.id"))
    geojson: Mapped[str] = mapped_column()


class GeoArea(Champs, db.Model):
    __tablename__ = "file"
    __table_args__ = {"schema": "ds"}
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_champ: Mapped[int] = mapped_column(ForeignKey("ds.champs.id"))
    url: Mapped[str] = mapped_column()
