import pandas as pd

amazon_url = 'https://drive.google.com/file/d/1T7zK8OqQ-arYTFzMDTTobD2TXOQmlrgc/view?usp=share_link'
amazon = 'https://drive.google.com/uc?export=download&id='+amazon_url.split('/')[-2]

netflix_url = 'https://drive.google.com/file/d/1HRGpJw7xrluH0O1FwLPbzhMRh7ibSkvO/view?usp=share_link'
netflix = 'https://drive.google.com/uc?export=download&id='+netflix_url.split('/')[-2]

hulu_url = 'https://drive.google.com/file/d/1MnGjuCAB1TwUleTXRCGp8DeSHkXnOZMm/view?usp=share_link'
hulu = 'https://drive.google.com/uc?export=download&id='+hulu_url.split('/')[-2]

disney_url = 'https://drive.google.com/file/d/14QdATtN8kJBZHgXFR3VDm89Aq2-ND9fo/view?usp=share_link'
disney = 'https://drive.google.com/uc?export=download&id='+disney_url.split('/')[-2]

rating1_url = 'https://drive.google.com/file/d/1nKTpA16pbzVuN9CMJxDFVsiNPN0OsVNF/view?usp=share_link'
rating1 = 'https://drive.google.com/uc?export=download&id='+rating1_url.split('/')[-2]

rating2_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating2 = 'https://drive.google.com/uc?export=download&id='+rating2_url.split('/')[-2]

rating3_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating3 = 'https://drive.google.com/uc?export=download&id='+rating3_url.split('/')[-2]

rating4_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating4 = 'https://drive.google.com/uc?export=download&id='+rating4_url.split('/')[-2]

rating5_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating5 = 'https://drive.google.com/uc?export=download&id='+rating5_url.split('/')[-2]

rating6_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating6 = 'https://drive.google.com/uc?export=download&id='+rating6_url.split('/')[-2]

rating7_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating7 = 'https://drive.google.com/uc?export=download&id='+rating7_url.split('/')[-2]

rating8_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating8 = 'https://drive.google.com/uc?export=download&id='+rating8_url.split('/')[-2]

rating9_url = 'https://drive.google.com/file/d/1Npoa3s4tm15v22Zhwt8kl6JQnPe0Aq_X/view?usp=share_link'
rating9 = 'https://drive.google.com/uc?export=download&id='+rating9_url.split('/')[-2]

def obtener_datos_plataforma(platform):
  """
  lectura de datasets transformados por plataforma
  """
  
  if(platform == 'amazon'):
		
    return pd.read_csv(amazon)

  if(platform == 'hulu'):
    
    return pd.read_csv(hulu)

  if(platform == 'disney'):
    
    return pd.read_csv(disney)

  if (platform == 'netflix'):

    return pd.read_csv(netflix)


def obtener_rating(path):
  """
  lectura de datasets de ratings de peliculas por usuarios de todas las plataformas
  """

  if (path == 1):
  
    return pd.read_csv(rating1)
  
  if(path == 2):
  
    return pd.read_csv(rating2)
  
  if (path == 3):
  
    return pd.read_csv(rating3)
  
  if (path == 4):
  
    return pd.read_csv(rating4)
  
  if (path == 5):
  
    return pd.read_csv(rating5)
  
  if (path == 6):
  
    return pd.read_csv(rating6)
  
  if (path == 7):
  
    return pd.read_csv(rating7)
  
  if (path == 8):
  
    return pd.read_csv(rating8)
  
  if (path == 9):
	
    return pd.read_csv(rating9)









