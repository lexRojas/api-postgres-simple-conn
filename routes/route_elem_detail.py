import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_elem_detail = APIRouter()


@route_elem_detail.get("/elem_detail")
def get_elem_detail(presupuesto='', sector = 'A'):
   with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
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
      elementos = dict_cur.fetchall()
      dict_cur.close()

      row_id = 1
      elem_detail = []

      for row in elementos:
         
         cod_ele_sec       = row['cod_ele_sec']
         descripcion       = row['descripcion']
         comentario        = row['comentario']
         unidad_medida     = row['unidad_medida']
         cantidad_elemento = row['cantidad_elemento']
         children          = row['children']
         
         with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur_2:
            dict_cur_2.execute("select "
                                 "tpm.presupuesto ," +
                                 "tpm.codigo_manobra ," +
                                 "tm.actividad," +
                                 "tum.descripcion unidad_medida," +
                                 "tpm.cantidad," +
                                 "tpm.rendimiento " +
                              "from tb_presup_manobra tpm " +
                              "inner join tb_manoobra tm on tpm.codigo_manobra = tm.codigo_manobra " +
                              "inner join tb_unidad_medida tum  on tpm.unidad_medida = tum.cod_unidad_medida " +
                              "where (presupuesto IN ('"+ presupuesto +"')) AND (cod_ele_sec IN ('"+ cod_ele_sec +"'))" )
            actividades  = dict_cur_2.fetchall()
            dict_cur_2.close()

            elem_detail.append({
               'key'          : row_id,
               'presupuesto'  : presupuesto,
               'cod_ele_sec'  : cod_ele_sec,
               'descripcion'  : descripcion,
               'comentario'   : comentario,
               'unidad_medida':unidad_medida,
               'cantidad_elemento':cantidad_elemento,
               'children'     :children,
               'actividades' : actividades
            })


      return (elem_detail)















   return result

