

from config.db import *
from fastapi import APIRouter
from models.modelos import * 
from sqlalchemy import join,select,text
from sqlalchemy.orm import load_only

route_vista_actividades = APIRouter()


@route_vista_actividades.get("/tb_vista_actividades" )
def get_vista_actividades(presupuesto='', sector = ''):

   # stmt = text("select tb_presup_manobra.presupuesto," +
	# 		            "tb_presup_manobra.codigo_manobra , "		 +
	# 	               "tb_elementos_sectores.cod_ele_sec ," +
	# 	               "tb_elementos_sectores.descripcion," + 
	# 	               "tb_elementos_sectores.comentario " +
   #             "from tb_presup_manobra  " +
   #             "inner join  tb_elementos_sectores on  tb_presup_manobra.cod_ele_sec = tb_elementos_sectores.cod_ele_sec " +
   #             "where tb_presup_manobra.presupuesto = '2023317' ")   
   
   stmt = select(tb_presup_manobra,tb_unidad_medida).join(tb_presup_manobra, tb_unidad_medida).options(load_only(tb_presup_manobra.presupuesto), load_only(tb_unidad_medida.cod_unidad_medida,tb_unidad_medida.descrip_larga)).where(tb_presup_manobra.presupuesto=='2023317')

   result  = session.scalars(stmt).all()
   
   return result
