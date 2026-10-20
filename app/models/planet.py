from sqlalchemy.orm import Mapped, mapped_column
from ..db import db


class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    year_length: Mapped[str]
        

    def to_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            description=self.description,
            year_length=self.year_length
        )


    @classmethod
    def from_dict(cls, planet_data):
        name = planet_data["name"]
        description = planet_data["description"]
        year_length = planet_data["year_length"]

        new_planet = cls(
            name=name, 
            description=description, 
            year_length=year_length
        )

        return new_planet

# planets = [
#     Planet(1, "Earth", "Our home", "365"),
#     Planet(2, "Venus", "Hottest planet", "225"),
#     Planet(3, "Mars", "The red planet", "687"),
#     Planet(4, "Mercury", "Smallest planet", "88"),
# ]
