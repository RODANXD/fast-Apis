from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schema.account_chat_history import AccountChatHistoryOut, AccountChatHistoryCreate, AccountChatHistoryBase
from app.schema.account_chat_history import HRChatHistoryOut, HRChatHistoryBase, HRChatHistoryCreate, HRChatHistoryUpdate

from app.curd import account_chat_history as curd

router = APIRouter(prefix="/account-chat-history", tags=["Account Chat History"])


@router.get('/', response_model=list[AccountChatHistoryOut])
def list_account_chat_history(db: Session = Depends(get_db)):
    return curd.get_chat_history(db)


@router.get('/{ach_id}', response_model=AccountChatHistoryOut)
def get_account_chat_history(ach_id: int, db: Session = Depends(get_db)):
    
    account_history = curd.get_account_chat_history(db, ach_id)
    if not account_history:
        raise HTTPException(status_code=404, detail="Account chat history not found")
    return account_history

@router.post('/', response_model=AccountChatHistoryOut)
def create_account_chat_history(account_chat_history: AccountChatHistoryCreate, db: Session = Depends(get_db)):
    try:
        return curd.create_account_chat_history(db, account_chat_history)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Account chat history already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/{ach_id}', response_model=AccountChatHistoryOut)
def update_account_chat_history(ach_id: int, account_chat_history: AccountChatHistoryBase, db: Session = Depends(get_db)):
    updated = curd.update_account_chat_history(db, ach_id, account_chat_history)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account chat history not found")
    return updated

@router.delete('/{ach_id}', response_model=AccountChatHistoryOut)
def delete_account_chat_history(ach_id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_account_chat_history(db, ach_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account chat history not found")
    return deleted


@router.get('/hr/', response_model=list[HRChatHistoryOut])
def list_all_hr_chat_history(db: Session = Depends(get_db)):
    return curd.get_all_hr_chat_history(db)


@router.get('/hr/{hr_id}', response_model=list[HRChatHistoryOut])
def list_hr_chat_history(hr_id: int, db: Session = Depends(get_db)):
    return curd.get_hr_chat_history(db, hr_id)

@router.post('/hr/', response_model=HRChatHistoryOut)
def create_hr_chat_history(hr_chat_history: HRChatHistoryBase, db: Session = Depends(get_db)):
    
    try:
        return curd.create_hr_chat_history(db, hr_chat_history)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
@router.put('/hr/{hr_id}', response_model=HRChatHistoryOut)
def update_hr_chat_history(hr_id: int, hr_chat_history: HRChatHistoryUpdate, db: Session = Depends(get_db)):
    updated = curd.update_hr_chat_history(db, hr_id, hr_chat_history)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HR chat history not found")
    return updated
@router.delete('/hr/{hr_id}', response_model=HRChatHistoryOut)
def delete_hr_chat_history(hr_id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_hr_chat_history(db, hr_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HR chat history not found")
    return deleted
@router.get('/hr/{hr_id}/{chat_id}', response_model=HRChatHistoryOut)
def get_hr_chat_history_entry(hr_id: int, chat_id: int, db: Session = Depends(get_db)):
    hr_chat = curd.get_hr_chat_history_entry(db, hr_id, chat_id)
    if not hr_chat:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="HR chat history entry not found")
    return hr_chat