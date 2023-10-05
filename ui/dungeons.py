import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"
#URI = "https://www.dnd5eapi.co/api/proficiencies/light-armor"
#URI = "https://www.dnd5eapi.co/api/classes/barbarian"

response = requests.get(URI)

#print(f"GET: {response.text}")
response_json = json.loads(response.text)


#print(f"{response_json['count']}")
#print(f"{response_json['results']}")


# 0 en el array
    # navegar dentro del archivo json

seleccion = int(input("Selecciona un personaje: "))
print(f"{response_json['results'][(seleccion)]['name']}")

'''
for i in range(12):
    elemento = response_json['results'][i]['name']
    print(f"{i + 1}. {elemento}")
'''
