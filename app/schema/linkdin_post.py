from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LinkedInPostBase(BaseModel):
    generated_content: str
    topic: str
    tone: str
    custom_instructions: Optional[str] = None
    prompt: Optional[str] = None
    created_at: datetime
    user: Optional[int] = None

class LinkedInPostCreate(LinkedInPostBase):
    pass

class LinkedInPostUpdate(LinkedInPostBase):
    generated_content: Optional[str] = None
    topic: Optional[str] = None
    tone: Optional[str] = None
    custom_instructions: Optional[str] = None
    prompt: Optional[str] = None
    created_at: Optional[datetime] = None
    user: Optional[int] = None

class LinkedInPostOut(LinkedInPostBase):
    id: int
    class Config:
        orm_mode = True
