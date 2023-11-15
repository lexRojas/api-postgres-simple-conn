from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

#---IMPORTACION DE RUTAS 

from routes.route_presupuesto import route_presupuesto
from routes.route_sectores import route_sectores
from routes.route_elementos import route_elementos
from routes.route_empleados import route_empleado
from routes.route_reset import route_reset
from routes.route_actividades import route_actividades


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