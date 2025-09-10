# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.schema.x_post import XPostOut
# from app.curd import x_post as curd

# router = APIRouter(prefix="/x-posts", tags=["X Posts"])


# @router.get('/', response_model=list[XPostOut])
# def list_x_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return curd.get_all_x_posts(db, skip=skip, limit=limit)
