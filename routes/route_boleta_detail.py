from fastapi import APIRouter
from config.db import db_pool
from fastapi import FastAPI, HTTPException
from psycopg2 import sql
import psycopg2.extras

route_boleta_detail = APIRouter()


@route_boleta_detail.get("/boleta_detail")
def get_boleta(presupuesto='', cerrada = False):
   conn = db_pool.getconn()

   with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select b.id, " +
                        "   b.fecha_inicio, " +
                        "   b.codigo_manobra ," +
                        "   b.comentarios," +
                        "   concat( b.cantidad_medida,' ' ,b.unidad_medida) cantidad_asignada " +
                     "from horas.boleta b " +
                     "where b.proyecto  = '"+ presupuesto+"' and cerrada =" + cerrada)
      

      boletas = dict_cur.fetchall()
      dict_cur.close()

      row_id = 1
      boleta_detail = []

      for row in boletas:
         id                = row['id']
         fecha_inicio      = row['fecha_inicio']
         codigo_manobra    = row['codigo_manobra']
         comentarios       = row['comentarios']
         cantidad_asignada = row['cantidad_asignada']
         
         with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur_2:
            dict_cur_2.execute("select b.id, " +
                                "       eb.codigo_empleado ,	" +
                                "       p.nombre_completo " +
                                " from horas.boleta b " +
                                " inner join horas.empleado_boleta eb on b.id = eb.id_boleta " +
                                " inner join payroll.empleado e on eb.codigo_empleado = e.codigo_empleado " +
                                " inner join payroll.persona_empleado pe on e.idempleado  = pe.empleadoes_idempleado " +
                                " inner join payroll.persona p on pe.persona_idpersona = p.idpersona " +
                                " where b.id = " + str(id) )




            empleados  = dict_cur_2.fetchall()
            dict_cur_2.close()

            boleta_detail.append({
               'id'                :id,
               'fecha_inicio'      :fecha_inicio,
               'codigo_manobra'    :codigo_manobra,
               'comentarios'       :comentarios,
               'cantidad_asignada' :cantidad_asignada,
               'empleados'         : empleados
            })

      db_pool.putconn(conn)
      return (boleta_detail)

