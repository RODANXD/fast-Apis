from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    userId: int | None
    paymentId: str
    amountPaid: float
    email: str
    status: str
    paymentMethod: str | None = None
    subscriptionType: str | None = None
    receiptUrl: str | None = None
    currency: str | None = None
    transactionDate: datetime | None = None
    created_at: datetime | None = None

class TransactionOut(TransactionCreate):
    id: int
    class Config:
        orm_mode = True

class TransactionUpdate(BaseModel):
    pass
