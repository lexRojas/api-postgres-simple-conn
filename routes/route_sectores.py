import json
from fastapi import APIRouter
from config.db import db_pool
import psycopg2.extras

route_sectores = APIRouter()

#cursor_factory=psycopg2.extras.RealDictCursor

@route_sectores.get("/tb_sectores")
def get_sectores(presupuesto=''):
   conn = db_pool.getconn()
   with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as dict_cur:
      dict_cur.execute("select presupuesto, codigo_sector,descripcion from public.tb_sectores_proyectos sp where sp.presupuesto= '"+ presupuesto +"'")
      result = dict_cur.fetchall()
      dict_cur.close()
      db_pool.putconn(conn)
   return result

