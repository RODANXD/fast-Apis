from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class GoogleCalendarConnectionBase(BaseModel):
    calendar_id: str
    email: str
    name: Optional[str] = None
    timezone: str
    access_token: str
    refresh_token: str
    expiry_time: Optional[datetime] = None
    user_id: Optional[int] = None

class GoogleCalendarConnectionCreate(GoogleCalendarConnectionBase):
    pass

class GoogleCalendarConnectionUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    timezone: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expiry_time: Optional[datetime] = None
    user_id: Optional[int] = None

    class Config:
        orm_mode = True

class GoogleCalendarConnectionOut(GoogleCalendarConnectionBase):
    class Config:
        orm_mode = True

class DeleteCalendarConnection(BaseModel):
    id: str
    detail: str