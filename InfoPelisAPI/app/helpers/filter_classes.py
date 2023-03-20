from pydantic import BaseModel
from typing import Optional

class FiltrosMayorDuracion(BaseModel):
	year: Optional[str]=''
	platform: Optional[str]='amazon'
	duration_type: Optional[str]='min'
	
class FiltrosMayorPuntaje(BaseModel):
	year: int=2019
	platform: str='amazon'
	score: float=3
	
class FiltrosMayorCantidad(BaseModel):
	platform: str

class FiltrosMayorActor(BaseModel):
	year: int=2019
	platform: str='amazon'
