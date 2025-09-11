from pydantic import BaseModel
from typing import Optional

class CallrecordBase(BaseModel):
    from_contact_number: str
    contact_number: str
    result: str
    created_at: Optional[str] = None

class CallrecordCreate(CallrecordBase):
    pass
class CallrecordOut(CallrecordBase):
    id: int
    class Config:
        orm_mode = True


class DeleteResponse(BaseModel):
    id: int
    detail: str