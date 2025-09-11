from sqlalchemy.orm import Session

from app.models.users import ScheduledContent
from app.schema.scheduled_content import ScheduledContentCreate, ScheduledContentUpdate
from app.models.users import User as _User
from fastapi import HTTPException


def get_all_scheduled_contents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ScheduledContent).offset(skip).limit(limit).all()

def get_scheduled_contents(db: Session):
    return db.query(ScheduledContent).all()


def get_scheduled_content(db: Session, sc_id: int):
    return db.query(ScheduledContent).filter(ScheduledContent.id == sc_id).first()


def create_scheduled_content(db: Session, sc_data):
    obj = ScheduledContent(**sc_data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_scheduled_content(db: Session, sc_id: int, sc_data: dict):
    obj = db.query(ScheduledContent).filter(ScheduledContent.id == sc_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="ScheduledContent not found")
    for k, v in sc_data.items():
        setattr(obj, k, v)
    db.commit()
    db.refresh(obj)
    return obj


def delete_scheduled_content(db: Session, sc_id: int):
    obj = db.query(ScheduledContent).filter(ScheduledContent.id == sc_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="ScheduledContent not found")
    db.delete(obj)
    db.commit()
    return True
