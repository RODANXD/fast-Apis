from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.users import XPost
from app.schema.x_post import XPostCreate, XPostUpdate, XpostBase, XPostOut
from typing import List


def get_xposts(db: Session) -> List[XPost]:
    return db.query(XPost).all()

def get_xpost(db: Session, xpost_id: int) -> XPost:
    return db.query(XPost).filter(XPost.id == xpost_id).first()

def create_xpost(db: Session, xpost: XPostCreate) -> XPost:
    db_xpost = XPost(**xpost.dict())
    db.add(db_xpost)
    db.commit()
    db.refresh(db_xpost)
    return db_xpost

def update_xpost(db: Session, xpost_id: int, xpost: XPostUpdate) -> XPost:
    db_xpost = db.query(XPost).filter(XPost.id == xpost_id).first()
    if not db_xpost:
        raise HTTPException(status_code=404, detail="Xpost not found")
    for key, value in xpost.dict().items():
        setattr(db_xpost, key, value)
    db.commit()
    db.refresh(db_xpost)
    return db_xpost

def delete_xpost(db: Session, xpost_id: int) -> XPost:
    db_xpost = db.query(XPost).filter(XPost.id == xpost_id).first()
    if not db_xpost:
        raise HTTPException(status_code=404, detail="Xpost not found")
    db.delete(db_xpost)
    db.commit()
    return db_xpost

