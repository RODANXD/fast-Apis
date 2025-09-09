from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ContactBase(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    businessName: Optional[str] = None
    companyName: Optional[str] = None
    countryCode: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    created: Optional[str] = None
    lastActivity: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[str] = None
    additionalEmails: Optional[str] = None
    additionalPhones: Optional[str] = None
    team_id: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    businessName: Optional[str] = None
    companyName: Optional[str] = None
    countryCode: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    created: Optional[str] = None
    lastActivity: Optional[str] = None
    status: Optional[str] = None
    tags: Optional[str] = None
    additionalEmails: Optional[str] = None
    additionalPhones: Optional[str] = None
    team_id: Optional[str] = None

class ContactOut(ContactBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class ContactListBase(BaseModel):
    contactid: Optional[int] = None
    lists_id: Optional[int] = None

class ContactListCreate(ContactListBase):
    pass

class ContactListUpdate(BaseModel):
    contactid: Optional[int] = None
    lists_id: Optional[int] = None
    
class ContactListOut(ContactListBase):
    id: int

    class Config:
        orm_mode = True