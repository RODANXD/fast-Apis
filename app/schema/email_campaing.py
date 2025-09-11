from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class EmailCampaignBase(BaseModel):
    campaign_title: str
    campaign_objective: str
    main_subject: str
    cta_type: str
    list_of_target: List[int]
    desired_tone: str
    language: str
    send_time_window: str
    start_date: date
    frequency: Optional[List[str]] = None
    include_brainai: bool = False
    include_branding: bool = False
    custom_prompt: Optional[str] = None
    text_length: str
    product_or_service_feature: str
    review: bool = False
    calender_choosed: Optional[str] = None
    url: str
    is_draft: bool = False
    status: Optional[str] = None
    is_active: bool = True
    user_id: Optional[int] = None

class EmailCampaignCreate(EmailCampaignBase):
    pass

class EmailCampaignUpdate(EmailCampaignBase):
    campaign_title: str | None = None
    campaign_objective: str | None = None
    main_subject: str | None = None
    cta_type: str | None = None
    list_of_target: List[int] | None = None
    desired_tone: str | None = None
    language: str | None = None
    send_time_window: str | None = None
    start_date: date | None = None
    frequency: Optional[List[str]] = None 
    include_brainai: bool = False
    include_branding: bool = False
    custom_prompt: Optional[str] = None
    text_length: str | None = None
    product_or_service_feature: str | None = None
    review: bool = False 
    calender_choosed: Optional[str] = None
    url: str | None = None
    is_draft: bool = False
    status: Optional[str] = None 
    is_active: bool = True
    user_id: Optional[int] = None

class EmailCampaignOut(EmailCampaignBase):
    id: int
    class Config:
        orm_mode = True
