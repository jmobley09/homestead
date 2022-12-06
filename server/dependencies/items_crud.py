from sqlalchemy.orm import Session

from sql import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate, category_id: int):
    db_item = models.Item(**item.dict(), owner_id=category_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item