from sqlalchemy.orm import Session
from app.models.users import Content
from app.models.users import ContentCreationChatHistory
from app.schema.content import ContentCreate, ContentOut, ContentBase, ContentDetailOut
from app.schema.content import ContentCreationChatHistoryBase, ContentCreationChatHistoryOut, ContentCreationChatHistoryUpdate, ContentCreationChatHistoryCreate

def get_contents(db: Session):
    return db.query(Content).all()
def get_content(db: Session, content_id: int):
    return db.query(Content).filter(Content.id == content_id).first()
def create_content(db: Session, content: ContentCreate):
    db_content = Content(**content.dict())
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content
def update_content(db: Session, content: ContentBase, content_id: int):
    db_content = db.query(Content).filter(Content.id == content_id).first()
    if db_content:
        for key, value in content.dict().items():
            setattr(db_content, key, value)
        db.commit()
        db.refresh(db_content)
        return db_content
    return None
def delete_content(db: Session, content_id: int):
    db_content = db.query(Content).filter(Content.id == content_id).first()
    if db_content:
        db.delete(db_content)
        db.commit()
        return True
    return False
def get_content_detail(db: Session, content_id: int):
    return db.query(Content).filter(Content.id == content_id).first()







def get_content_creation_chat_histories(db: Session):
    return db.query(ContentCreationChatHistory).all()

def get_content_creation_chat_history(db: Session, chat_history_id: int):
    return db.query(ContentCreationChatHistory).filter(ContentCreationChatHistory.id == chat_history_id).first()
def create_content_creation_chat_history(db: Session, chat_history: ContentCreationChatHistoryCreate):
    # avoid duplicate thread_id inserts: if a record exists, merge/append chat_history and update
    thread_id = getattr(chat_history, "thread_id", None)
    if thread_id:
        existing = db.query(ContentCreationChatHistory).filter(ContentCreationChatHistory.thread_id == thread_id).first()
        if existing:
            incoming = getattr(chat_history, "chat_history", None) or []
            # merge arrays
            existing.chat_history = (existing.chat_history or []) + incoming
            # update optional fields if provided
            if getattr(chat_history, "name", None):
                existing.name = chat_history.name
            if getattr(chat_history, "updated_at", None):
                existing.updated_at = chat_history.updated_at
            db.commit()
            db.refresh(existing)
            return existing

    db_chat_history = ContentCreationChatHistory(**chat_history.dict())
    db.add(db_chat_history)
    db.commit()
    db.refresh(db_chat_history)
    return db_chat_history
def update_content_creation_chat_history(db: Session, chat_history_id: int, chat_history: ContentCreationChatHistoryUpdate):
    db_chat_history = db.query(ContentCreationChatHistory).filter(ContentCreationChatHistory.id == chat_history_id).first()
    if db_chat_history:
        for key, value in chat_history.dict(exclude_unset=True).items():
            setattr(db_chat_history, key, value)
        db.commit()
        db.refresh(db_chat_history)
        return db_chat_history
    return None
def delete_content_creation_chat_history(db: Session, chat_history_id: int):
    db_chat_history = db.query(ContentCreationChatHistory).filter(ContentCreationChatHistory.id == chat_history_id).first()
    if db_chat_history:
        db.delete(db_chat_history)
        db.commit()
        return True
    return False


