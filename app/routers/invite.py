from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.invite import InviteTokenCreate, InviteTokenRedeem, InviteTokenOut
from app.curd import invite as curd

router = APIRouter(prefix="/invite-tokens", tags=["Invite Tokens"])


@router.post('/', response_model=InviteTokenOut, status_code=status.HTTP_201_CREATED)
def create_token(invite: InviteTokenCreate, db: Session = Depends(get_db)):
    token = curd.create_invite_token(db, invite)
    return token


@router.post('/redeem', response_model=InviteTokenOut)
def redeem_token(redeem: InviteTokenRedeem, db: Session = Depends(get_db)):
    token = curd.redeem_invite_token(db, redeem)
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid or expired token")
    return token


