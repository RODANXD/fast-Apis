
from sqlalchemy.orm import Session
from app.models.users import TransactionHistory
from app.schema.transaction import TransactionCreate, TransactionOut, TransactionUpdate

def get_transactions(db: Session):
    return db.query(TransactionHistory).all()

def get_transaction(db: Session, transaction_id: int):
    return db.query(TransactionHistory).filter(TransactionHistory.id == transaction_id).first()

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = TransactionHistory(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def update_transaction(db: Session, transaction_id: int, transaction):
    db_transaction = db.query(TransactionHistory).filter(TransactionHistory.id == transaction_id).first()
    if not db_transaction:
        return None
    for key, value in transaction.dict().items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(TransactionHistory).filter(TransactionHistory.id == transaction_id).first()
    if db_transaction:
        db.delete(db_transaction)
        db.commit()