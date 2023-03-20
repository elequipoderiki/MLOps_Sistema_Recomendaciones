#este modulo simula una conexion a un data lake
import pandas as pd

amazon_url = 'https://drive.google.com/file/d/164lVaSN0CKa8FL478g37633Ue6bAxrXp/view?usp=share_link'
amazon = 'https://drive.google.com/uc?export=download&id='+amazon_url.split('/')[-2]

netflix_url = 'https://drive.google.com/file/d/1z4pMXv5BobPmJ9v7D4psDej4vxxIjuZY/view?usp=share_link'
netflix = 'https://drive.google.com/uc?export=download&id='+netflix_url.split('/')[-2]

hulu_url = 'https://drive.google.com/file/d/1N0LIOKcl_4X1gljFhzE4mN0LXN4s7iUv/view?usp=share_link'
hulu = 'https://drive.google.com/uc?export=download&id='+hulu_url.split('/')[-2]

disney_url = 'https://drive.google.com/file/d/1peB0sK-G0hhFqEfe-4GoddyHVBYj6YRR/view?usp=share_link'
disney = 'https://drive.google.com/uc?export=download&id='+disney_url.split('/')[-2]


def obtener_datos_plataforma(platform):
  """
  lectura de datos crudos de catalogo de peliculas por plataforma
  """
	
  if(platform == 'amazon'):
    
    return pd.read_csv(amazon)

  if(platform == 'hulu'):

    return pd.read_csv(hulu)

  if(platform == 'disney'):

    return pd.read_csv(disney)

  if(platform == 'netflix'):

    return pd.read_csv(netflix)










