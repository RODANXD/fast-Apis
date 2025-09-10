from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any

class ContentBase(BaseModel):
    text: str
    post_type: str
    language: str
    media_type: str
    video_duration: Optional[str] = None
    author: Optional[str] = None
    post_id: str
    post_status: Optional[str] = None
    caption: Optional[str] = None
    media_urls: Optional[List[Dict[str, Any]]] = None
    created_at: datetime
    user_id: Optional[int] = None

class ContentCreate(ContentBase):
    pass

class ContentOut(ContentBase):
    id: int
    class Config:
        orm_mode = True

class ContentDetailOut(ContentOut):
    id: int
    detail : str



class ContentCreationChatHistoryBase(BaseModel):
    thread_id: Optional[str] = None
    chat_history: Optional[List[Dict[str, Any]]] = None
    name: str
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
class ContentCreationChatHistoryCreate(ContentCreationChatHistoryBase):
    pass
class ContentCreationChatHistoryOut(ContentCreationChatHistoryBase):
    id: int
    class Config:
        orm_mode = True
class ContentCreationChatHistoryUpdate(ContentCreationChatHistoryBase):
    thread_id: Optional[str] = None
    chat_history: Optional[List[Dict[str, Any]]] = None
    name: Optional[str] = None
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
class DeleteResponse(BaseModel):
    id: int
    detail: str