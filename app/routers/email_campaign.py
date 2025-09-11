from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.email_campaing import EmailCampaignBase, EmailCampaignCreate, EmailCampaignOut, EmailCampaignUpdate
from app.curd import email_campaing as curd


router = APIRouter(prefix="/email-campaigns", tags=["Email Campaigns"])
@router.get("/", response_model=list[EmailCampaignOut])
def get_email_campaigns(db: Session = Depends(get_db)):
    return curd.get_email_campaigns(db)

@router.get("/{email_campaign_id}", response_model=EmailCampaignOut)
def get_email_campaign(email_campaign_id: int, db: Session = Depends(get_db)):
    return curd.get_email_campaign(db, email_campaign_id)

@router.post("/", response_model=EmailCampaignOut)
def create_email_campaign(email_campaign: EmailCampaignCreate, db: Session = Depends(get_db)):
    return curd.create_email_campaign(db, email_campaign)

@router.put("/{email_campaign_id}", response_model=EmailCampaignOut)
def update_email_campaign(email_campaign_id: int, email_campaign: EmailCampaignUpdate, db: Session = Depends(get_db)):
    db_email_campaign = curd.get_email_campaign(db, email_campaign_id)
    if not db_email_campaign:
        raise HTTPException(status_code=404, detail="Email Campaign not found")
    return curd.update_email_campaign(db, email_campaign_id, email_campaign)
@router.delete("/{email_campaign_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_email_campaign(email_campaign_id: int, db: Session = Depends(get_db)):
    db_email_campaign = curd.get_email_campaign(db, email_campaign_id)
    curd.delete_email_campaign(db, email_campaign_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    