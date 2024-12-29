import pytest
import requests
import main


def test_statuscode_gt():
    result = requests.get(url=main.URL_TRA, headers=main.HEADER, json=main.body_null)
    assert result.status_code == 200

#Это цикл на создание, изменения имени, добавление в покебол и удаления покемона. 
request_create = requests.post(url=main.URL_POK, headers=main.HEADER, json=main.body_create) #Создаю покемона
print(f"{request_create.text} А вот json")
print(request_create.json)

id = request_create.json()["id"] #Записываю ID в переменную

body_put = {
    "pokemon_id": f"{id}",
    "name": "Делаю дзшку",
    "photo_id": 4
}

request_put = requests.put(url=main.URL_POK, headers=main.HEADER, json=body_put) #Меняю имя у созданного покемона
print(f"\n{request_put.text} А вот json")
print(f"{request_put.json}")

body_add_in_pok = {
    "pokemon_id": f"{id}"
}

request_add_pokeball = requests.post(url=main.URL_TRA_ADD, headers=main.HEADER, json=body_add_in_pok) #Добавляю в покебол
print(f"\n{request_add_pokeball.text} А вот json")
print(f"{request_add_pokeball.json}")

body_kill = {
    "pokemon_id": f"{id}"
}

request_kill = requests.post(url=main.URL_POK_KILL, headers=main.HEADER, json=body_kill) #Убиваю, чтобы завершить его цикл:)
print(f"\n{request_kill.text} А вот json")
print(f"{request_kill.json}")
