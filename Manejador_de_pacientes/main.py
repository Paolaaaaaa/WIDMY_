from fastapi import FastAPI, HTTPException, Request
from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import views 
from models import Paciente
from typing import Dict

app = FastAPI()
DATABASE_URL ='postgresql://etl:password@localhost:5432/'+'Bi_ETL'

engine = create_engine(DATABASE_URL)

def get_db():
    return create_engine(DATABASE_URL)

@app.post("/pacientes/")
async def crear_paciente(paciente: Dict[str, str]):
   
    paciente = views.create_item(get_db() ,paciente)
        
    return paciente

@app.get("/pacientes/list")
async def get_pacientes():
    paciente = views.get_Items(get_db() )
    return paciente


@app.get("/paciente/id")
async def obtener_paciente(paciente_id: int):
    paciente = views.get_item(paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="El paciente no existe")
    return paciente

# Replace 'username', 'password', 'host', 'port', and 'database_name' with your database credentials
#DATABASE_URL = "postgresql://db_user:isis2503@localhost:5432/pacientes_db"

#34.125.215.124

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def create_gine ():
    try:
        engine=create_engine(DATABASE_URL)
        with engine.connect() as connection:
                print("¡Conexión exitosa!")
                
    except Exception as e:
        print("Data load error: " + str(e))


    return engine
