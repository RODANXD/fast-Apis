from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.knowlegebase import KnowledgeBaseBase, KnowledgeBaseCreate, KnowledgeBaseOut, KnowledgeBaseUpdate,DeleteKnowledgeBase
from app.curd import knowledgebase as curd

router = APIRouter(prefix="/knowledge-bases", tags=["Knowledge Bases"])
@router.get('/', response_model=list[KnowledgeBaseOut])
def list_knowledge_bases(db: Session = Depends(get_db)):
    return curd.get_knowledge_bases(db)

@router.get('/{id}', response_model=KnowledgeBaseOut)
def get_knowledge_base(id: int, db: Session = Depends(get_db)):
    return curd.get_knowledge_base(db, id)

@router.post('/', response_model=KnowledgeBaseOut)
def create_knowledge_base(knowledge_base: KnowledgeBaseCreate, db: Session = Depends(get_db)):
    return curd.create_knowledge_base(db, knowledge_base)

@router.put('/{id}', response_model=KnowledgeBaseOut)
def update_knowledge_base(id: int, knowledge_base: KnowledgeBaseUpdate, db: Session = Depends(get_db)):
    db_knowledge_base = curd.get_knowledge_base(db, id)
    if not db_knowledge_base:
        raise HTTPException(status_code=404, detail="Knowledge Base not found")
    return curd.update_knowledge_base(db, id, knowledge_base)
@router.delete('/{id}', response_model=DeleteKnowledgeBase)
def delete_knowledge_base(id: int, db: Session = Depends(get_db)):
    db_knowledge_base = curd.get_knowledge_base(db, id)
    if not db_knowledge_base:
        raise HTTPException(status_code=404, detail="Knowledge Base not found")
    curd.delete_knowledge_base(db, id)
    # return both id and detail to satisfy the DeleteKnowledgeBase response schema
    return {"id": id, "detail": "Knowledge Base deleted successfully"}
