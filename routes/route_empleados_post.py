from datetime import date, time
from fastapi import APIRouter
from config.db import db_pool
from fastapi import FastAPI, HTTPException
from psycopg2 import sql
from psycopg2 import errors
import psycopg2.extras
from models.vista_actividades import addEmpleadosClass
import logging 

route_empleado_post = APIRouter()


@route_empleado_post.post ("/addEmpleado")
def cerrar(valores:addEmpleadosClass):

   strFecha = valores.fecha_inicio.strftime("%Y-%m-%d")
   strHora = valores.hora_inicio.strftime("%H:%M") 

   miSQL = "INSERT INTO horas.empleado_boleta (id_boleta, codigo_empleado, fecha_inicio, hora_inicio) VALUES("+str(valores.id_boleta)+" , '"+ valores.codigo_empleado+"', '"+ strFecha +"', '"+ strHora +"');"

   
   conn = db_pool.getconn()

   print(miSQL)

   try:
      with conn.cursor() as icursor:
         icursor.execute(miSQL)
      conn.commit()
      return {'resultado':True}
   except  Exception as e:
      return {'resultado':False}
   finally:
      db_pool.putconn(conn)