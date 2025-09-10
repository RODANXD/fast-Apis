from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.googlecalender import GoogleCalendarConnectionBase, GoogleCalendarConnectionCreate, GoogleCalendarConnectionOut, GoogleCalendarConnectionUpdate, DeleteCalendarConnection
from app.auth import get_current_user

from app.curd import googlecalender as curd


router = APIRouter(prefix="/google-calendar", tags=["Google Calendar Connections"])

@router.get('/', response_model=list[GoogleCalendarConnectionOut])
def list_google_calendar_connections(db: Session = Depends(get_db)):
    return curd.get_google_calendar_connections(db)

@router.get('/{calendar_id}', response_model=GoogleCalendarConnectionOut)
def read_google_calendar_connection(calendar_id: str, db: Session = Depends(get_db)):
    connection = curd.get_google_calendar_connection(db, calendar_id)
    if not connection:
        raise HTTPException(status_code=404, detail="Google Calendar connection not found")
    return connection

@router.post('/', response_model=GoogleCalendarConnectionOut)
def create_google_calendar_connection(connection: GoogleCalendarConnectionCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    # if tokens not provided in request, use authenticated user's stored tokens
    data = connection.dict(exclude_unset=True)
    if not data.get('access_token') and getattr(current_user, 'accessToken', None):
        data['access_token'] = current_user.accessToken
    if not data.get('refresh_token') and getattr(current_user, 'refreshToken', None):
        data['refresh_token'] = current_user.refreshToken
    return curd.create_google_calendar_connection(db, GoogleCalendarConnectionCreate(**data))


@router.put('/{calendar_id}', response_model=GoogleCalendarConnectionOut)
def update_google_calendar_connection_api(calendar_id: str, connection: GoogleCalendarConnectionUpdate, db: Session = Depends(get_db)):
    db_connection = curd.get_google_calendar_connection(db, calendar_id)
    data = connection.dict(exclude_unset=True)
    if not db_connection:
        # upsert: create new connection with provided fields and calendar_id
        data['calendar_id'] = calendar_id
        return curd.create_google_calendar_connection(db, GoogleCalendarConnectionCreate(**data))
    return curd.update_google_calendar_connection(db, calendar_id, connection)

@router.delete('/{calendar_id}', response_model=DeleteCalendarConnection)
def delete_google_calendar_connection_api(calendar_id: str, db: Session = Depends(get_db)):
    db_connection = curd.get_google_calendar_connection(db, calendar_id)
    if not db_connection:
        raise HTTPException(status_code=404, detail="Google Calendar connection not found")
    curd.delete_google_calendar_connection(db, calendar_id)
    return {"id": calendar_id, "detail": "Google Calendar connection deleted"}