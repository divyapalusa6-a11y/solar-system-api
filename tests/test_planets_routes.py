def test_get_all_planets_returns_empty_list_when_db_is_empty(client):
    # act
    response = client.get("/planets")

    # assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_all_planets_returns_one_planet_when_present(client, one_planet):
    # act
    response = client.get("/planets")
    planets = response.get_json()

    # assert
    assert response.status_code == 200
    assert len(planets) == 1

    planet = planets[0]
    assert planet["id"] == one_planet.id
    assert planet["name"] == one_planet.name
    assert planet["description"] == one_planet.description
    assert planet["year_length"] == one_planet.year_length

def test_get_one_planet_returns_one_planet_when_present(client, one_planet):
    # act
    response = client.get(f"/planets/{one_planet.id}")
    planet = response.get_json()

    # assert
    assert response.status_code == 200
    assert planet["id"] == one_planet.id
    assert planet["name"] == one_planet.name
    assert planet["description"] == one_planet.description
    assert planet["year_length"] == one_planet.year_length


def test_create_planet_successfully(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "Proxima Centauri b",
        "description": "A potentially habitable exoplanet",
        "year_length": "1.2"
    }

    # act
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_json()

    # assert
    assert response.status_code == 201
    assert response_body["id"] == 1
    assert response_body["name"] == EXPECTED_PLANET["name"]
    assert response_body["description"] == EXPECTED_PLANET["description"]
    assert response_body["year_length"] == EXPECTED_PLANET["year_length"]
