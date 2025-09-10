from fastapi import APIRouter, Depends, HTTPException, Request
from datetime import timedelta
from app.auth import create_access_token, create_refresh_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.users import User

router = APIRouter(prefix="/auth", tags=["auth"])


# NOTE: This demo assumes a simple password check. Replace with your user auth logic.
@router.post('/token')
async def login_for_access_token(request: Request, db: Session = Depends(get_db)):
    # support application/x-www-form-urlencoded (OAuth2PasswordRequestForm) and application/json
    username = None
    password = None
    content_type = request.headers.get('content-type', '')
    if content_type.startswith('application/json'):
        body = await request.json()
        username = body.get('username') or body.get('email')
        password = body.get('password')
    else:
        form = await request.form()
        username = form.get('username')
        password = form.get('password')

    if not username or not password:
        raise HTTPException(status_code=400, detail='username and password are required')

    user = db.query(User).filter(User.email == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": str(user.id)}, expires_delta=access_token_expires)
    refresh_token = create_refresh_token({"sub": str(user.id)})
    # persist tokens on user
    user.accessToken = access_token
    user.refreshToken = refresh_token
    db.commit()
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}
