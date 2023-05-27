from sqlalchemy.orm import Session
from . import models, schemas

def create_item(db: Session, paciente: schemas.ItemCreate):
    db_item = models.Pacientes(name=paciente.name, id=paciente.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()