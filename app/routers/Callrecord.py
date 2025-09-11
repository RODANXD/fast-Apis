from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schema.Callrecord import CallrecordBase, CallrecordCreate,CallrecordOut, DeleteResponse
from app.curd import Callrecord as curd

router = APIRouter(prefix="/call-record", tags=["Call Record"])


@router.get("/", response_model=list[CallrecordOut])
def get_all_call_record(db: Session = Depends(get_db)):
    return curd.get_call_records(db)


@router.get("/{id}", response_model=CallrecordOut)
def get_call_record(id: int, db: Session = Depends(get_db)):
    call_record = curd.get_call_record(db, id)
    if not call_record:
        raise HTTPException(status_code=404, detail="Call record not found")
    return call_record
@router.post("/", response_model=CallrecordOut)
def create_call_record(call_record: CallrecordCreate, db: Session = Depends(get_db)):
    try:
        return curd.create_call_record(db, call_record)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Call record already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@router.put("/{id}", response_model=CallrecordOut)
def update_call_record(id: int, call_record: CallrecordBase, db: Session = Depends(get_db)):
    updated = curd.update_call_record(db, id, call_record)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Call record not found")
    return updated


@router.delete("/{id}", response_model=DeleteResponse)
def delete_call_record(id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_call_record(db, id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Call record not found")
    return deleted


@router.get("/search-call-record/", response_model=list[CallrecordOut])
def search_call_record(query: str, db: Session = Depends(get_db)):
    results = curd.search_call_records(db, query)
    if not results:
        raise HTTPException(status_code=404, detail="No call records found matching the query")
    return results