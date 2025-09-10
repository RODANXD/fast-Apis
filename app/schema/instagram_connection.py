from pydantic import BaseModel
from typing import Optional


class InstagramConnectionBase(BaseModel):
    instagram_user_id: str
    user_id: Optional[int] = None


class InstagramConnectionOut(InstagramConnectionBase):
    class Config:
        orm_mode = True
