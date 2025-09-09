from pydantic import BaseModel
from datetime import datetime


class AgentBase(BaseModel):
    name: str
    country: str
    phone_number: str
    number_type: str
    status: bool | None = None
    user_id: int | None = None
    created_at: datetime | None = None


class AgentCreate(AgentBase):
    pass

class AgentUpdate(AgentBase):
    name: str | None = None
    country: str | None = None
    phone_number: str | None = None
    number_type: str | None = None
    status: bool | None = None
    user_id: int | None = None

class AgentOut(AgentBase):
    id: int

    class Config:
        orm_mode = True
    

from typing import Optional


class PhoneAgentBase(BaseModel):
    agent_name: str
    language: str
    voice: str
    status: Optional[bool] = None
    phone_number: Optional[str] = None
    user_id: Optional[int] = None


class PhoneAgentCreate(PhoneAgentBase):
    pass


class PhoneAgentUpdate(PhoneAgentBase):
    agent_name: Optional[str] = None
    language: Optional[str] = None
    voice: Optional[str] = None
    status: Optional[bool] = None
    phone_number: Optional[str] = None
    user_id: Optional[int] = None

class PhoneAgentOut(PhoneAgentBase):
    id: int

    class Config:
        orm_mode = True


