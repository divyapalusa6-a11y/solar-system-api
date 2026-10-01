from flask import Blueprint,abort,make_response
from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    results = []

    for planet in planets:
        results.append(dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        year_length=planet.year_length    
        ))

    return results

@planets_bp.get("/<id>")
def handle_planet(id):
    planet = validate_planet(id)
    return dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        year_length=planet.year_length     

    )
def validate_planet(id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"planet {id} invalid"}, 400))
    for planet in planets:
        if planet.id == id:
            return planet
    abort(make_response({"message": f"planet {id} not found"}, 404))




