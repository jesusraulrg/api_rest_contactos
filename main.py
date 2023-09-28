from fastapi import FastAPI
import csv
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/contactos")
async def get_contactos():
    # Definimos una lista para almacenar los datos de contactos en formato JSON
    contactos = []

    try:
        # Abrir el archivo CSV en modo lectura
        with open('contactos.csv', mode='r', encoding='utf-8') as csv_file:
            # Utilizar el lector CSV para leer el archivo
            csv_reader = csv.DictReader(csv_file)
            
            # Iterar a través de las filas del archivo CSV
            for row in csv_reader:
                # Convertir cada fila en un diccionario
                contacto = {
                    "nombre": row["nombre"],
                    "email": row["email"],
                }
                # Agregar el contacto a la lista
                contactos.append(contacto)

    except FileNotFoundError:
        return {"error": "El archivo contactos.csv no se encontró"}

    # Convertir la lista de contactos a formato JSON
    contactos_json = json.dumps(contactos)

    # Retornar los contactos en formato JSON en la respuesta
    return contactos_json
