from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schema.agent import AgentCreate, AgentOut, AgentUpdate
from app.schema.agent import PhoneAgentCreate, PhoneAgentOut, PhoneAgentUpdate
from app.curd import agent as curd

router = APIRouter(prefix="/agent-numbers", tags=["Agents Numbers"])

@router.get('/', response_model=list[AgentOut])
def list_agents(db: Session = Depends(get_db)):
    return curd.get_agents(db)


@router.get('/{agent_id}', response_model=AgentOut)
def get_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = curd.get_agent(db, agent_id)
    if agent is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found")
    return agent

@router.get('/by-phone/{phone_number}', response_model=AgentOut)
def get_agent_by_phone(phone_number: str, db: Session = Depends(get_db)):
    agent = curd.get_agent_by_phone_number(db, phone_number)
    if agent is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found")
    return agent

@router.post('/', response_model=AgentOut, status_code=status.HTTP_201_CREATED)
def create_agent(agent: AgentCreate, db: Session = Depends(get_db)):
    try:
        return curd.create_agent(db, agent)
    except IntegrityError as e:
        db.rollback()
        msg = str(e.orig) if e.orig is not None else str(e)

        if "agent_phone_numbers_phone_number_key" in msg or "unique" in msg.lower():
            raise HTTPException(status_code=400, detail="phone_number already exists")
        raise HTTPException(status_code=400, detail=msg)


@router.put('/{agent_id}', response_model=AgentOut)
def update_agent(agent_id: int, agent: AgentUpdate, db: Session = Depends(get_db)):
    updated = curd.update_agent(db, agent_id, agent)
    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent not found")
    return updated


@router.delete('/{agent_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    deleted = curd.delete_agent(db, agent_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agent Deleted not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/phone-agents/', response_model=list[PhoneAgentOut])
def list_phone_agents(db: Session = Depends(get_db)):
    return curd.get_phone_agents(db)


@router.get('/phone-agents/{phone_agent_id}', response_model=PhoneAgentOut)
def get_phone_agent(phone_agent_id: int, db: Session = Depends(get_db)):
    phone_agent = curd.get_phone_agent(db, phone_agent_id)
    if not phone_agent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone Agent not found")
    return phone_agent


@router.post('/phone-agents/', response_model=PhoneAgentOut)
def create_phone_agent(phone_agent: PhoneAgentCreate, db: Session = Depends(get_db)):
    try:
        return curd.create_phone_agent(db, phone_agent)
    except IntegrityError as e:
        db.rollback()
        msg = str(e.orig) if e.orig is not None else str(e)

        if "phone_agents_phone_number_key" in msg or "unique" in msg.lower():
            raise HTTPException(status_code=400, detail="phone_number already exists")
        raise HTTPException(status_code=400, detail=msg)


@router.put('/phone-agents/{phone_agent_id}', response_model=PhoneAgentOut)
def update_phone_agent(phone_agent_id: int, phone_agent: PhoneAgentUpdate, db: Session = Depends(get_db)):
    phone_agent = curd.update_phone_agent(db, phone_agent_id, phone_agent)
    if not phone_agent:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Phone Agent not found")
    return phone_agent


@router.delete('/phone-agents/{phone_agent_id}')
def delete_phone_agent(phone_agent_id: int, db: Session = Depends(get_db)):
    curd.delete_phone_agent(db, phone_agent_id)
    return {"message": "Phone Agent deleted successfully"}
