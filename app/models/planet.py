class Planet:
    def __init__(self, id, name, description, year_length):
        self.id = id
        self.name = name
        self.description = description
        self.year_length = year_length


planets = [
    Planet(1, "Earth", "Our home", "365"),
    Planet(2, "Venus", "Hottest planet", "225"),
    Planet(3, "Mars", "The red planet", "687"),
    Planet(4, "Mercury", "Smallest planet", "88"),
]
