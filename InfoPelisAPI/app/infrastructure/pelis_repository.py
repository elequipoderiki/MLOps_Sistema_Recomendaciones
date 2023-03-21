import pandas as pd
import numpy as np
from .data.conexion_transformaciones import *
import gc #garbage collector

# AUXILIARES

def peli_mayor_duracion(df, anio, tipo_duracion):
  """
  Dado un año, tipo de duración y dataset devuelve película con mayor duración

  Parameters
  ---------
  tipo_duracion: str
    palabra min para peliculas o season para television
  df: object
    dataframe con columna de tipo de duracion
  anio: int
    año del cual queremos la película de mayor duración
  """
  
  pelis = df[df.duration_type == tipo_duracion]

  #si filtro año es requerido
  if (anio > 0):
  
    pelis = pelis[pelis.release_year == anio]
  
  idmax = pelis[['duration_int']].idxmax()
  
  pelis_mayor_dur = pelis.loc[idmax.values]
  
  return pelis_mayor_dur  



def mayor_peli_de_todas(year, duration_type):
  """
  Dado un año y tipo de duración devuelve película con mayor duración
  para todas las plataformas

  Parameters
  ---------
  duration_type: str
      palabra min para peliculas o season para television
  year: int
    año del cual queremos la película de mayor duración
  """

  platforms = ['amazon','netflix','hulu','disney']
  
  mayor_dur = 0
  
  mayor_peli = pd.NA
  
  for platform in platforms:
  
    df = obtener_datos_plataforma(platform)    
  
    #obtenemos la peli de mayor duracion para este dataset
    peli = peli_mayor_duracion(df, year, duration_type)
  
    #liberamos memoria en cada iteracion
    del df
    gc.collect()
  
    #si la duracion de la peli supera a la mayor anterior la guardamos 
    if peli.duration_int > mayor_dur:
  
      mayor_peli = peli
      
  return mayor_peli  



def cantidad_mayor_rating_xanio(id_pelis, score):
  """
  obtiene cantidad de peliculas con mayor ratings 

  Parameters
  ---------
  id_pelis: str
      ids de peliculas que queremos filtrar 
  score: int
    puntaje que deben superar las peliculas a contabilizar
  """

  cantidad_pelis = 0

  for i in range(1,9):

    data = obtener_rating(i)

    #seleccionamos datos de las peliculas que nos interesan
    pelis = data[data['movieId'].isin(id_pelis)]

    #liberamos memoria asignada al dataset
    del data
    gc.collect()

    #agrupamos por peli y promediamos puntaje
    pelis_rating = pelis.groupby(['movieId'])['rating'].mean()

    #contabilizamos peliculas con rating mayor al score de cada dataset
    cantidad_pelis += len(pelis_rating[pelis_rating > score])
  
  return cantidad_pelis



#FUNCION 1
def mayor_duracion(year:int , platform:str , duration_type:str ):
  """
  funcion que obtiene pelicula con mayor duracion con filtros de año, plataforma y tipo duracion

  Parameters
  ---------
  duration_type: str
    palabra min para peliculas o season para television
  platform: str
    nombre de plataforma con catalogo de peliculas
  anio: int
    año del cual queremos la película de mayor duración
  """

  #si filtro plataforma es requerido
  if(len(platform) > 0):
 
    df = obtener_datos_plataforma(platform)
 
    return peli_mayor_duracion(df, year, duration_type)
 
  else: #si no hay filtro busco en todos      
 
    return mayor_peli_de_todas(year, duration_type)




#FUNCION 2
def cantidad_mayor_rating(platform: str, score: float, year: int):
  """
  funcion que contabiliza peliculas de una plataforma que superen puntaje en un año elegido

  Parameters
  ---------
  score: float
    puntaje que las peliculas a contabilizar deben superar
  platform: str
    nombre de plataforma con catalogo de peliculas
  anio: int
    año del cual queremos la película de mayor duración
  """

  #traemos dataset desde el data lake
  df = obtener_datos_plataforma(platform)

  id_pelis = df[df.release_year == year].id

  return  cantidad_mayor_rating_xanio(id_pelis, score)




#FUNCION 3
def cantidad_por_plataforma(platform):
  """
  funcion para contabilizar peliculas por plataforma

  Parameters
  ---------
  platform: str
    nombre de plataforma con catalogo de peliculas
  """

  df = obtener_datos_plataforma(platform) 
  
  return len(df.id.unique())




#FUNCION 4
from collections import defaultdict

def actor_mas_apariciones(platform, year):
  """
  obtiene actor mas repetido por plataforma y año

  Parameters
  ---------
  platform: str
    nombre de plataforma con catalogo de peliculas
  year: int
    año del cual queremos la película de mayor duración
  """

  df = obtener_datos_plataforma(platform) 
  
  #filtramos pelis por año 
  pelis = df[df.release_year == year]

  #eliminamos campos nulos
  appearance_groups = df['cast'].dropna()
  
  #aplanamos nombres del casting de cada pelicula
  appearances = [item.strip() for group in appearance_groups for item in group.split(',')]
  
  #diccionario de todos los actores junto con su cantidad de apariciones
  cast = defaultdict(int)
  
  for item in appearances:
    
    cast[item] += 1
  
  #obtenemos el actor con mas apariciones
  res = max(cast.items(), key=lambda a:a[1])
  return pd.DataFrame({'actor':res[0], 'apariciones':res[1]},index=[0])

    
      

