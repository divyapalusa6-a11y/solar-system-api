from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[int]
    description: Mapped[str]
    name: Mapped[str]
    planets: Mapped[list["Planet"]] = relationship(back_populates="moon")

    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name,
            "size": self.size,
            "description": self.description
        }
        
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(name=moon_data["name"], size=moon_data["size"], description=moon_data["description"])
        return new_moon