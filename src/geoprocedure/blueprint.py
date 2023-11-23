from flask import Blueprint, request
from werkzeug.datastructures import MultiDict


routes = Blueprint("main", __name__)
routes = Blueprint("main", __name__)

from geoprocedure.env import db
from geoprocedure.models import Demarche, Dossier
from geoprocedure.schemas import DemarcheSchema, DossierSchema


@routes.route("/demarches", methods=["GET"])
def get_all_demarches():
    params = MultiDict(request.args)
    fields = params.pop("fields", default="").split(",")
    query = db.session.select(Demarche)
    data = db.session.execute(query).scalars()
    return DemarcheSchema(only=fields).dump(data, many=True)


@routes.route("/dossiers", methods=["GET"])
def get_all_dossiers():
    params = MultiDict(request.args)
    fields = params.pop("fields", default="").split(",")
    query = db.session.select(Dossier)
    data = db.session.execute(query).scalars()
    return DossierSchema(only=fields).dump(data, many=True)
