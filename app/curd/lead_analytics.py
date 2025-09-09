from sqlalchemy.orm import Session
from app.models.users import Lead_Analytics, AppointmentSetter
from app.schema.lead_analytics import LeadAnalyticsCreate, LeadAnalyticsUpdate, LeadAnalyticsBase, LeadAnalyticsOut

def get_lead_analytics(db: Session):
    return db.query(Lead_Analytics).all()

def get_lead_analytics_by_id(db: Session, lead_analytics_id: int):
    return db.query(Lead_Analytics).filter(Lead_Analytics.id == lead_analytics_id).first()

def create_lead_analytics(db: Session, lead_analytics: LeadAnalyticsCreate):
    data = lead_analytics.dict(exclude_unset=True)
    agent_id = data.get('agent_id')
    if agent_id:
        agent = db.query(AppointmentSetter).filter(AppointmentSetter.id == agent_id).first()
        if not agent:
            from sqlalchemy.exc import IntegrityError
            raise IntegrityError(statement=None, params=None, orig=Exception(f"agent id {agent_id} does not exist"))
    db_lead_analytics = Lead_Analytics(**data)
    db.add(db_lead_analytics)
    db.commit()
    db.refresh(db_lead_analytics)
    return db_lead_analytics

def update_lead_analytics(db: Session, lead_analytics_id: int, lead_analytics: LeadAnalyticsUpdate):
    db_lead_analytics = db.query(Lead_Analytics).filter(Lead_Analytics.id == lead_analytics_id).first()
    if db_lead_analytics:
        data = lead_analytics.dict(exclude_unset=True)
        agent_id = data.get('agent_id')
        if agent_id:
            agent = db.query(AppointmentSetter).filter(AppointmentSetter.id == agent_id).first()
            if not agent:
                from sqlalchemy.exc import IntegrityError
                raise IntegrityError(statement=None, params=None, orig=Exception(f"agent id {agent_id} does not exist"))
        for key, value in data.items():
            setattr(db_lead_analytics, key, value)
        db.commit()
        db.refresh(db_lead_analytics)
        return db_lead_analytics
    else:
        return None

def delete_lead_analytics(db: Session, lead_analytics_id: int):
    db_lead_analytics = db.query(Lead_Analytics).filter(Lead_Analytics.id == lead_analytics_id).first()
    if db_lead_analytics:
        db.delete(db_lead_analytics)
        db.commit()
        return True
    return False
def get_lead_analytics_by_user(db: Session, user_id: int):
    return db.query(Lead_Analytics).filter(Lead_Analytics.userId == user_id).all()
