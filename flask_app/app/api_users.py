from flask_restx import Namespace, Resource, fields
from flask import request
from .models import User
from .db import db

ns = Namespace("users", description="User operations")

user_model = ns.model(
    "User",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(required=True),
        "email": fields.String(required=True),
    },
)

@ns.route("/")
class UserList(Resource):
    @ns.marshal_list_with(user_model)
    def get(self):
        return User.query.all()   # Uses default Postgres DB

    @ns.expect(user_model, validate=True)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        data = request.json

        user = User(name=data["name"], email=data["email"])
        db.session.add(user)
        db.session.commit()

        return user, 201


@ns.route("/<int:id>")
class UserItem(Resource):
    @ns.marshal_with(user_model)
    def get(self, id):
        return User.query.get_or_404(id)

    @ns.expect(user_model, validate=True)
    @ns.marshal_with(user_model)
    def put(self, id):
        data = request.json

        user = User.query.get_or_404(id)
        user.name = data["name"]
        user.email = data["email"]

        db.session.commit()
        return user

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"deleted": id}
