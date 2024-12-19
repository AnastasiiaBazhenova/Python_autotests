import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '<YOUR_TOKEN>'
Header = {'Content-Type' : 'application/json', 'trainer_token' :Token}
Trainer_id = '12478'
Trainer_name = 'Nastya'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response_get.json()["data"][0]['name'] == 'Бульбазавр'


@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', Trainer_id), ('id', '155866')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : Trainer_id})
    assert response_parametrize.json()["data"][0][key] == value

def test_trainer_name():
    response_trainer_name = requests.get(url=f'{URL}/me', params={'trainer_id': Trainer_id}, headers=Header)
    response_trainer_name.raise_for_status() 
    assert response_trainer_name.json()['data'][0]['trainer_name'] == 'Nastya'

def test_trainer_status_code():
    response_trainer_status_code = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : Trainer_id}, headers=Header)
    assert response_trainer_status_code.status_code == 200
