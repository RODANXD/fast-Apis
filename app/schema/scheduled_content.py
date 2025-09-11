from pydantic import BaseModel
from typing import Optional
from datetime import date, time, datetime


class ScheduledContentBase(BaseModel):
    text: str
    document: Optional[str] = None
    platform: str
    platform_unique_id: str
    scheduled_type: str
    scheduled_date: Optional[date] = None
    scheduled_time: Optional[time] = None
    published_time: Optional[datetime] = None
    user_id: Optional[int] = None
    media_type: str
    media_id: Optional[str] = None


class ScheduledContentCreate(ScheduledContentBase):
    pass


class ScheduledContentUpdate(BaseModel):
    text: Optional[str] = None
    document: Optional[str] = None
    platform: Optional[str] = None
    platform_unique_id: Optional[str] = None
    scheduled_type: Optional[str] = None
    scheduled_date: Optional[date] = None
    scheduled_time: Optional[time] = None
    published_time: Optional[datetime] = None
    user_id: Optional[int] = None
    media_type: Optional[str] = None
    media_id: Optional[str] = None

    class Config:
        orm_mode = True


class ScheduledContentOut(ScheduledContentBase):
    id: int

    class Config:
        orm_mode = True
