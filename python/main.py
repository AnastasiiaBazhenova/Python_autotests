import requests
URL = 'https://api.pokemonbattle.ru/v2'
Token = 'a11a6dee93c9793c186159cd7a3ef392'
Header = {'Content-Type' : 'application/json', 'trainer_token' :Token}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_newname = {
    "pokemon_id": "155866",
    "name": "Чип",
    "photo_id": 1
}

body_catch = {
  "message": "Покемон пойман в покебол",
  "id": "155866"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = Header, json = body_create)
print(response_create.text)

response_newname = requests.put(url = f'{URL}/pokemons', headers = Header, json = body_newname)
print(response_newname.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = Header, json = body_catch)
print(response_catch.text)