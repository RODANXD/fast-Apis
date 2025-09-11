from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import date


class LeadAnalyticsBase(BaseModel):
    chat_history: Optional[List[Dict[str, Any]]] = None
    thread_id: Optional[str] = None
    agent_id: Optional[int] = None
    lead_id: Optional[int] = None
    agent_is_enabled: Optional[bool] = None
    status: Optional[str] = None
    platform_unique_id: Optional[str] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None

class LeadAnalyticsCreate(LeadAnalyticsBase):
    pass


class LeadAnalyticsUpdate(LeadAnalyticsBase):
    chat_history: Optional[List[Dict[str, Any]]] = None
    thread_id: Optional[str] = None
    agent_id: Optional[int] = None
    lead_id: Optional[int] = None
    agent_is_enabled: Optional[bool] = None
    status: Optional[str] = None
    platform_unique_id: Optional[str] = None
    created_at: Optional[date] = None
    updated_at: Optional[date] = None


class LeadAnalyticsOut(LeadAnalyticsBase):
    id: int
    class Config:
        orm_mode = True