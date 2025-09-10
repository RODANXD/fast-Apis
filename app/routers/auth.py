from fastapi import APIRouter, Depends, HTTPException, Request
from datetime import timedelta
import jwt
from app.auth import create_access_token, create_refresh_token, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from app.database import get_db
from sqlalchemy.orm import Session
from app.models.users import User

router = APIRouter(prefix="/auth", tags=["auth"])


# NOTE: This demo assumes a simple password check. Replace with your user auth logic.
@router.post('/token')
async def login_for_access_token(request: Request, db: Session = Depends(get_db)):
    # Try parsing JSON body first (works even if Content-Type is missing), then fall back to form
    username = None
    password = None
    try:
        body = await request.json()
        if isinstance(body, dict):
            username = body.get('username') or body.get('email')
            password = body.get('password')
    except Exception:
        # not JSON or failed to parse; will try form below
        pass

    if not username or not password:
        form = await request.form()
        username = username or form.get('username') or form.get('email')
        password = password or form.get('password')

    if not username or not password:
        raise HTTPException(status_code=400, detail='username and password are required')

    user = db.query(User).filter(User.email == username).first()
    if not user or user.password != password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": str(user.id)}, expires_delta=access_token_expires)
    refresh_token = create_refresh_token({"sub": str(user.id)})
    # persist refresh token on user (the DB schema stores refreshToken)
    user.refreshToken = refresh_token
    db.commit()
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": refresh_token}


@router.post('/refresh')
async def refresh_access_token(request: Request, db: Session = Depends(get_db)):
    # accept JSON or form with a `refresh_token` field
    content_type = request.headers.get('content-type', '')
    if content_type.startswith('application/json'):
        body = await request.json()
        refresh_token = body.get('refresh_token')
    else:
        form = await request.form()
        refresh_token = form.get('refresh_token')

    if not refresh_token:
        raise HTTPException(status_code=400, detail='refresh_token is required')

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get('sub'))
    except Exception:
        raise HTTPException(status_code=401, detail='Invalid refresh token')

    user = db.query(User).filter(User.id == user_id).first()
    if not user or user.refreshToken != refresh_token:
        raise HTTPException(status_code=401, detail='Invalid refresh token')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": str(user.id)}, expires_delta=access_token_expires)
    new_refresh_token = create_refresh_token({"sub": str(user.id)})
    # persist the new refresh token
    user.refreshToken = new_refresh_token
    db.commit()
    return {"access_token": access_token, "token_type": "bearer", "refresh_token": new_refresh_token}
