from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.x_post import XPostOut
from app.curd import xpost as curd

router = APIRouter(prefix="/xposts", tags=["X Posts"])


@router.get('/', response_model=list[XPostOut])
def list_x_posts(db: Session = Depends(get_db)):
    return curd.get_xposts(db)

@router.get('/{x_post_id}', response_model=XPostOut)
def get_x_post(x_post_id: int, db: Session = Depends(get_db)):
    return curd.get_xpost(db, x_post_id)

@router.post('/', response_model=XPostOut)
def create_x_post(x_post: XPostOut, db: Session = Depends(get_db)):
    return curd.create_xpost(db, x_post)

@router.put('/{x_post_id}', response_model=XPostOut)
def update_x_post(x_post_id: int, x_post: XPostOut, db: Session = Depends(get_db)):
    return curd.update_xpost(db, x_post_id, x_post)

@router.delete('/{x_post_id}')
def delete_x_post(x_post_id: int, db: Session = Depends(get_db)):
    xpost = curd.delete_xpost(db, x_post_id)
    if not xpost:
        raise HTTPException(status_code=404, detail="X Post not found")
    curd.delete_x_post(db, x_post_id)
    return {"id": x_post_id, "detail": "X Post deleted"}