from pydantic import BaseModel
from typing import Optional


class XpostBase(BaseModel):
    generated_content: str
    topic: str
    purpose: str
    custom_instructions: Optional[str] = None
    prompt: Optional[str] = None
    created_at: Optional[str] = None
    user: Optional[int] = None

class XPostCreate(XpostBase):
    pass

class XPostUpdate(BaseModel):
    generated_content: Optional[str] = None
    topic: Optional[str] = None
    purpose: Optional[str] = None
    custom_instructions: Optional[str] = None
    prompt: Optional[str] = None
    created_at: Optional[str] = None
    user: Optional[int] = None

    class Config:
        orm_mode = True


class XPostOut(BaseModel):
    id: int
    generated_content: str
    topic: str
    purpose: str
    custom_instructions: Optional[str] = None
    prompt: Optional[str] = None
    created_at: Optional[str] = None
    user: Optional[int] = None

    class Config:
        orm_mode = True

class ResponseDelete(BaseModel):
    id: int
    detail: str