from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional



class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    year_length: Mapped[str]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planets")
   

    def to_dict(self):
        return dict(
            id=self.id, 
            name=self.name, 
            description=self.description,
            year_length=self.year_length,
            moon=self.moon.name if self.moon_id else None

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
