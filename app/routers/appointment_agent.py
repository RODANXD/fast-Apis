from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.appointment_agent_leads import AppointmentAgentLeadsOut, AppointmentAgentLeadCreated
from app.curd import appointment_agent as curd

router = APIRouter(prefix="/appointment-agent-leads", tags=["Appointment Agent Leads"])


@router.get("/", response_model=list[AppointmentAgentLeadsOut])
def get_appointment_agent_leads(db: Session = Depends(get_db)):
    return curd.get_appointment_agent_leads(db)


@router.post("/", response_model=AppointmentAgentLeadCreated)
def create_appointment_agent_lead(appointment_agent_lead: AppointmentAgentLeadCreated, db: Session = Depends(get_db)):
    return curd.create_appointment_agent_lead(db, appointment_agent_lead)

@router.put("/{lead_id}", response_model=AppointmentAgentLeadsOut)
def update_appointment_agent_lead(lead_id: int, appointment_agent_lead: AppointmentAgentLeadCreated, db: Session = Depends(get_db)):
    updated = curd.update_appointment_agent_lead(db, lead_id, appointment_agent_lead)
    if not updated:
        raise HTTPException(status_code=404, detail="Appointment agent lead not found")
    return updated

@router.delete("/{lead_id}")
def delete_appointment_agent_lead(lead_id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_appointment_agent_lead(db, lead_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Appointment agent lead not found")
    return {"detail": "Appointment agent lead deleted"}

