import uvicorn


from config.db  import  * 
from models.modelos import tb_presupuesto

def run():
    pass

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    run()



if __name__ == "__main__":
    uvicorn.run("app.api:app", host="localhost", port=8080, reload=True)
    # uvicorn.run("app.api:app", host="0.0.0.0", port=5000, reload=True)