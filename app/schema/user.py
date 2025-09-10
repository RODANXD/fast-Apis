from pydantic import BaseModel

class UserBase(BaseModel):
    firstName: str | None
    lastName: str | None
    email: str
    country: str | None
    role: str | None
    phoneNumber: str | None = None
    image: str | None = None
    city: str | None = None
    company: str | None = None
    countryCode: str | None = None
    subscriptionType: str | None = None


class UserCreate(UserBase):
    password: str | None = None


class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True
