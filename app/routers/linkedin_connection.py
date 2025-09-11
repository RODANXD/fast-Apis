# from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app.schema.linkedin_connection import LinkedinConnectionOut
# from app.curd import linkedin_connection as curd

# router = APIRouter(prefix="/linkedin-connections", tags=["LinkedIn Connections"])


# @router.get('/', response_model=list[LinkedinConnectionOut])
# def list_linkedin_connections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return curd.get_all_linkedin_connections(db, skip=skip, limit=limit)
