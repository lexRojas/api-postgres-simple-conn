import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_presupuesto = APIRouter()


@route_presupuesto.get("/tb_presupuesto")
def get_presupuesto(filtro=''):
   with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select presupuesto,proyecto from public.tb_presupuesto where proyecto like '%"+ filtro.upper() +"%' order by fecha_cambio desc limit 10")
      result = dict_cur.fetchall()
      dict_cur.close()
   return result

