from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List, Dict, Any
from datetime import datetime

class Appointment(BaseModel):
    agent_name: str
    agent_personality: str
    agent_language: Optional[List[str]] = None
    gender: Optional[str] = None
    age: int
    business_description: str
    your_business_offer: str
    qualification_questions: Optional[List[str]] = None
    sequence: Dict[str, Any]
    objective_of_the_agent: str
    calendar_choosed: Optional[str] = None
    calendar_id: Optional[str] = None
    webpage_link: Optional[str] = None
    whatsapp_number: Optional[str] = None
    prompt: str
    platform_unique_id: Optional[str] = None
    is_followups_enabled: Optional[bool] = None
    follow_up_details: Optional[Dict[str, Any]] = None
    emoji_frequency: int
    is_active: Optional[bool] = None
    user_id: Optional[int] = None
    first_message: Optional[str] = None


class AppointmentCreate(Appointment):
    pass


class AppointmentUpdate(Appointment):
    agent_name: Optional[str] = None
    agent_personality: Optional[str] = None
    agent_language: Optional[List[str]] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    business_description: Optional[str] = None
    your_business_offer: Optional[str] = None
    qualification_questions: Optional[List[str]] = None
    sequence: Optional[Dict[str, Any]] = None
    objective_of_the_agent: Optional[str] = None
    calendar_choosed: Optional[str] = None
    calendar_id: Optional[str] = None
    webpage_link: Optional[str] = None
    whatsapp_number: Optional[str] = None
    prompt: Optional[str] = None
    platform_unique_id: Optional[str] = None
    is_followups_enabled: Optional[bool] = None
    follow_up_details: Optional[Dict[str, Any]] = None
    emoji_frequency: Optional[int] = None
    is_active: Optional[bool] = None
    user_id: Optional[int] = None
    first_message: Optional[str] = None

class AppointmentOut(Appointment):
    id: int
    
    class Config:
        orm_mode = True