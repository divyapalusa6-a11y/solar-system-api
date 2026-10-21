from flask import Blueprint,abort,make_response, request
from .route_utilities import validate_model
from ..models.planet import Planet
from ..models.moon import Moon
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
    
    planet = validate_model(Planet, planet_id)
    return planet.to_dict()



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


# Create a moon for a specific planet.
@bp.post("/<planet_id>/moons")
def create_moon(planet_id):
    # Check that the planet exists.
    planet = validate_model(Planet, planet_id)

    # Read the moon's information from the JSON request body.
    request_body = request.get_json()

    # Create a Moon object from the request data.
    new_moon = Moon.from_dict(request_body)

    # Associate the moon with the selected planet.
    new_moon.planet = planet

    # Save the new moon to the database.
    db.session.add(new_moon)
    db.session.commit()

    # Return the new moon's data and status code 201 (Created).
    return new_moon.to_dict(), 201

    




