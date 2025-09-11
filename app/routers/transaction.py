from app.schema.transaction import TransactionUpdate
from app.curd.transaction import update_transaction, delete_transaction
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.transaction import TransactionCreate, TransactionOut, TransactionUpdate
from app.curd import transaction as curd

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get('/', response_model=list[TransactionOut])
def get_transactions(db: Session = Depends(get_db)):
    return curd.get_transactions(db)


@router.get('/{transaction_id}', response_model=TransactionOut)

def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = curd.get_transaction(db, transaction_id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@router.post('/', response_model=TransactionOut)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return curd.create_transaction(db, transaction)

@router.put('/{transaction_id}', response_model=TransactionOut)
def update_transaction_api(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = curd.get_transaction(db, transaction_id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return update_transaction(db, transaction_id, transaction)

@router.delete('/{transaction_id}')
def delete_transaction_api(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = curd.get_transaction(db, transaction_id)
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    delete_transaction(db, transaction_id)
    return {"detail": "Transaction deleted"}