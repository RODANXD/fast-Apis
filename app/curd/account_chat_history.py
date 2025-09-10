from sqlalchemy.orm import Session
from app.models.users import AccountChatHistory
from app.models.users import HRChatHistory
from app.schema.account_chat_history import AccountChatHistoryCreate, AccountChatHistoryOut
from app.schema.account_chat_history import HRChatHistoryBase, HRChatHistoryCreate, HRChatHistoryOut

def get_chat_history(db:Session):
    return db.query(AccountChatHistory).all()

def get_account_chat_history(db: Session, ach_id: int):
    return db.query(AccountChatHistory).filter(AccountChatHistory.id == ach_id).first()

def create_account_chat_history(db: Session, ach: AccountChatHistoryCreate):
    # create a SQLAlchemy model instance from the Pydantic schema
    db_ach = AccountChatHistory(**ach.dict(exclude_unset=True))
    db.add(db_ach)
    db.commit()
    db.refresh(db_ach)
    return db_ach

def update_account_chat_history(db: Session, ach_id: int, ach: AccountChatHistoryOut):
    db_ach = get_account_chat_history(db, ach_id)
    if not db_ach:
        return None
    for key, value in ach.dict(exclude_unset=True).items():
        setattr(db_ach, key, value)
    db.commit()
    db.refresh(db_ach)
    return db_ach

def delete_account_chat_history(db: Session, ach_id: int):
    db_ach = get_account_chat_history(db, ach_id)
    if db_ach:
        # capture column values to return after deletion (so response_model validation passes)
        result = {c.name: getattr(db_ach, c.name) for c in AccountChatHistory.__table__.columns}
        db.delete(db_ach)
        db.commit()
        return result
    return None

def delete_all_account_chat_history(db: Session):
    db.query(AccountChatHistory).delete()
    db.commit()





def create_hr_chat_history(db: Session, hr_chat: HRChatHistoryCreate):
    db_hr_chat = HRChatHistory(**hr_chat.dict(exclude_unset=True))
    db.add(db_hr_chat)
    db.commit()
    db.refresh(db_hr_chat)
    return db_hr_chat

def get_hr_chat_history(db: Session, user_id: int):
    # return all HR chat history rows for the given user_id
    return db.query(HRChatHistory).filter(HRChatHistory.user_id == user_id).all()

def delete_hr_chat_history(db: Session, user_id: int):
    # delete all HR chat history rows for the given user_id
    db.query(HRChatHistory).filter(HRChatHistory.user_id == user_id).delete()
    db.commit()
def delete_all_hr_chat_history(db: Session):
    db.query(HRChatHistory).delete()
    db.commit()
def update_hr_chat_history(db: Session, ach_id: int, hr_chat: HRChatHistoryOut):
    # find the HR chat history row by its primary id
    db_hr_chat = get_hr_chat_history_by_id(db, ach_id)
    if not db_hr_chat:
        return None
    for key, value in hr_chat.dict(exclude_unset=True).items():
        setattr(db_hr_chat, key, value)
    db.commit()
    db.refresh(db_hr_chat)
    return db_hr_chat

def get_all_hr_chat_history(db: Session):
    return db.query(HRChatHistory).all()
def get_hr_chat_history_by_id(db: Session, ach_id: int):
    return db.query(HRChatHistory).filter(HRChatHistory.id == ach_id).first()