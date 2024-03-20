from fastapi import APIRouter, HTTPException
from config.db import db_pool
import psycopg2.extras
from psycopg2 import sql

from models.vista_actividades import boleta


route_boleta = APIRouter()


@route_boleta.post("/boleta")
async def boleta_post(data:boleta):
    try:
        set_boleta(data)
        return {"message": "Data inserted successfully"}
    except Exception as e:
        #raise HTTPException(status_code=500, detail=str(e))
        return {"message": e}


def set_boleta(data:boleta):
   

    #ingreso la boleta ...

    query = sql.SQL("INSERT INTO horas.boleta (fecha_inicio,proyecto,ubicacion,comentarios,cantidad_medida,unidad_medida,hora_inicio,hora_final,cerrada,codigo_manobra,fecha_final) VALUES( %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id")

    valores = (data.fecha_inicio,
               data.proyecto, 
               data.ubicacion, 
               data.comentarios,
               data.cantidad_medida,
               data.unidad_medida, 
               data.hora_inicio,
               data.hora_final, 
               data.cerrada,        
               data.codigo_manobra,
               data.fecha_final)
    
    conn = db_pool.getconn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, valores)
            inserted_id = cursor.fetchone()[0]
        conn.commit()
    finally:
        db_pool.putconn(conn)

    #ingreso los empleados ...

    if(data.empleados_asignados):

        for empleado in data.empleados_asignados:

                query = sql.SQL("INSERT INTO horas.empleado_boleta (id_boleta, codigo_empleado, fecha_inicio, hora_inicio) VALUES(%s, %s,%s,%s)")
                valores = (inserted_id,empleado.codigo_empleado, data.fecha_inicio, data.hora_inicio)

                conn = db_pool.getconn()
                try:
                    with conn.cursor() as cursor:
                        cursor.execute(query, valores)
                    conn.commit()
                finally:
                    db_pool.putconn(conn)




