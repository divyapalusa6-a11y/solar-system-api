from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    year_length: Mapped[str]
        


# planets = [
#     Planet(1, "Earth", "Our home", "365"),
#     Planet(2, "Venus", "Hottest planet", "225"),
#     Planet(3, "Mars", "The red planet", "687"),
#     Planet(4, "Mercury", "Smallest planet", "88"),
# ]
