from sqlalchemy.orm import Session
from app.models.users import GoogleCalendarConnectionDetails
from app.schema.googlecalender import GoogleCalendarConnectionBase, GoogleCalendarConnectionCreate, GoogleCalendarConnectionOut, GoogleCalendarConnectionUpdate


def get_google_calendar_connections(db: Session):
    return db.query(GoogleCalendarConnectionDetails).all()


def get_google_calendar_connection(db: Session, calendar_id: str):
    return db.query(GoogleCalendarConnectionDetails).filter(GoogleCalendarConnectionDetails.calendar_id == calendar_id).first()


def create_google_calendar_connection(db: Session, google_calendar_connection: GoogleCalendarConnectionCreate):
    data = google_calendar_connection.dict(exclude_unset=True)
    calendar_id = data.get("calendar_id")
    if calendar_id:
        existing = db.query(GoogleCalendarConnectionDetails).filter(GoogleCalendarConnectionDetails.calendar_id == calendar_id).first()
        if existing:
            # update tokens and any provided fields
            for k, v in data.items():
                setattr(existing, k, v)
            db.commit()
            db.refresh(existing)
            return existing

    db_google_calendar_connection = GoogleCalendarConnectionDetails(**data)
    db.add(db_google_calendar_connection)
    db.commit()
    db.refresh(db_google_calendar_connection)
    return db_google_calendar_connection


def update_google_calendar_connection(db: Session, calendar_id: str, google_calendar_connection: GoogleCalendarConnectionUpdate):
    db_google_calendar_connection = db.query(GoogleCalendarConnectionDetails).filter(GoogleCalendarConnectionDetails.calendar_id == calendar_id).first()
    if not db_google_calendar_connection:
        return None
    for key, value in google_calendar_connection.dict(exclude_unset=True).items():
        setattr(db_google_calendar_connection, key, value)
    db.commit()
    db.refresh(db_google_calendar_connection)
    return db_google_calendar_connection


def delete_google_calendar_connection(db: Session, calendar_id: str):
    db_google_calendar_connection = db.query(GoogleCalendarConnectionDetails).filter(GoogleCalendarConnectionDetails.calendar_id == calendar_id).first()
    if not db_google_calendar_connection:
        return None
    db.delete(db_google_calendar_connection)
    db.commit()
    return db_google_calendar_connection

def get_calendar_connections_by_user_id(db: Session, user_id: int):
    return db.query(GoogleCalendarConnectionDetails).filter(GoogleCalendarConnectionDetails.user_id == user_id).all()