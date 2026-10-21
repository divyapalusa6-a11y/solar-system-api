
# Mapped and mapped_column define database columns.
# relationship connects Planet to the Moon model.
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class Planet(db.Model):
    # Unique ID for each planet, generated automatically by the database.
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # These attributes become columns in the planet table.
    name: Mapped[str]
    description: Mapped[str]
    year_length: Mapped[str]

    # One planet can have many moons.
    # "planet" must match the relationship name in Moon.
    # SQLAlchemy uses this relationship to access a planet's moons.
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    def to_dict(self):
        # Convert the Planet object into a dictionary for a JSON response.
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            year_length=self.year_length,
            moons=[moon.to_dict() for moon in self.moons]
        )

    @classmethod
    def from_dict(cls, planet_data):
        # Read the planet's information from the incoming dictionary.
        name = planet_data["name"]
        description = planet_data["description"]
        year_length = planet_data["year_length"]

        # Create a new Planet object using the provided information.
        new_planet = cls(
            name=name,
            description=description,
            year_length=year_length
        )

        return new_planet


# Previously used sample data:
# planets = [
#     Planet(1, "Earth", "Our home", "365"),
#     Planet(2, "Venus", "Hottest planet", "225"),
#     Planet(3, "Mars", "The red planet", "687"),
#     Planet(4, "Mercury", "Smallest planet", "88"),
# ]
