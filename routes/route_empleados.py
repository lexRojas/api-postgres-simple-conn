import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_empleado = APIRouter()


@route_empleado.get("/empleados")
def get_empleados(presupuesto=0):
   
   with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select codigo_empleado,"+
                       "concat( trim(nombre1),' ',trim(nombre2),' ',apellido1,' ',apellido2) as nombre_completo, " + 
                       "concat( codigo_empleado,'-',trim(nombre1),' ', trim(nombre2),' ',apellido1,' ',apellido2) as nombre_codigo " + 
                       "from payroll.empleado e " +
                       "inner join payroll.persona p on e.persona_idpersona = p.idpersona " +
                       "where fecha_salida is null " +
                       "and funcion = 'C-Campo' " +
                       "and proyecto_presupuesto = "+ str(presupuesto)+"")
      result = dict_cur.fetchall()
      dict_cur.close()

   return result

