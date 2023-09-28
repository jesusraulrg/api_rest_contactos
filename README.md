# Design Document: api_rest_contactos

## 1. Descripción
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com).

## 3. Diseño de la DB
Para este ejemplo se utilizará el gestor de bases de datos [SQLite3](https://www.sqlite.org/). con las siguientes tablas:

### 3.1 Tabla: contactos

|No.|Campo|Tipo|Restricciones|Descripción|
|--|--|--|--|--|
|1|id_contactos|int|PRIMARY KEY|Llave primaria de la tabla|
|2|nombre|varchar(100)|NOT NULL|Nombre del usuario|
|3|primer_apellido|varchar(50)|NOT NULL|Primer apellido del usuario|
|4|segundo_apellido|varchar(50)|NOT NULL|Segundo apellido del usuario|
|5|email|varchar(50)|NOT NULL|Correo electrónico|
|6|telefono|varchar(13)|NOT NULL|Numero de telefono|

### 3.2 Script

``` sql
CREATE TABLE IF NOT EXISTS contactos (
    id_contactos INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);
```

## 4. Diseño de la API

### 4.1 ENDPOINT Raiz de la API (GET)

|No.|Propiedad|Detalle|
|--|--|--|
|1|Description||
|2|Summary||
|3|Method||
|4|EndPoint||
|5|Query Param||
|6|Path Param||
|7|Data||
|8|Version||
|9|Status Code (ÉXITO)||
|10|Response Type (ÉXITO)||
|11|Response (ÉXITO)||
|12|CURL||
|13|Status Code (ERROR)||
|14|Response Type (ERROR)||
|15|Response (ERROR)||

### 4.2 ENDPOINT de Obtención de Contactos (GET)

|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Obtener una lista de contactos|
|2|Summary|Endpoint para obtener la lista de contactos|
|3|Method|GET|
|4|EndPoint|http://localhost:8000/contactos|
|5|Query Param|?nombre=Juan|
|6|Path Param|NA|
|7|Data|NA|
|8|Version|v1|
|9|Status Code (ÉXITO)|200|
|10|Response Type (ÉXITO)|application/json|
|11|Response (ÉXITO)|Formato JSON|
|12|CURL|```curl -X GET 'http://localhost:8000/contactos' -H 'accept: application/json'```|
|13|Status Code (ERROR)|400|
|14|Response Type (ERROR)|application/json|
|15|Response (ERROR)|Mensajes de error específicos en formato JSON|

### 4.3 ENDPOINT de Creación de Contactos (POST)

|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Crear un nuevo contacto|
|2|Summary|Endpoint para crear un nuevo contacto|
|3|Method|POST|
|4|EndPoint|http://localhost:8000/contactos|
|5|Query Param|NA|
|6|Path Param|NA|
|7|Data|Datos del nuevo contacto a enviar en el cuerpo de la solicitud (en formato JSON)|
|8|Version|v1|
|9|Status Code (ÉXITO)|201|
|10|Response Type (ÉXITO)|application/json|
|11|Response (ÉXITO)|```{"message" : "Contacto creado con éxito", "datetime" : "21/09/23 10:36"}```|
|12|CURL|```curl -X POST 'http://localhost:8000/contactos' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"nombre": "Juan", "email": "juan@example.com"}'```|
|13|Status Code (ERROR)|400|
|14|Response Type (ERROR)|application/json|
|15|Response (ERROR)|Mensajes de error específicos en formato JSON|

### 4.4 ENDPOINT de Eliminación de Contactos (DELETE)

|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Eliminar un contacto existente|
|2|Summary|Endpoint para eliminar un contacto|
|3|Method|DELETE|
|4|EndPoint|http://localhost:8000/contactos/{id}|
|5|Query Param|NA|
|6|Path Param|id|
|7|Data|NA|
|8|Version|v1|
|9|Status Code (ÉXITO)|204|
|10|Response Type (ÉXITO)|NA|
|11|Response (ÉXITO)||
|12|CURL|```curl -X DELETE 'http://localhost:8000/contactos/123' -H 'accept: application/json'```|
|13|Status Code (ERROR)|400|
|14|Response Type (ERROR)|application/json|
|15|Response (ERROR)|Mensajes de error específicos en formato JSON|

### 4.5 ENDPOINT de Creación de Contactos (POST)

|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Actualizar un contacto existente|
|2|Summary|Endpoint para actualizar un contacto|
|3|Method|PUT|
|4|EndPoint|http://localhost:8000/contactos/{id}|
|5|Query Param|NA|
|6|Path Param|id|
|7|Data|Datos actualizados del contacto a enviar en el cuerpo de la solicitud (en formato JSON)|
|8|Version|v1|
|9|Status Code (ÉXITO)|200|
|10|Response Type (ÉXITO)|application/json|
|11|Response (ÉXITO)|```{"message" : "Contacto actualizado con éxito", "datetime" : "21/09/23 10:36"}```|
|12|CURL|```curl -X PUT 'http://localhost:8000/contactos/123' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"nombre": "Nuevo Nombre", "email": "nuevo@example.com"}'```|
|13|Status Code (ERROR)|400|
|14|Response Type (ERROR)|application/json|
|15|Response (ERROR)|Mensajes de error específicos en formato JSON|
