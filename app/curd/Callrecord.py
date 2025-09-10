from sqlalchemy.orm import Session
from app.models.users import CallRecord
from app.schema.Callrecord import CallrecordBase, CallrecordCreate, CallrecordOut

def get_call_records(db: Session):
    return db.query(CallRecord).all()

def get_call_record(db: Session, id: int):
    return db.query(CallRecord).filter(CallRecord.id == id).first()

def create_call_record(db: Session, call_record: CallrecordCreate):
    db_call_record = CallRecord(**call_record.dict())
    db.add(db_call_record)
    db.commit()
    db.refresh(db_call_record)
    return db_call_record

def update_call_record(db: Session, id: int, call_record: CallrecordBase):
    db_call_record = db.query(CallRecord).filter(CallRecord.id == id).first()
    if not db_call_record:
        return None
    for key, value in call_record.dict(exclude_unset=True).items():
        setattr(db_call_record, key, value)
    db.commit()
    db.refresh(db_call_record)
    return db_call_record

def delete_call_record(db: Session, id: int):
    db_call_record = db.query(CallRecord).filter(CallRecord.id == id).first()
    if not db_call_record:
        return None
    db.delete(db_call_record)
    db.commit()
    return {"id": id, "detail": "deleted successfully"}

def search_call_records(db: Session, from_contact_number: str = None, contact_number: str = None, result: str = None):
    query = db.query(CallRecord)
    if from_contact_number:
        query = query.filter(CallRecord.from_contact_number == from_contact_number)
    if contact_number:
        query = query.filter(CallRecord.contact_number == contact_number)
    if result:
        query = query.filter(CallRecord.result == result)
    return query.all()
