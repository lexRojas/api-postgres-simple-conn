import json
from fastapi import APIRouter
from config.db import db_pool
import psycopg2.extras

route_reset = APIRouter()


@route_reset.get("/reset")
def reset():
   conn = db_pool.getconn()
   conn.rollback()
   return {"mensaje":'reseteado'}

