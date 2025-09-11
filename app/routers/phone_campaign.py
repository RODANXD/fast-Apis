from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.phone_campaign import PhoneCampaignCreate, PhoneCampaignBase, PhoneCampaignOut, PhoneCampaignUpdate
from app.curd import phone_campaign as curd
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/phone-campaigns", tags=["Phone Campaigns"])

@router.get("/", response_model=list[PhoneCampaignOut])
def get_phone_campaigns(db: Session = Depends(get_db)):
    return curd.get_phone_campaigns(db)

@router.get("/{phone_campaign_id}", response_model=PhoneCampaignOut)
def get_phone_campaign(phone_campaign_id: int, db: Session = Depends(get_db)):
    return curd.get_phone_campaign(db, phone_campaign_id)


@router.post("/", response_model=PhoneCampaignOut)
def create_phone_campaign(phone_campaign: PhoneCampaignCreate, db: Session = Depends(get_db)):
    try:
        return curd.create_phone_campaign(db, phone_campaign)
    except IntegrityError as e:
        msg = str(e.orig) if hasattr(e, 'orig') and e.orig is not None else str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

@router.put("/{phone_campaign_id}", response_model=PhoneCampaignOut)
def update_phone_campaign(phone_campaign_id: int, phone_campaign: PhoneCampaignUpdate, db: Session = Depends(get_db)):
    db_phone_campaign = curd.get_phone_campaign(db, phone_campaign_id)
    if not db_phone_campaign:
        raise HTTPException(status_code=404, detail="Phone Campaign not found")
    return curd.update_phone_campaign(db, phone_campaign_id, phone_campaign)

@router.delete("/{phone_campaign_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_phone_campaign(phone_campaign_id: int, db: Session = Depends(get_db)):
    db_phone_campaign = curd.get_phone_campaign(db, phone_campaign_id)
    if not db_phone_campaign:
        raise HTTPException(status_code=404, detail="Phone Campaign not found")
    curd.delete_phone_campaign(db, phone_campaign_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)