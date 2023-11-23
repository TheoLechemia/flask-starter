from flask import Blueprint


routes = Blueprint("main", __name__)

from geoprocedure.env import db
from geoprocedure.models import Demarche, Dossier, Champs, GeoArea, File


@routes.route("/demarches", methods=["GET"])
def get_all_demarches():
    return "GET all dossiers"


@routes.route("/dossiers", methods=["GET"])
def get_all_dossiers():
    return "GET all dossiers"
