from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from sql.database import SessionLocal
from sql import schemas
from dependencies import items_crud

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = items_crud.get_items(db, skip=skip, limit=limit)
    return items