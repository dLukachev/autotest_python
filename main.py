URL_POK = 'https://api.pokemonbattle.ru/v2/pokemons'
URL_TRA = 'https://api.pokemonbattle.ru/v2/trainers'
URL_TRA_MY = 'https://api.pokemonbattle.ru/v2/trainers?trainer_id=11624'
URL_TRA_ADD = 'https://api.pokemonbattle.ru/v2/trainers/add_pokeball'
URL_POK_KILL = 'https://api.pokemonbattle.ru/v2/pokemons/knockout'

HEADER = {'Content-Type' : 'Application/json',
          'trainer_token' : 'TRAINER_TOKEN'} #Заменить TRAINER_TOKEN на свой

body_null = {

}

body_create = {  
    "name": "Питон",
    "photo_id": 4
}

