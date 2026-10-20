from flask import Blueprint,abort,make_response, request
from .route_utilities import validate_model
from ..models.planet import Planet
from ..db import db

bp = Blueprint("planets_bp", __name__, url_prefix="/planets")
@bp.post("")
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()
    return new_planet.to_dict(), 201

@bp.get("")
def get_all_planets():
    query = db.select(Planet)
    description_param = request.args.get("description")

    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    year_length_param = request.args.get("year_length")
    if year_length_param:
        query = query.where(Planet.year_length.ilike(f"%{year_length_param}"))

    query = query.order_by(Planet.id)
    planets = db.session.scalars(query)
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict()) 
    return planets_response

@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    
    planet = validate_model(Planet, id)
    return planet.to_dict()
  
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         response = {"message": f"planet {planet_id} invalid"}
#         abort(make_response(response , 400))

#     query = db.select(Planet).where(Planet.id == planet_id)
#     planet = db.session.scalar(query)

#     if not planet:
#         response = {"message": f"planet {planet_id} not found"}
#         abort(make_response(response, 404))

#     return planet

@bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.year_length = request_body["year_length"]
    db.session.commit()

    return make_response("", 204)

@bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_model(Planet, planet_id)
    db.session.delete(planet)
    db.session.commit()

    return make_response("", 204)
    
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




