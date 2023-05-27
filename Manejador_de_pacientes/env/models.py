from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    _tablename_ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    
