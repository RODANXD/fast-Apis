from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TeamMemberBase(BaseModel):
    isAdmin: Optional[bool] = None
    role: str
    teamId: Optional[str] = Field(None, alias='teamId')
    userId: Optional[int] = None

    class Config:
        allow_population_by_field_name = True

class TeamMemberOut(TeamMemberBase):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class TeamMemberCreate(TeamMemberBase):
    pass

