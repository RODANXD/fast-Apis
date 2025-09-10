from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class AccountChatHistoryBase(BaseModel):
    thread_id: Optional[str] = None
    chat_history: Optional[list] = None
    name: str
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AccountChatHistoryCreate(AccountChatHistoryBase):
    pass


class AccountChatHistoryOut(AccountChatHistoryBase):
    id: int

    class Config:
        orm_mode = True




class HRChatHistoryBase(BaseModel):
    thread_id: Optional[str] = None
    chat_history: Optional[List[Dict[str, Any]]] = None
    name: str
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class HRChatHistoryCreate(HRChatHistoryBase):
    pass

class HRChatHistoryUpdate(HRChatHistoryBase):
    thread_id: Optional[str] = None
    chat_history: Optional[List[Dict[str, Any]]] = None
    name: Optional[str] = None
    user_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class HRChatHistoryOut(HRChatHistoryBase):
    id: int
    class Config:
        orm_mode = True
