from fastapi import APIRouter
from config.db import session

from schemas.schemas import tb_presupuesto_BM
from models.modelos import tb_presupuesto
from typing import Optional


from sqlalchemy import select


route_presupuesto = APIRouter()


@route_presupuesto.get("/tb_presupuesto" )
def get_presupuesto(filtro : Optional[str] = None):
     
   if filtro == None:
      sql = select(tb_presupuesto)
   else:
      filtro = '%'+filtro+'%'
      sql = select(tb_presupuesto).where(tb_presupuesto.proyecto.like (filtro))

   result = session.scalars(sql).all()
   return result
