from fastapi import HTTPException
from app.schema.user import UserCreate, UserOut, UserBase
from app.curd.user import create_user, get_user, get_all_users, update_user, delete_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schema.user import UserCreate, UserOut
from app.curd.user import create_user, get_user, get_all_users

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print("Error getting database session ❌", e)
        raise
    finally:
        db.close()

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)

@router.get("/", response_model=list[UserOut])
def list_users_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_users(db, skip, limit)

@router.put("/{user_id}", response_model=UserOut)
def update_user_api(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db, user_id, user)

@router.delete("/{user_id}")
def delete_user_api(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user(db, user_id)
    return {"detail": "User deleted"}


    