import requests
import json
import os

CACHE_FILE = "poke_cache.json"

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def get_pokemon_data(name):
    cache = load_cache()
    name_lower = name.lower()
    if name_lower in cache:
        return cache[name_lower]
    url_dados = f"https://pokeapi.co/api/v2/pokemon/{name_lower}"
    try:
        response = requests.get(url_dados, timeout=5)
        if response.status_code == 200:
            data = response.json()
            poke_id = data["id"]
            image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
            result = {
                "id": poke_id,
                "name": data["name"].capitalize(),
                "height": data["height"],
                "weight": data["weight"],
                "types": data["types"],
                "abilities": data["abilities"],
                "image_url": image_url 
            }
            cache[name_lower] = result
            save_cache(cache)
            return result
        else:
            print(f"[ERRO] Pokémon '{name}' não encontrado.")
    except requests.RequestException as e:
        print(f"[ERRO DE CONEXÃO] {e}")
    return None