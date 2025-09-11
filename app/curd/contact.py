from sqlalchemy.orm import Session
from app.models.users import Contact, Team, ContactList, Lists
from app.schema.contact import ContactCreate, ContactUpdate, ContactOut
from app.schema.contact import ContactListCreate, ContactListOut, ContactListBase
from sqlalchemy.exc import IntegrityError

def get_contacts(db: Session):
    return db.query(Contact).all()

def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def create_contact(db: Session, contact: ContactCreate):
    data = contact.dict(exclude_unset=True)
    team_id = data.get('team_id')
    if team_id:
        team = db.query(Team).filter(Team.id == team_id).first()
        if not team:
            raise IntegrityError(statement=None, params=None, orig=Exception(f"team id {team_id} does not exist"))
    db_contact = Contact(**data)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: int, contact_update: ContactUpdate):
    db_contact = get_contact(db, contact_id)
    if not db_contact:
        return None
    for key, value in contact_update.dict(exclude_unset=True).items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = get_contact(db, contact_id)
    if not db_contact:
        return False
    db.delete(db_contact)
    db.commit()
    return True


def get_contact_lists(db: Session):
    return db.query(ContactList).all()

def get_contact_list(db: Session, contact_list_id: int):
    return db.query(ContactList).filter(ContactList.id == contact_list_id).first()

def create_contact_list(db: Session, contact_list: ContactListCreate):
    data = contact_list.dict(exclude_unset=True)
    contactid = data.get('contactid')
    if contactid:
        contact = db.query(Contact).filter(Contact.id == contactid).first()
        if not contact:
            raise IntegrityError(statement=None, params=None, orig=Exception(f"contact id {contactid} does not exist"))
    lists_id = data.get('lists_id')
    if lists_id:
        list_row = db.query(Lists).filter(Lists.id == lists_id).first()
        if not list_row:
            raise IntegrityError(statement=None, params=None, orig=Exception(f"lists id {lists_id} does not exist"))
    db_contact_list = ContactList(**data)
    db.add(db_contact_list)
    db.commit()
    db.refresh(db_contact_list)
    return db_contact_list

def update_contact_list(db: Session, contact_list_id: int, contact_list_update: ContactListBase):
    db_contact_list = db.query(ContactList).filter(ContactList.id == contact_list_id).first()
    if not db_contact_list:
        return None
    data = contact_list_update.dict(exclude_unset=True)
    contactid = data.get('contactid')
    if contactid:
        contact = db.query(Contact).filter(Contact.id == contactid).first()
        if not contact:
            raise IntegrityError(statement=None, params=None, orig=Exception(f"contact id {contactid} does not exist"))
    lists_id = data.get('lists_id')
    if lists_id:
        list_row = db.query(Lists).filter(Lists.id == lists_id).first()
        if not list_row:
            raise IntegrityError(statement=None, params=None, orig=Exception(f"lists id {lists_id} does not exist"))
    for key, value in data.items():
        setattr(db_contact_list, key, value)
    db.commit()
    db.refresh(db_contact_list)
    return db_contact_list

def delete_contact_list(db: Session, contact_list_id: int):
    db_contact_list = db.query(ContactList).filter(ContactList.id == contact_list_id).first()
    if not db_contact_list:
        return False
    db.delete(db_contact_list)
    db.commit()
    return True