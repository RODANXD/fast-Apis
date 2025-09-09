from sqlalchemy.orm import Session
from app.models.users import AgentPhoneNumber, PhoneAgent
from app.schema.agent import AgentBase, AgentOut, AgentCreate, AgentUpdate
from app.schema.agent import PhoneAgentBase, PhoneAgentCreate, PhoneAgentOut, PhoneAgentUpdate


def get_agents(db: Session):
    return db.query(AgentPhoneNumber).all()

def get_agent(db: Session, agent_id: int):
    return db.query(AgentPhoneNumber).filter(AgentPhoneNumber.id == agent_id).first()


def get_agent_by_phone_number(db: Session, phone_number: str):
    return db.query(AgentPhoneNumber).filter(AgentPhoneNumber.phone_number == phone_number).first()
def create_agent(db: Session, agent: AgentCreate):
    db_agent = AgentPhoneNumber(**agent.dict(exclude_unset=True))
    db.add(db_agent)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def update_agent(db: Session, agent_id: int, agent: AgentUpdate):
    db_agent = get_agent(db, agent_id)
    if not db_agent:
        return None
    for key, value in agent.dict(exclude_unset=True).items():
        setattr(db_agent, key, value)
    db.commit()
    db.refresh(db_agent)
    return db_agent

def delete_agent(db: Session, agent_id: int):
    db_agent = get_agent(db, agent_id)
    if not db_agent:
        return None
    db.delete(db_agent)
    db.commit()


def get_phone_agents(db: Session):
    return db.query(PhoneAgent).all()
def get_phone_agent(db: Session, phone_agent_id: int):
    return db.query(PhoneAgent).filter(PhoneAgent.id == phone_agent_id).first()

def create_phone_agent(db: Session, phone_agent: PhoneAgentCreate):
    db_phone_agent = PhoneAgent(**phone_agent.dict(exclude_unset=True))
    db.add(db_phone_agent)
    db.commit()
    db.refresh(db_phone_agent)
    return db_phone_agent

def update_phone_agent(db: Session, phone_agent_id: int, phone_agent: PhoneAgentUpdate):
    db_phone_agent = get_phone_agent(db, phone_agent_id)
    if not db_phone_agent:
        return None
    for key, value in phone_agent.dict(exclude_unset=True).items():
        setattr(db_phone_agent, key, value)
    db.commit()
    db.refresh(db_phone_agent)
    return db_phone_agent

def delete_phone_agent(db: Session, phone_agent_id: int):
    db_phone_agent = get_phone_agent(db, phone_agent_id)
    if not db_phone_agent:
        return None
    db.delete(db_phone_agent)
    db.commit()
    return db_phone_agent