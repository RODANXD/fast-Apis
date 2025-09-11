from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class WhatsAppConnectionBase(BaseModel):
    whatsapp_business_id: str
    whatsapp_phone_id: str
    phone_number: Optional[str] = None
    name: Optional[str] = None
    access_token: str
    expiry_time: Optional[datetime] = None
    user_id: Optional[int] = None


class WhatsAppConnectionCreate(WhatsAppConnectionBase):
    pass


class WhatsAppConnectionUpdate(BaseModel):
    phone_number: Optional[str] = None
    name: Optional[str] = None
    access_token: Optional[str] = None
    expiry_time: Optional[datetime] = None
    user_id: Optional[int] = None

    class Config:
        orm_mode = True


class WhatsAppConnectionOut(WhatsAppConnectionBase):
    class Config:
        orm_mode = True
