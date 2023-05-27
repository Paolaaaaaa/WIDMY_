from fastapi import FastAPI, HTTPException, Request
from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import views 

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/pacientepost/")
async def crear_paciente(request: Request):
    paciente = views.create_item(get_db ,request)
        
    return paciente

@app.get("/paciente/id")
async def obtener_paciente(paciente_id: int):
    paciente = views.get_item(paciente_id)
    if paciente is None:
        raise HTTPException(status_code=404, detail="El paciente no existe")
    return paciente

# Replace 'username', 'password', 'host', 'port', and 'database_name' with your database credentials
DATABASE_URL = "postgresql://db_user:isis2503@10.182.0.15:5432/pacientes_db"
#34.125.215.124

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)