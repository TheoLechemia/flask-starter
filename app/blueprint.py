from flask import Blueprint


routes = Blueprint("main", __name__)

from app.env import db
from app.models import Demarche, Dossier, Champs, GeoArea, File
from app.schemas import DemarcheSchema, DossierSchema


@routes.route("/demarches", methods=["GET"])
def get_all_demarches():
    query = db.session.select(Demarche)
    data = db.session.execute(query).scalars()
    return DemarcheSchema().dump(data, many=True)


@routes.route("/dossiers", methods=["GET"])
def get_all_dossiers():
    query = db.session.select(Dossier)
    data = db.session.execute(query).scalars()
    return DossierSchema().dump(data, many=True)
