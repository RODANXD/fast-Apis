from sqlalchemy.orm import Session
from app.models.users import KnowledgeBase
from app.schema.knowlegebase import KnowledgeBaseBase, KnowledgeBaseCreate, KnowledgeBaseOut, KnowledgeBaseUpdate

def get_knowledge_bases(db: Session):
    return db.query(KnowledgeBase).all()

def get_knowledge_base(db: Session, id: int):
    return db.query(KnowledgeBase).filter(KnowledgeBase.id == id).first()

def create_knowledge_base(db: Session, knowledge_base: KnowledgeBaseCreate):
    db_knowledge_base = KnowledgeBase(**knowledge_base.dict())
    db.add(db_knowledge_base)
    db.commit()
    db.refresh(db_knowledge_base)
    return db_knowledge_base

def update_knowledge_base(db: Session, id: int, knowledge_base: KnowledgeBaseUpdate):
    db_knowledge_base = db.query(KnowledgeBase).filter(KnowledgeBase.id == id).first()
    for key, value in knowledge_base.dict().items():
        setattr(db_knowledge_base, key, value)
    db.commit()
    db.refresh(db_knowledge_base)
    return db_knowledge_base

def delete_knowledge_base(db: Session, id: int):
    db_knowledge_base = db.query(KnowledgeBase).filter(KnowledgeBase.id == id).first()
    if db_knowledge_base:
        db.delete(db_knowledge_base)
        db.commit()
    return db_knowledge_base
