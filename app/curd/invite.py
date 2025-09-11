from sqlalchemy.orm import Session
from app.models.users import InviteTokens, User, Team
from app.schema.invite import InviteTokenCreate, InviteTokenRedeem, InviteTokenOut
from uuid import uuid4
from datetime import datetime, timedelta


def create_invite_token(db: Session, invite: InviteTokenCreate, ttl_hours: int = 72):
    token = invite.token or str(uuid4())
    expires_at = invite.expiresAt or (datetime.utcnow() + timedelta(hours=ttl_hours))
    # if invite references a teamId that doesn't exist, create minimal team row
    if invite.teamId:
        existing_team = db.query(Team).filter(Team.id == invite.teamId).first()
        if not existing_team:
            # create a minimal team record so FK constraint passes
            new_team = Team(id=invite.teamId, userId=invite.userId or None, numberOfTeamMembers=0, credits=0)
            db.add(new_team)
            db.flush()

    db_token = InviteTokens(
        email=invite.email or "",
        token=token,
        userId=invite.userId,
        teamId=invite.teamId,
        role=invite.role,
        expiresAt=expires_at,
        accepted=False,
        created_at=datetime.utcnow(),
    )
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token


def redeem_invite_token(db: Session, redeem: InviteTokenRedeem):
    token_row = db.query(InviteTokens).filter(InviteTokens.token == redeem.token).first()
    if not token_row:
        return None
    if token_row.accepted:
        return None
    if token_row.expiresAt and token_row.expiresAt < datetime.utcnow():
        return None

    # mark accepted and optionally associate a user
    token_row.accepted = True
    if redeem.userId:
        token_row.userId = redeem.userId
    if redeem.email and not token_row.email:
        token_row.email = redeem.email
    db.commit()
    db.refresh(token_row)
    return token_row


