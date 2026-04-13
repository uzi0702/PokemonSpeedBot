import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def get_speed(name):
    res = requests.get(f"{BASE_URL}pokemon/{name}", timeout=10)

    if not res.ok:
        return None

    data = res.json()

    for stat in data["stats"]:
        if stat["stat"]["name"] == "speed":
            return stat["base_stat"]

    return None