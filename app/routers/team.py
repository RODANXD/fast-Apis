from app.schema.team import TeamMemberCreate
from app.curd.team import update_team_member, delete_team_member
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.team import TeamMemberOut, TeamMemberBase, TeamMemberCreate
from app.curd import team as curd

router = APIRouter(prefix="/team-members", tags=["Team Members"])

@router.get('/', response_model=list[TeamMemberOut])
def list_team_members(db: Session = Depends(get_db)):
    return curd.get_team_members(db)

@router.get('/{team_member_id}', response_model=TeamMemberOut)
def read_team_member(team_member_id: int, db: Session = Depends(get_db)):
    member = curd.get_team_member(db, team_member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Team member not found")
    return member

@router.post('/', response_model=TeamMemberOut)
def create_team_member(team_member: TeamMemberCreate, db: Session = Depends(get_db)):
    return curd.create_team_member(db, team_member)

@router.put('/{team_member_id}', response_model=TeamMemberOut)
def update_team_member_api(team_member_id: int, team_member: TeamMemberCreate, db: Session = Depends(get_db)):
    db_member = curd.get_team_member(db, team_member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Team member not found")
    return update_team_member(db, team_member_id, team_member)

@router.delete('/{team_member_id}')
def delete_team_member_api(team_member_id: int, db: Session = Depends(get_db)):
    db_member = curd.get_team_member(db, team_member_id)
    if not db_member:
        raise HTTPException(status_code=404, detail="Team member not found")
    delete_team_member(db, team_member_id)
    return {"detail": "Team member deleted"}