import json
from fastapi import APIRouter
from config.db import conn
import psycopg2.extras

route_reset = APIRouter()


@route_reset.get("/reset")
def reset():
   conn().rollback()
   return {"mensaje":'reseteado'}

