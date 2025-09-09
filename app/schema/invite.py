from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InviteTokenBase(BaseModel):
    token: Optional[str] = None
    teamId: Optional[str] = None
    userId: Optional[int] = None
    email: Optional[str] = None
    role: Optional[str] = None


class InviteTokenCreate(InviteTokenBase):
    expiresAt: Optional[datetime] = None


class InviteTokenRedeem(BaseModel):
    token: str
    userId: Optional[int] = None
    email: Optional[str] = None


class InviteTokenOut(InviteTokenBase):
    id: int
    accepted: Optional[bool] = None
    created_at: Optional[datetime] = None
    expiresAt: Optional[datetime] = None

    class Config:
        orm_mode = True


