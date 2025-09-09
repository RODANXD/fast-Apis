from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.whatsapp_connection import WhatsAppConnectionCreate, WhatsAppConnectionOut, WhatsAppConnectionUpdate
from app.curd import whatsapp_connection as curd

router = APIRouter(prefix="/whatsapp-connections", tags=["WhatsApp Connections"])


@router.get('/', response_model=list[WhatsAppConnectionOut])
def list_whatsapp_connections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return curd.get_all_whatsapp_connections(db, skip=skip, limit=limit)


@router.get('/{wc_id}', response_model=WhatsAppConnectionOut)
def get_whatsapp_connection(wc_id: str, db: Session = Depends(get_db)):
    wc = curd.get_whatsapp_connection(db, wc_id)
    if wc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="WhatsApp connection not found")
    return wc


@router.post('/', response_model=WhatsAppConnectionOut)
def create_whatsapp_connection(wc_in: WhatsAppConnectionCreate, db: Session = Depends(get_db)):
    return curd.create_whatsapp_connection(db, wc_in.dict())


@router.put('/{wc_id}', response_model=WhatsAppConnectionOut)
def update_whatsapp_connection(wc_id: str, wc_in: WhatsAppConnectionUpdate, db: Session = Depends(get_db)):
    updated = curd.update_whatsapp_connection(db, wc_id, wc_in.dict(exclude_unset=True))
    return updated


@router.delete('/{wc_id}')
def delete_whatsapp_connection(wc_id: str, db: Session = Depends(get_db)):
    deleted = curd.delete_whatsapp_connection(db, wc_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="WhatsApp connection not found")
    return {"deleted": True}
