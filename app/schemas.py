from marshmallow import fields, validates_schema, EXCLUDE
from marshmallow.decorators import post_dump
from marshmallow.exceptions import ValidationError
from marshmallow_sqlalchemy import auto_field
from marshmallow_sqlalchemy.fields import Nested


from utils_flask_sqla.schema import SmartRelationshipsMixin


from app.env import ma
from app.models import Demarche, Dossier


class DemarcheSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Demarche
        include_fk = True


class DossierSchema(SmartRelationshipsMixin, ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dossier
        include_fk = True

    demarche = Nested(DemarcheSchema)


DemarcheSchema.dossier = Nested(DossierSchema)
