from fastapi import FastAPI, HTTPException, Request
from typing import Union

app = FastAPI()

app.data = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/pacientes/")
async def crear_paciente(request: Request):
    paciente = await request.json()
    paciente_id = paciente.get("id")
    paciente_nombre = paciente.get("nombre")
    # Aquí puedes procesar los datos recibidos y almacenarlos en una base de datos, por ejemplo.
    # Asegúrate de validar los datos y realizar las operaciones necesarias.
    # ...
    return {"message": f"Paciente creado: ID: {paciente_id}, Nombre: {paciente_nombre}"}

