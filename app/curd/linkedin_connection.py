from sqlalchemy.orm import Session
from app.models.users import LinkedinConnectionDetails


def get_all_linkedin_connections(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LinkedinConnectionDetails).offset(skip).limit(limit).all()


def get_linkedin_connection(db: Session, lid: str):
    return db.query(LinkedinConnectionDetails).filter(LinkedinConnectionDetails.linkedin_id == lid).first()


def create_linkedin_connection(db: Session, data: dict):
    obj = LinkedinConnectionDetails(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
