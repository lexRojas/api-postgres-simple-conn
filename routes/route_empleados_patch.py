from datetime import date, time
from fastapi import APIRouter
from config.db import db_pool
from fastapi import FastAPI, HTTPException
from psycopg2 import sql
from psycopg2 import errors
import psycopg2.extras
from models.vista_actividades import cerrarValores
import logging 

route_empleado_patch = APIRouter()


@route_empleado_patch.post ("/cerrar")
def cerrar(valores:cerrarValores):

   #query= sql.SQL("UPDATE horas.empleado_boleta SET fecha_final=%s          , hora_final=%s      where id_boleta=%s and codigo_empleado=%s ;")

   strFecha = valores.fecha_final.strftime("%Y-%m-%d")
   strHora = valores.hora_final.strftime("%H:%M") 


   miSQL = "UPDATE horas.empleado_boleta SET fecha_final='"+ strFecha +"', hora_final='"+ strHora +"' where id_boleta="+ str(valores.id_boleta) +" and codigo_empleado='"+ valores.codigo_empleado +"';"
   
   conn = db_pool.getconn()

   print(miSQL)

   try:
      with conn.cursor() as icursor:
         icursor.execute(miSQL)
      conn.commit()
      return {'mensaje':'Felicidades!!!'}
   except  Exception as e:
      return {'mensaje':e}
   finally:
      db_pool.putconn(conn)