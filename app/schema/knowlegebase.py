from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class KnowledgeBaseBase(BaseModel):
    # The DB model for knowledge base doesn't have a separate `name` column.
    # Keep fields that exist on the SQLAlchemy model.
    data: Optional[str] = None
    data_type: Optional[str] = None
    path: Optional[str] = None
    user_id: Optional[int] = None
class KnowledgeBaseCreate(KnowledgeBaseBase):
    pass
class KnowledgeBaseOut(KnowledgeBaseBase):
    id: int

    class Config:
        orm_mode = True
class KnowledgeBaseUpdate(BaseModel):
    name: Optional[str] = None
    data: Optional[str] = None
    data_type: Optional[str] = None
    path: Optional[str] = None
    user_id: Optional[int] = None


    class Config:
        orm_mode = True
class DeleteKnowledgeBase(BaseModel):
    id: int
    detail: str