from app import create_app
from app.db import db
from app.models.planet import Planet

app = create_app()

planets = [
    {
        "name": "Mercury",
        "description": "The smallest planet",
        "year_length": "0.330"
    },
    {
        "name": "Venus",
        "description": "The hottest planet",
        "year_length": "4.87"
    },
    {
        "name": "Earth",
        "description": "Our home planet",
        "year_length": "5.972"
    },
    {
        "name": "Mars",
        "description": "The red planet",
        "year_length": "0.642"
    },
    {
        "name": "Jupiter",
        "description": "The largest planet",
        "year_length": "1898"
    },
    {
        "name": "Saturn",
        "description": "The planet famous for its rings",
        "year_length": "568"
    },
    {
        "name": "Uranus",
        "description": "An ice giant",
        "year_length": "86.8"
    },
    {
        "name": "Neptune",
        "description": "The farthest planet from the Sun",
        "year_length": "102"
    }
]

with app.app_context():
    existing_planets = db.session.scalars(
        db.select(Planet)
    ).all()

    existing_names = {
        planet.name for planet in existing_planets
    }

    for planet_data in planets:
        if planet_data["name"] not in existing_names:
            new_planet = Planet(**planet_data)
            db.session.add(new_planet)

    db.session.commit()

    print("Planet seed data added successfully!")