# Design Document: api_rest_contactos

## 1. Descripción
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com).

## 3. Diseño de la DB
Para este ejemplo se utilizará el gestor de bases de datos [SQLite3](https://www.sqlite.org/). con las siguientes tablas:

|No.|Campo|Tipo|Restricciones|Descripción|
|--|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|
