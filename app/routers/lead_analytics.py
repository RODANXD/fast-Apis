from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.lead_analytics import LeadAnalyticsCreate,LeadAnalyticsBase,LeadAnalyticsOut,LeadAnalyticsUpdate
from app.curd import lead_analytics as curd

router = APIRouter(prefix="/lead-analytics", tags=["Lead Analytics"])

@router.get('/', response_model=list[LeadAnalyticsOut])
def list_lead_analytics(db: Session = Depends(get_db)):
    return curd.get_lead_analytics(db)

@router.get('/{lead_analytics_id}', response_model=LeadAnalyticsOut)
def get_lead_analytics(lead_analytics_id: int, db: Session = Depends(get_db)):
    lead_analytics = curd.get_lead_analytics(db, lead_analytics_id)
    if lead_analytics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead Analytics not found")
    return lead_analytics


@router.post('/', response_model=LeadAnalyticsOut, status_code=status.HTTP_201_CREATED)
def create_lead_analytics(lead_analytics: LeadAnalyticsCreate, db: Session = Depends(get_db)):
    return curd.create_lead_analytics(db, lead_analytics)


@router.put('/{lead_analytics_id}', response_model=LeadAnalyticsOut)
def update_lead_analytics(lead_analytics_id: int, lead_analytics: LeadAnalyticsUpdate, db: Session = Depends(get_db)):
    lead_analytics = curd.update_lead_analytics(db, lead_analytics_id, lead_analytics)
    if lead_analytics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead Analytics not found")
    return lead_analytics


@router.delete('/{lead_analytics_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lead_analytics(lead_analytics_id: int, db: Session = Depends(get_db)):
    lead_analytics = curd.delete_lead_analytics(db, lead_analytics_id)
    if lead_analytics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead Analytics not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

