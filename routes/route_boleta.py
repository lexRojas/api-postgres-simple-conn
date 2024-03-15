from fastapi import APIRouter
from config.db import conn
import psycopg2.extras
from models.vista_actividades import boleta

route_boleta = APIRouter()


@route_boleta.post("/boleta")
def set_boleta(data):
   
   with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      
        sql= f"INSERT INTO horas.boleta (fecha_inicio,proyecto,ubicacion,comentarios,cantidad_medida,unidad_medida,hora_inicio,hora_final,cerrada,codigo_manobra,fecha_final) VALUES('{data.fecha_inicio}','{data.proyecto}','{data.ubicacion}','{data.comentarios}',{data.cantidad_medida},'{data.unidad_medida}','{data.hora_inicio}','{data.hora_final}',{data.cerrada},{data.codigo_manobra},'{data.fecha_final}');" 
      
        dict_cur.execute(sql)
       
        conn.commit
      
   return 1

