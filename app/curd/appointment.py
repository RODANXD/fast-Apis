from sqlalchemy.orm import Session
from app.models.users import AppointmentSetter
from app.schema.appointment import Appointment, AppointmentCreate, AppointmentUpdate, AppointmentOut
from uuid import uuid4


def get_appointments(db: Session):
    return db.query(AppointmentSetter).all()

def get_appointment(db: Session, id: int):
    return db.query(AppointmentSetter).filter(AppointmentSetter.id == id).first()

def create_appointment(db: Session, appointment: AppointmentCreate):
    # use only provided fields and ensure platform_unique_id exists
    data = appointment.dict(exclude_unset=True)
    if not data.get('platform_unique_id'):
        data['platform_unique_id'] = str(uuid4())
    db_appointment = AppointmentSetter(**data)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def update_appointment(db: Session, id: int, appointment: AppointmentUpdate):
    db_appointment = db.query(AppointmentSetter).filter(AppointmentSetter.id == id).first()
    if not db_appointment:
        return None
    for key, value in appointment.dict(exclude_unset=True).items():
        setattr(db_appointment, key, value)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def delete_appointment(db: Session, id: int):
    db_appointment = db.query(AppointmentSetter).filter(AppointmentSetter.id == id).first()
    if not db_appointment:
        return None
    db.delete(db_appointment)
    db.commit()
    return db_appointment

def get_appointment_by_user_id(db: Session, user_id: int):
    return db.query(AppointmentSetter).filter(AppointmentSetter.user_id == user_id).all()
