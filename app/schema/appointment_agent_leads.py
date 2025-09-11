from pydantic import BaseModel
from typing import Optional


class AppointmentAgentLeadsBase(BaseModel):
    lead_id: Optional[int] = None

class AppointmentAgentLeadCreated(AppointmentAgentLeadsBase):
    pass


class AppointmentAgentLeadsOut(AppointmentAgentLeadsBase):
    id: int

    class Config:
        orm_mode = True
