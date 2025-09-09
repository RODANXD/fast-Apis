from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.users import WhatsAppConnection
from typing import List, Optional
from app.schema.whatsapp_connection import WhatsAppConnectionCreate, WhatsAppConnectionUpdate


def get_all_whatsapp_connections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(WhatsAppConnection).offset(skip).limit(limit).all()


def _find_whatsapp_connection(db: Session, wc_id: str):
    """Try to find a WhatsAppConnection by business id or, if numeric, by user_id."""
    # first try business id
    obj = db.query(WhatsAppConnection).filter(WhatsAppConnection.whatsapp_business_id == wc_id).first()
    if obj:
        return obj
    # if wc_id looks like an integer, try user_id lookup
    if wc_id.isdigit():
        obj = db.query(WhatsAppConnection).filter(WhatsAppConnection.user_id == int(wc_id)).first()
        if obj:
            return obj
    return None


def get_whatsapp_connection(db: Session, wc_id: str):
    return _find_whatsapp_connection(db, wc_id)


def create_whatsapp_connection(db: Session, wc_data: dict):
    # ensure required business id and access_token provided
    if not wc_data.get('whatsapp_business_id'):
        raise HTTPException(status_code=400, detail='whatsapp_business_id is required')
    if not wc_data.get('access_token'):
        raise HTTPException(status_code=400, detail='access_token is required')
    obj = WhatsAppConnection(**wc_data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_whatsapp_connection(db: Session, wc_id: str, wc_data: dict):
    obj = _find_whatsapp_connection(db, wc_id)
    if not obj:
        raise HTTPException(status_code=404, detail="WhatsApp connection not found")
    for k, v in wc_data.items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj


def delete_whatsapp_connection(db: Session, wc_id: str):
    obj = _find_whatsapp_connection(db, wc_id)
    if not obj:
        raise HTTPException(status_code=404, detail="WhatsApp connection not found")
    db.delete(obj)
    db.commit()
    return True
