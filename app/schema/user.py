from pydantic import BaseModel

class UserBase(BaseModel):
    firstName: str | None
    lastName: str | None
    email: str
    country: str | None
    role: str | None

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    class Config:
        orm_mode = True
