import json
from fastapi import APIRouter
from config.db import session
import psycopg2.extras

from schemas.schemas import tb_presupuesto_BM
from models.modelos import tb_presupuesto
from typing import Optional


from sqlalchemy import select


route_presupuesto = APIRouter()


@route_presupuesto.get("/tb_presupuesto" )
def get_presupuesto(filtro : Optional[str] = None):
   
#    with conn().cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
#       dict_cur.execute("select presupuesto,proyecto from public.tb_presupuesto where proyecto like '%"+ filtro.upper() +"%' order by fecha_cambio desc limit 10")
#       result = dict_cur.fetchall()
#       dict_cur.close()
#    return result

   
   if filtro == None:
      sql = select(tb_presupuesto)
   else:
      filtro = '%'+filtro+'%'
      sql = select(tb_presupuesto).where(tb_presupuesto.presupuesto.like (filtro))

   result = session.scalars(sql).all()
   return result
