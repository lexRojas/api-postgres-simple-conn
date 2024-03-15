from datetime import date, time

from pydantic import BaseModel


class cls_actividades(dict):
    codigo_manobra  : int
    actividad       : str
    um              : str
    cantidad        : int
    rendimiento     : float


class elementos(dict):
    presupuesto : str
    cod_ele_sec : str
    descripcion : str
    comentario  : str
    unidad_medida : str
    cantidad_elemento : int
    actividades: list[cls_actividades] = []
    

class empleados(BaseModel):
    codigo_empleado:str
    nombre_codigo:str
    nombre_completo:str


class boleta(BaseModel):
    id:int
    fecha_inicio : date
    proyecto  : str
    ubicacion  : str
    comentarios  : str
    cantidad_medida : float
    unidad_medida: str
    hora_inicio: time
    hora_final: time
    cerrada:bool
    codigo_manobra: int
    fecha_final: date
    empleados_asignados: list[empleados] 
    