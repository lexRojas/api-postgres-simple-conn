from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#---IMPORTACION DE RUTAS 

from routes.route_presupuesto import route_presupuesto
from routes.route_sectores import route_sectores
from routes.route_elementos import route_elementos
from routes.route_empleados import route_empleado
from routes.route_reset import route_reset
from routes.route_actividades import route_actividades
from routes.route_elem_detail import route_elem_detail
from routes.route_vista_actividades import route_vista_actividades
from routes.route_boleta import route_boleta
from routes.route_boleta_detail import route_boleta_detail

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"mensaje":'hola a todos'}

app.include_router(route_reset)
app.include_router(route_presupuesto)
app.include_router(route_sectores)
app.include_router(route_elementos)
app.include_router(route_empleado)
app.include_router(route_actividades)
app.include_router(route_vista_actividades)
app.include_router(route_elem_detail)
app.include_router(route_boleta)
app.include_router(route_boleta_detail)