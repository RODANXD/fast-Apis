from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schema.appointment import Appointment, AppointmentCreate, AppointmentUpdate, AppointmentOut
from app.curd import appointment as curd

router = APIRouter(prefix="/appointment-setters", tags=["Appointment Setter"])


@router.get('/', response_model=list[AppointmentOut])
def list_appointments(db: Session = Depends(get_db)):
    return curd.get_appointments(db)

@router.get('/{appointment_id}', response_model=AppointmentOut)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = curd.get_appointment(db, appointment_id)
    if appointment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
    return appointment

@router.post('/', response_model=AppointmentOut)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    try:
        return curd.create_appointment(db, appointment)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Appointment already exists")
    

@router.put('/{appointment_id}', response_model=AppointmentOut)
def update_appointment(appointment_id: int, appointment: AppointmentUpdate, db: Session = Depends(get_db)):
    updated = curd.update_appointment(db, appointment_id, appointment)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
    return updated


@router.delete('/{appointment_id}', response_model=AppointmentOut)
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_appointment(db, appointment_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appointment not found")
    return deleted

    