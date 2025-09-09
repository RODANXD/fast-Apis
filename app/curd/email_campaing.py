from sqlalchemy.orm  import Session
from app.models.users import EmailCampaign
from app.schema.email_campaing import EmailCampaignCreate, EmailCampaignOut, EmailCampaignUpdate

def get_email_campaigns(db: Session):
    return db.query(EmailCampaign).all()

def get_email_campaign(db: Session, email_campaign_id: int):
    return db.query(EmailCampaign).filter(EmailCampaign.id == email_campaign_id).first()

def create_email_campaign(db: Session, email_campaign: EmailCampaignCreate):
    db_email_campaign = EmailCampaign(**email_campaign.dict())
    db.add(db_email_campaign)
    db.commit()
    db.refresh(db_email_campaign)
    return db_email_campaign

def update_email_campaign(db: Session, email_campaign_id: int, email_campaign: EmailCampaignUpdate):
    db_email_campaign = db.query(EmailCampaign).filter(EmailCampaign.id == email_campaign_id).first()
    for key, value in email_campaign.dict().items():
        setattr(db_email_campaign, key, value)
    db.commit()
    db.refresh(db_email_campaign)

    return db_email_campaign

def delete_email_campaign(db: Session, email_campaign_id: int):
    db_email_campaign = db.query(EmailCampaign).filter(EmailCampaign.id == email_campaign_id).first()
    db.delete(db_email_campaign)
    db.commit()
    return db_email_campaign

