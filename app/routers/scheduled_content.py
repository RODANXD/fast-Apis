from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.scheduled_content import ScheduledContentCreate, ScheduledContentOut, ScheduledContentUpdate
from app.curd import scheduled_content as curd

router = APIRouter(prefix="/scheduled-content", tags=["Scheduled Content"])


@router.get('/', response_model=list[ScheduledContentOut])
def list_scheduled_contents(db: Session = Depends(get_db)):
    return curd.get_scheduled_contents(db)


@router.get('/{sc_id}', response_model=ScheduledContentOut)
def get_scheduled_content(sc_id: int, db: Session = Depends(get_db)):
    sc = curd.get_scheduled_content(db, sc_id)
    if sc is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scheduled content not found")
    return sc


@router.post('/', response_model=ScheduledContentOut)
def create_scheduled_content(sc_in: ScheduledContentCreate, db: Session = Depends(get_db)):
    return curd.create_scheduled_content(db, sc_in.dict())


@router.put('/{sc_id}', response_model=ScheduledContentOut)
def update_scheduled_content(sc_id: int, sc_in: ScheduledContentUpdate, db: Session = Depends(get_db)):
    updated = curd.update_scheduled_content(db, sc_id, sc_in.dict(exclude_unset=True))
    return updated


@router.delete('/{sc_id}')
def delete_scheduled_content(sc_id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_scheduled_content(db, sc_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Scheduled content not found")
    return {"deleted": True}
