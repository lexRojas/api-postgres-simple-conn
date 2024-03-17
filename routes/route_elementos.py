import json
from fastapi import APIRouter
from config.db import db_pool
import psycopg2.extras

route_elementos = APIRouter()


@route_elementos.get("/tb_elementos")
def get_elementos(presupuesto='', sector = 'A'):
   conn = db_pool.getconn()
   with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select es.presupuesto,"  +
                           "es.cod_ele_sec," +
                           "es.descripcion," +
                           "es.comentario," +
                           "um.descripcion unidad_medida, " +
                           "es.cantidad_elemento," +
                           "count(tpm.presupuesto)>0 children " +
                        "from tb_elementos_sectores es " +
                        "inner join tb_unidad_medida um on um.cod_unidad_medida = es.unidad_medida " +
                        "inner join tb_presup_manobra tpm on es.presupuesto = tpm.presupuesto and es.cod_ele_sec = tpm.cod_ele_sec " +
                        "where es.presupuesto= '"+ presupuesto+"' and es.sector= '"+ sector +"' " +
                        "group by es.presupuesto,  " +
                           "es.cod_ele_sec, " +
                           "es.descripcion," +
                           "es.comentario," +
                           "um.descripcion," +
                           "es.cantidad_elemento" )
      result = dict_cur.fetchall()
      dict_cur.close()
      db_pool.putconn(conn)

   return result

