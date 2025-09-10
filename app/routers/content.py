from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.content import ContentCreate, ContentOut, ContentBase, ContentDetailOut
from app.schema.content import ContentCreationChatHistoryBase, ContentCreationChatHistoryOut, ContentCreationChatHistoryUpdate, ContentCreationChatHistoryCreate
from app.curd import content as curd

router = APIRouter(prefix="/contents", tags=["Contents"])

@router.get('/', response_model=list[ContentOut])
def list_contents(db: Session = Depends(get_db)):
    return curd.get_contents(db)

@router.get('/{content_id}', response_model=ContentDetailOut)
def read_content(content_id: int, db: Session = Depends(get_db)):
    content = curd.get_content(db, content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.post('/', response_model=ContentOut)
def create_content(content: ContentCreate, db: Session = Depends(get_db)):
    return curd.create_content(db, content)


@router.put('/{content_id}', response_model=ContentOut)
def update_content_api(content_id: int, content: ContentCreate, db: Session = Depends(get_db)):
    db_content = curd.get_content(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    return curd.update_content(db, content, content_id)
@router.delete('/{content_id}')
def delete_content_api(content_id: int, db: Session = Depends(get_db)):
    db_content = curd.get_content(db, content_id)
    if not db_content:
        raise HTTPException(status_code=404, detail="Content not found")
    curd.delete_content(db, content_id)
    return {"detail": "Content deleted"}







@router.get('/chat-histories/', response_model=list[ContentCreationChatHistoryOut])
def list_content_creation_chat_histories(db: Session = Depends(get_db)):
    return curd.get_content_creation_chat_histories(db)
@router.get('/chat-histories/{chat_history_id}', response_model=ContentCreationChatHistoryOut)
def read_content_creation_chat_history(chat_history_id: int, db: Session = Depends(get_db
)):
    chat_history = curd.get_content_creation_chat_history(db, chat_history_id)
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return chat_history
@router.post('/chat-histories/')
def create_content_creation_chat_history_api(content_creation_chat_history: ContentCreationChatHistoryCreate, db: Session = Depends(get_db)):
    return curd.create_content_creation_chat_history(db, content_creation_chat_history)



@router.put('/chat-histories/{chat_history_id}', response_model=ContentCreationChatHistoryOut)
def update_content_creation_chat_history_api(chat_history_id: int, content_creation_chat_history: ContentCreationChatHistoryUpdate, db: Session = Depends(get_db)):
    db_chat_history = curd.get_content_creation_chat_history(db, chat_history_id)
    if not db_chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return curd.update_content_creation_chat_history(db, chat_history_id, content_creation_chat_history)


@router.delete('/chat-histories/{chat_history_id}')
def delete_content_creation_chat_history_api(chat_history_id: int, db: Session = Depends(get_db)):
    db_chat_history = curd.get_content_creation_chat_history(db, chat_history_id)
    if not db_chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    curd.delete_content_creation_chat_history(db, chat_history_id)
    return {"detail": "Chat history deleted"}