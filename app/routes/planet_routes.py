from flask import Blueprint
from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    results = []

    for planet in planets:
        results.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "year_length": planet.year_length,
        })

    return results




