from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

from app.schema.linkdin_post import LinkedInPostCreate, LinkedInPostOut, LinkedInPostUpdate
from app.curd import linkdin_post as curd


router = APIRouter(prefix="/linkedin-posts", tags=["LinkedIn Posts"])

@router.get("/", response_model=list[LinkedInPostOut])
def list_posts(db: Session = Depends(get_db)):
    return curd.get_linkedin_posts(db)

@router.get("/{post_id}", response_model=LinkedInPostOut)
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = curd.get_linkedin_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=LinkedInPostOut)
def update_post(post_id: int, post: LinkedInPostUpdate, db: Session = Depends(get_db)):
    linkdinpost = curd.update_linkedin_post(db, post_id, post)
    if linkdinpost is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return linkdinpost

@router.post("/", response_model=LinkedInPostOut)
def create_post(post: LinkedInPostCreate, db: Session = Depends(get_db)):
    return curd.create_linkedin_post(db, post)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = curd.delete_linkedin_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    curd.delete_linkedin_post(db, post_id)
    return {"detail": "Post deleted"}