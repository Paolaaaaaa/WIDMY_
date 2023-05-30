from sqlalchemy.orm import Session
from models import Paciente
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

def create_item(engine, paciente):
    session = Session(bind=engine)
    db_item = Paciente(name=paciente["name"], id=paciente["id"])
    session.add(db_item)
    session.commit()
    session.close()
    return "paciente creado correctamente"



def get_item(engine, item_id: int):
    session = Session(bind=engine)
    pacientes = session.query(Paciente).filter(Paciente.id==item_id)
    session.close()
    return pacientes

def get_Items(engine):
    session = Session(bind=engine)
    pacientes = session.query(Paciente).all()
    session.close()
    return pacientes