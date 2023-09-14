import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_elementos = APIRouter()


@route_elementos.get("/tb_elementos")
def get_elementos(presupuesto='', sector = 'A'):
   with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select es.presupuesto, " + 
                       "es.cod_ele_sec, "+
                       "es.descripcion,"+
                       "es.comentario,"+
                       "um.descripcion unidad_medida, "+
                       "es.cantidad_elemento "+     
                       "from tb_elementos_sectores es " +
                       "inner join tb_unidad_medida um on um.cod_unidad_medida = es.unidad_medida " +
                       "where es.presupuesto= '"+ presupuesto+"' and es.sector= '"+ sector +"' ")
      result = dict_cur.fetchall()
      dict_cur.close()

   return result

