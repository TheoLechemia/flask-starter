from flask import Blueprint


routes = Blueprint("main", __name__)

from app.env import db


@routes.route("/demarches", methods=["GET"])
def get_all_demarches():
    return "GET all dossiers"


@routes.route("/dossiers", methods=["GET"])
def get_all_dossiers():
    return "GET all dossiers"
