from pydantic import BaseModel
from typing import Optional
from datetime import date

class Usuario_BM(BaseModel):
    id: Optional[int] 
    name: str
    login: str
    password: str
    perfil: str

class Tb_Usuario_BM(BaseModel):
    nombre: str
    password: str
    fecha_vencimiento: date
    fecha_cambio : date
    login : str
    activo : bool


class tb_presupuesto_BM(BaseModel):  
    presupuesto: str
    proyecto: str
    propietario: str
    fecha_apertura: date
    hora_apertura :str
    area_construccion: float
    fecha_cambio: date
    cod_usuario : str
    tipo_licitacion : int
    responsable : int
    num_licitacion : str
    activo: bool
    class Config:
        orm_mode = True