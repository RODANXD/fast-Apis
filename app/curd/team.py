
from sqlalchemy.orm import Session
from app.models.users import Teammembers
from app.schema.team import TeamMemberCreate, TeamMemberBase, TeamMemberOut

def get_team_members(db: Session):
    return db.query(Teammembers).all()

def get_team_member(db: Session, team_member_id: int):
    return db.query(Teammembers).filter(Teammembers.id == team_member_id).first()

def create_team_member(db: Session, team_member: TeamMemberCreate):
    data = team_member.dict(by_alias=True, exclude_unset=True)
    # map alias 'teamId' if provided under 'team_id'
    if 'teamId' in data and 'teamId' not in data:
        data['teamId'] = data.pop('teamId')
    db_team_member = Teammembers(**data)
    db.add(db_team_member)
    db.commit()
    db.refresh(db_team_member)
    return db_team_member

def update_team_member(db: Session, team_member_id: int, team_member: TeamMemberCreate):
    db_member = db.query(Teammembers).filter(Teammembers.id == team_member_id).first()
    if not db_member:
        return None
    data = team_member.dict(by_alias=True, exclude_unset=True)
    if 'teamId' in data and 'teamId' not in data:
        data['teamId'] = data.pop('team_id')
    for key, value in data.items():
        setattr(db_member, key, value)
    db.commit()
    db.refresh(db_member)
    return db_member

def delete_team_member(db: Session, team_member_id: int):
    db_member = db.query(Teammembers).filter(Teammembers.id == team_member_id).first()
    if db_member:
        db.delete(db_member)
        db.commit()