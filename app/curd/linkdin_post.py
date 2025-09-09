from sqlalchemy.orm import Session
from app.models.users import LinkedInPost
from app.schema.linkdin_post import LinkedInPostCreate, LinkedInPostOut, LinkedInPostUpdate


def get_linkedin_posts(db: Session):
    return db.query(LinkedInPost).all()

def get_linkedin_post(db: Session, linkedin_post_id: int):
    return db.query(LinkedInPost).filter(LinkedInPost.id == linkedin_post_id).first()

def create_linkedin_post(db: Session, linkedin_post: LinkedInPostCreate):
    db_linkedin_post = LinkedInPost(**linkedin_post.dict())
    db.add(db_linkedin_post)
    db.commit()
    db.refresh(db_linkedin_post)
    return db_linkedin_post

def update_linkedin_post(db: Session, linkedin_post_id: int, linkedin_post: LinkedInPostUpdate):
    db_linkedin_post = db.query(LinkedInPost).filter(LinkedInPost.id == linkedin_post_id).first()
    if not db_linkedin_post:
        return None
    for key, value in linkedin_post.dict(exclude_unset=True).items():
        setattr(db_linkedin_post, key, value)
    db.commit()
    db.refresh(db_linkedin_post)
    return db_linkedin_post

def delete_linkedin_post(db: Session, linkedin_post_id: int):
    db_linkedin_post = db.query(LinkedInPost).filter(LinkedInPost.id == linkedin_post_id).first()
    if not db_linkedin_post:
        return None
    db.delete(db_linkedin_post)
    db.commit()
    return db_linkedin_post
