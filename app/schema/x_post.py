from pydantic import BaseModel
from typing import Optional


class XPostOut(BaseModel):
    id: int
    user: Optional[int] = None

    class Config:
        orm_mode = True
