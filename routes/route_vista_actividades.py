from typing import List

from fastapi import APIRouter
from config.db import conn
import psycopg2.extras
from models.vista_actividades import elementos

route_vista_actividades = APIRouter()


@route_vista_actividades.get("/tb_vista_actividades", response_model=elementos )
def get_vista_actividades(presupuesto='', sector = ''):
   mis_elementos =elementos
   with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select es.presupuesto," +
                           "es.cod_ele_sec, " +
                           "es.descripcion, " +
                           "es.comentario, " +
                           "um.descripcion unidad_medida,  " +
                           "es.cantidad_elemento " +
                        "from tb_elementos_sectores es  " +
                        "inner join tb_unidad_medida um on um.cod_unidad_medida = es.unidad_medida  " +
                        "where es.presupuesto= '"+ presupuesto +"' and es.sector= '"+ sector +"'  " +
                        "order by es.presupuesto, es.cod_ele_sec")  

      result = dict_cur.fetchall()
   for elemento  in result:
      print(elemento)
      cod_ele_sec = elemento['cod_ele_sec']      
      print(cod_ele_sec)

      registro  = dict(elemento)

      with conn().cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) as dict_cur2:
         dict_cur2.execute("select " +
                           "   tpm.presupuesto ," +
                           "   tpm.codigo_manobra ," +
                           "   tm.actividad," +
                           "   tum.descripcion um," +
                           "   tpm.cantidad," +
                           "   tpm.rendimiento  " +
                           "from tb_presup_manobra tpm " +
                           "inner join tb_manoobra tm on tpm.codigo_manobra = tm.codigo_manobra " +
                           "inner join tb_unidad_medida tum  on tpm.unidad_medida = tum.cod_unidad_medida " +
                           "where (presupuesto IN ('"+presupuesto+"')) AND (cod_ele_sec IN ('"+cod_ele_sec+"'))")
         
         result2 = dict_cur2.fetchall()
         registro['actividades'] = dict(result2)
         dict_cur2.close()

   #fin_for_elemento       

   mis_elementos = mis_elementos + registro


   dict_cur.close()

   return mis_elementos

