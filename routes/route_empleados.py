from datetime import date, time
from fastapi import APIRouter
from config.db import db_pool
from psycopg2 import sql
import psycopg2.extras

route_empleado = APIRouter()


@route_empleado.get("/empleados")
def get_empleados(presupuesto=0):
   conn = db_pool.getconn()
   try:
      with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
         dict_cur.execute("select codigo_empleado,"+
                        "concat( trim(nombre1),' ',trim(nombre2),' ',apellido1,' ',apellido2) as nombre_completo, " + 
                        "concat( codigo_empleado,'-',trim(nombre1),' ', trim(nombre2),' ',apellido1,' ',apellido2) as nombre_codigo " + 
                        "from payroll.empleado e " +
                        "inner join payroll.persona p on e.persona_idpersona = p.idpersona " +
                        "where fecha_salida is null " +
                        "and funcion = 'C-Campo' " +
                        "and proyecto_presupuesto = "+ str(presupuesto)+" " +
         	            "and codigo_empleado not in (select eb.codigo_empleado  from horas.empleado_boleta eb " +
								"                             where eb.fecha_final is null)")
         result = dict_cur.fetchall()
         dict_cur.close()
         db_pool.putconn(conn)
      return result
   except Exception as e:
      return [e]


@route_empleado.post ("/cerrar")
async def sacar_de_boleta_empleado(id_boleta=0, codigo_empleado='', fecha='', hora=''):

   try:
      fijar_valores(id_boleta, codigo_empleado, fecha, hora)
      return {'mensaje':'Exclente'}
   except Exception as e:
      return {'mensaje':e}



def fijar_valores(id_boleta, codigo_empleado, fecha, hora):
   
   query= sql.SQL("UPDATE horas.empleado_boleta " +
                           "SET   fecha_final=%s ," + 
                           "      hora_final=%s " +
                           "where id_boleta=%s and codigo_empleado= %s")


   valores = (fecha,hora,id_boleta,codigo_empleado)

   conn = db_pool.getconn()

   print('datos enviados por el usuarios....')
   print(valores)

   try:
      with conn.cursor() as cursor:
         cursor.execute(query,valores)

      conn.commit()
   finally:
      db_pool.putconn(conn)