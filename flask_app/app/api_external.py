from flask_restx import Namespace, Resource
import requests

ns = Namespace("external", description="External APIs")

@ns.route("/jsonplaceholder")
class JsonPlaceholder(Resource):
    def get(self):
        r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
        r.raise_for_status()
        return r.json()
