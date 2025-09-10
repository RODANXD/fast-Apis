from sqlalchemy.orm import Session
from app.models.users import AppointmentAgentLeads
from app.schema.appointment_agent_leads import AppointmentAgentLeadCreated, AppointmentAgentLeadsOut, AppointmentAgentLeadsBase

def get_appointment_agent_leads(db: Session):
    return db.query(AppointmentAgentLeads).all()

def get_appointment_agent_lead(db: Session, id: int):
    return db.query(AppointmentAgentLeads).filter(AppointmentAgentLeads.id == id).first()

def create_appointment_agent_lead(db: Session, appointment_agent_lead: AppointmentAgentLeadCreated):
    db_appointment_agent_lead = AppointmentAgentLeads(**appointment_agent_lead.dict())
    db.add(db_appointment_agent_lead)
    db.commit()
    db.refresh(db_appointment_agent_lead)
    return db_appointment_agent_lead

def update_appointment_agent_lead(db: Session, id: int, appointment_agent_lead: AppointmentAgentLeadsBase):
    db_appointment_agent_lead = db.query(AppointmentAgentLeads).filter(AppointmentAgentLeads.id == id).first()
    if not db_appointment_agent_lead:
        return None
    for key, value in appointment_agent_lead.dict(exclude_unset=True).items():
        setattr(db_appointment_agent_lead, key, value)
    db.commit()
    db.refresh(db_appointment_agent_lead)
    return db_appointment_agent_lead

def delete_appointment_agent_lead(db: Session, id: int):
    db_appointment_agent_lead = db.query(AppointmentAgentLeads).filter(AppointmentAgentLeads.id == id).first()
    if not db_appointment_agent_lead:
        return None
    db.delete(db_appointment_agent_lead)
    db.commit()
    return db_appointment_agent_lead
