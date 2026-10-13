from flask import Blueprint,abort,make_response, request
from ..models.planet import Planet,planets
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")
@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    year_length = request_body["year_length"]

    new_planet = Planet(name=name, description=description, year_length=year_length)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "year_length": new_planet.year_length,
    }
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "year_length": planet.year_length
            }
        )
    return planets_response
# @planets_bp.get("")
# def get_all_planets():
#     results = []

#     for planet in planets:
#         results.append(dict(
#         id=planet.id,
#         name=planet.name,
#         description=planet.description,
#         year_length=planet.year_length    
#         ))

#     return results

# @planets_bp.get("/<id>")
# def handle_planet(id):
#     planet = validate_planet(id)
#     return dict(
#         id=planet.id,
#         name=planet.name,
#         description=planet.description,
#         year_length=planet.year_length     

#     )
# def validate_planet(id):
#     try:
#         id = int(id)
#     except:
#         abort(make_response({"message": f"planet {id} invalid"}, 400))
#     for planet in planets:
#         if planet.id == id:
#             return planet
#     abort(make_response({"message": f"planet {id} not found"}, 404))




