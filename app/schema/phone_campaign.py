from pydantic import BaseModel
from datetime import datetime

class PhoneCampaignBase(BaseModel):
    campaign_name: str
    language: str
    voice: str
    choose_calendar: str | None = None
    max_call_time: int | None = None
    country: str
    phone_number: str
    status: str | None = None
    catch_phrase: str
    call_script: str
    tom_engages: bool | None = False
    created_at: datetime | None = None
    agent: int | None = None
    user_id: int | None = None
    target_lists: int

class PhoneCampaignCreate(PhoneCampaignBase):
    pass

class PhoneCampaignUpdate(PhoneCampaignBase):
    campaign_name: str | None = None
    language: str | None = None
    voice: str | None = None
    choose_calendar: str | None = None
    max_call_time: int | None = None
    country: str | None = None
    phone_number: str | None = None
    status: str | None = None
    catch_phrase: str | None = None
    call_script: str | None = None
    tom_engages: bool | None = None
    created_at: datetime | None = None
    agent: int | None = None
    user_id: int | None = None
    target_lists: int | None = None
    

class PhoneCampaignOut(PhoneCampaignBase):
    id: int
    class Config:
        orm_mode = True
