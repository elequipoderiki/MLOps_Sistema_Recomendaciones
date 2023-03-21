from fastapi import FastAPI
from helpers.filter_classes import *
from infrastructure.pelis_repository import mayor_duracion, cantidad_mayor_rating, cantidad_por_plataforma, actor_mas_apariciones
from fastapi import Response

description = """
Esta API le permite realizar consultas acerca de películas rentadas de Netflix, Amazon, Disney y Hulu. 🚀

## Película Mayor Duración

Consulte película de mayor duración por plataforma o en todas.

Las opciones son: 

* **Year** número de 4 digitos (ejemplo 1989).
* **Duration Type** minutaje o temporada (valores aceptados: min o sesion).
* **Platform** nombre de plataforma a consultar (Netflix, Amazon, Disney y Hulu).

## Cantidad Películas Mayor Puntaje

Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año.

Las opciones son: 

* **Year** número de 4 digitos (ejemplo 1989).
* **Scored** puntaje mínimo de las peliculas seleccionadas (entre 1 y 5)
* **Platform** nombre de plataforma a consultar (Netflix, Amazon, Disney y Hulu).

## Cantidad Películas 

Cantidad de películas por plataforma.

Las opciones son: 

* **Platform** nombre de plataforma a consultar (Netflix, Amazon, Disney y Hulu).

## Actor con Mayor Apariciones

Devuelve actor con mayor cantidad de apariciones por año y plataforma

Las opciones son: 

* **Year** número de 4 digitos (ejemplo 1989).
* **Platform** nombre de plataforma a consultar (Netflix, Amazon, Disney y Hulu).

"""

tags_metadata = [
    {
        "name": "película mayor duración",
        "description": "Consulta que admite filtros opcionales de **año**, **plataforma** y **tipo de duración**.",
    },
    {
        "name": "cantidad películas mayor puntaje",
        "description": "Consulta que admite filtros de **año**, **plataforma** y **puntaje**.",
        
    },
    {
        "name": "cantidad películas",
        "description": "Consulta que admite filtros **plataforma**.",        
    },
    {
        "name": "actor con mayor apariciones",
        "description": "Consulta que admite filtros **plataforma** y **año**.",        
    }
]

app = FastAPI(
    title="Info Pelis X Plataforma",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ricardo Ramos",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


#ENDPOINTS


@app.post("/get_max_duration",tags=["película mayor duración"])

def get_max_duration(filtro: FiltrosMayorDuracion):

	return Response(mayor_duracion(filtro.year, filtro.platform, filtro.duration_type).to_json(orient="records"), media_type="application/json")




@app.post("/get_score_count",tags=["cantidad películas mayor puntaje"])

def get_score_count(filtro: FiltrosMayorPuntaje):

    return cantidad_mayor_rating(filtro.platform, filtro.score, filtro.year)




@app.post("/get_count_platform",tags=["cantidad películas"])

def get_count_platform(filtro: FiltrosMayorCantidad):

    return cantidad_por_plataforma(filtro.platform)




@app.post("/get_actor",tags=["actor con mayor apariciones"])

def get_actor(filtro: FiltrosMayorActor):

    return Response(actor_mas_apariciones( filtro.platform, filtro.year).to_json(orient="records"), media_type="application/json")






