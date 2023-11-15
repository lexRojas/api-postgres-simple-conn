import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_actividades = APIRouter()


@route_actividades.get("/tb_actividades")
def get_actividades(presupuesto='', elemento = ''):
   with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select "
                           "tpm.presupuesto ," +
                           "tpm.codigo_manobra ," +
                           "tm.actividad," +
                           "tum.descripcion unidad_medida," +
                           "tpm.cantidad," +
                           "tpm.rendimiento " +
                        "from tb_presup_manobra tpm " +
                        "inner join tb_manoobra tm on tpm.codigo_manobra = tm.codigo_manobra " +
                        "inner join tb_unidad_medida tum  on tpm.unidad_medida = tum.cod_unidad_medida " +
                        "where (presupuesto IN ('"+ presupuesto +"')) AND (cod_ele_sec IN ('"+ elemento+"'))" )
      result = dict_cur.fetchall()
      dict_cur.close()

   return result

