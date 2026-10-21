
# Mapped and mapped_column define the database columns.
# relationship connects two SQLAlchemy models.
from sqlalchemy.orm import Mapped, mapped_column, relationship

# ForeignKey connects a column to a primary key in another table.
from sqlalchemy import ForeignKey

from ..db import db


class Moon(db.Model):
    # Unique ID for each moon. The database generates it automatically.
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    # The moon's name, size, and description are stored in the database.
    name: Mapped[str]
    size: Mapped[int]
    description: Mapped[str]

    # This foreign key identifies which planet this moon belongs to.
    # It references the id column in the planet table.
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))

    # This relationship lets us access the Planet object for this moon.
    # "moons" must match the relationship name in the Planet model.
    planet: Mapped["Planet"] = relationship(back_populates="moons")

    def to_dict(self):
        # Convert the Moon object into a dictionary for a JSON response.
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description,
            "planet_id": self.planet_id
        }

    @classmethod
    def from_dict(cls, moon_data):
        # Create a Moon object using the data received in the request.
        # The route will associate it with a planet.
        return cls(
            name=moon_data["name"],
            size=moon_data["size"],
            description=moon_data["description"]
        )
