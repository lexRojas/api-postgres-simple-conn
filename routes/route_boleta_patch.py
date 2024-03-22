from datetime import date, time
from fastapi import APIRouter
from config.db import db_pool
from fastapi import FastAPI, HTTPException
from psycopg2 import sql
from psycopg2 import errors
import psycopg2.extras
from models.vista_actividades import cerrarBoleta
from tools.tools import list_to_str 

route_boleta_patch = APIRouter()


@route_boleta_patch.patch ("/cerrar_boleta")
def cerrar(valores:cerrarBoleta):

   #query= sql.SQL("UPDATE horas.empleado_boleta SET fecha_final=%s          , hora_final=%s      where id_boleta=%s and codigo_empleado=%s ;")

   strFecha = valores.fecha_final.strftime("%Y-%m-%d")
   strHora = valores.hora_final.strftime("%H:%M") 
  
   # miSQL = "UPDATE horas.empleado_boleta SET fecha_final='"+ strFecha +"', hora_final='"+ strHora +"' where id_boleta="+ str(valores.id_boleta) +" and codigo_empleado='"+ valores.
   miSQL = "UPDATE horas.boleta SET cerrada=true where boleta.id in "+ list_to_str(valores.id_boleta) +";"
   miSQL2 ="UPDATE horas.empleado_boleta SET fecha_final='"+ strFecha +"', hora_final='"+ strHora +"' where id_boleta in "+ list_to_str(valores.id_boleta) +" and fecha_final is NULL;"
   
   conn = db_pool.getconn()

   try:
      with conn.cursor() as icursor:
         icursor.execute(miSQL)
         icursor.execute(miSQL2)

      conn.commit()
      return {'resultado':True}
   except  Exception as e:

      return {'resultado':False}
   finally:
      db_pool.putconn(conn)