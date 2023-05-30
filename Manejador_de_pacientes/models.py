from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    


def start_db(engine):
    print ("Tabla generando paciente")

    Base.metadata.create_all(engine)


