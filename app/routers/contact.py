from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.schema.contact import ContactCreate, ContactUpdate, ContactOut
from app.schema.contact import ContactListCreate, ContactListOut, ContactListUpdate
from app.curd import contact as crud

router = APIRouter(prefix="/contacts", tags=["Contacts"])

@router.get("/", response_model=list[ContactOut])
def list_contacts(db: Session = Depends(get_db)):
    return crud.get_contacts(db)

@router.get("/{contact_id}", response_model=ContactOut)
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = crud.get_contact(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

@router.post("/", response_model=ContactOut, status_code=status.HTTP_201_CREATED)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_contact(db, contact)
    except IntegrityError as e:
        # This typically means the provided team_id does not exist (FK violation)
        msg = str(e.orig) if hasattr(e, 'orig') and e.orig is not None else str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

@router.put("/{contact_id}", response_model=ContactOut)
def update_contact(contact_id: int, contact: ContactUpdate, db: Session = Depends(get_db)):
    updated = crud.update_contact(db, contact_id, contact)
    if not updated:
        raise HTTPException(status_code=404, detail="Contact not found")
    return updated

@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_contact(db, contact_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Contact not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/lists/", response_model=list[ContactListOut])
def list_contact_lists(db: Session = Depends(get_db)):
    return crud.get_contact_lists(db)

@router.post("/lists/", response_model=ContactListOut, status_code=status.HTTP_201_CREATED)
def create_contact_list(contact_list: ContactListCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_contact_list(db, contact_list)
    except IntegrityError as e:
        msg = str(e.orig) if hasattr(e, 'orig') and e.orig is not None else str(e)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)
    

@router.put("/lists/{list_id}", response_model=ContactListOut)
def update_contact_list(list_id: int, contact_list: ContactListUpdate, db: Session = Depends(get_db)):
    updated = crud.update_contact_list(db, list_id, contact_list)
    if not updated:
        raise HTTPException(status_code=404, detail="Contact List not found")
    return updated

@router.delete("/lists/{list_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact_list(list_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_contact_list(db, list_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Contact List not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/lists/{list_id}", response_model=ContactListOut)
def read_contact_list(list_id: int, db: Session = Depends(get_db)):
    contact_list = crud.get_contact_list(db, list_id)
    if not contact_list:
        raise HTTPException(status_code=404, detail="Contact List not found")
    return contact_list
