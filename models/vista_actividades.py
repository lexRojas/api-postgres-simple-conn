


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
    
    