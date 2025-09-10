from sqlalchemy.orm import Session
from app.models.users import PasswordResetTokens


def get_all_password_resets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PasswordResetTokens).offset(skip).limit(limit).all()


def get_password_reset(db: Session, pr_id: int):
    return db.query(PasswordResetTokens).filter(PasswordResetTokens.id == pr_id).first()


def create_password_reset(db: Session, data: dict):
    obj = PasswordResetTokens(**data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
