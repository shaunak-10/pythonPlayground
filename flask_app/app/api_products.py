from flask_restx import Namespace, Resource, fields
from flask import request
from .models import Product
from .db import db

ns = Namespace("products", description="Product operations")

product_model = ns.model(
    "Product",
    {
        "id": fields.Integer(readonly=True),
        "name": fields.String(required=True),
        "price": fields.Float(required=True),
    },
)

@ns.route("/")
class ProductList(Resource):
    @ns.marshal_list_with(product_model)
    def get(self):
        # READ from MySQL bind
        return Product.query.using_bind("mysql_db").all()

    @ns.expect(product_model, validate=True)
    @ns.marshal_with(product_model, code=201)
    def post(self):
        data = request.json

        # INSERT into MySQL
        engine = db.engines["mysql_db"]
        with db.engine.connect() as _:
            db.session.bind = engine

        p = Product(name=data["name"], price=data["price"])
        db.session.add(p)
        db.session.commit()

        return p, 201


@ns.route("/<int:id>")
class ProductItem(Resource):
    @ns.marshal_with(product_model)
    def get(self, id):
        return Product.query.using_bind("mysql_db").get_or_404(id)

    @ns.expect(product_model, validate=True)
    @ns.marshal_with(product_model)
    def put(self, id):
        data = request.json

        engine = db.engines["mysql_db"]
        db.session.bind = engine

        product = Product.query.using_bind("mysql_db").get_or_404(id)
        product.name = data["name"]
        product.price = data["price"]

        db.session.commit()
        return product

    def delete(self, id):
        engine = db.engines["mysql_db"]
        db.session.bind = engine

        product = Product.query.using_bind("mysql_db").get_or_404(id)
        db.session.delete(product)
        db.session.commit()

        return {"deleted": id}
