from sqlalchemy.orm import Session
from app.models.users import PhoneCampaign, PhoneAgent
from app.schema.phone_campaign import PhoneCampaignBase, PhoneCampaignCreate, PhoneCampaignOut, PhoneCampaignUpdate
from sqlalchemy.exc import IntegrityError

def get_phone_campaigns(db: Session):
    return db.query(PhoneCampaign).all()

def get_phone_campaign(db: Session, phone_campaign_id: int):
    return db.query(PhoneCampaign).filter(PhoneCampaign.id == phone_campaign_id).first()
def create_phone_campaign(db: Session, phone_campaign: PhoneCampaignCreate):
    data = phone_campaign.dict(exclude_unset=True)
    agent_id = data.get('agent')
    if agent_id is not None:
        agent = db.query(PhoneAgent).filter(PhoneAgent.id == agent_id).first()
        if not agent:
            raise IntegrityError(statement=None, params=None, orig=Exception(f"agent id {agent_id} does not exist"))
    db_phone_campaign = PhoneCampaign(**data)
    db.add(db_phone_campaign)
    db.commit()
    db.refresh(db_phone_campaign)
    return db_phone_campaign

def update_phone_campaign(db: Session, phone_campaign_id: int, phone_campaign_update: PhoneCampaignUpdate):
    db_phone_campaign = db.query(PhoneCampaign).filter(PhoneCampaign.id == phone_campaign_id).first()
    for key, value in phone_campaign_update.dict(exclude_unset=True).items():
        setattr(db_phone_campaign, key, value)
    db.commit()
    db.refresh(db_phone_campaign)
    return db_phone_campaign

def delete_phone_campaign(db: Session, phone_campaign_id: int):
    db_phone_campaign = db.query(PhoneCampaign).filter(PhoneCampaign.id == phone_campaign_id).first()
    db.delete(db_phone_campaign)
    db.commit()
    return db_phone_campaign

def get_phone_campaign_by_name(db: Session, name: str):
    return db.query(PhoneCampaign).filter(PhoneCampaign.name == name).first()