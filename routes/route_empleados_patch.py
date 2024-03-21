from datetime import date, time
from fastapi import APIRouter
from config.db import db_pool
from psycopg2 import sql
import psycopg2.extras
from models.vista_actividades import cerrarValores
import logging 

route_empleado_patch = APIRouter()


@route_empleado_patch.patch ("/cerrar")
async def cerrar(valores:cerrarValores):

   try:
      await fijar_valores(valores)
      return {'mensaje':'Excelente desde patch'}
   except Exception as e:
      return {'mensaje':e}



async def fijar_valores(values:cerrarValores):
   
   query= sql.SQL("UPDATE horas.empleado_boleta " +
                           "SET   fecha_final=%s ," + 
                           "      hora_final=%s " +
                           "where id_boleta=%s and codigo_empleado= %s")



   conn = db_pool.getconn()

   print('datos enviados por el usuarios....')
   
   print(values)
   print(query)



   try:
      with conn.cursor() as cursor:
         cursor.execute(query,values)
         print(query)

      
      logging.info(conn.commit())
   except Exception as e:
      return {'mensaje':e}
   finally:
      db_pool.putconn(conn)