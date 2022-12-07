from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sql.database import SessionLocal
from sql import schemas
from dependencies import categories_crud, items_crud

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = categories_crud.get_category_by_name(db, name=category.name)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return categories_crud.create_category(db=db, category=category)

@router.get("/", response_model=list[schemas.Category])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = categories_crud.get_categories(db, skip=skip, limit=limit)
    return categories

@router.get("/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = categories_crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

# route for creating items associated with a category
@router.post("/{category_id}/items/", response_model=schemas.Item)
def create_item_for_category(
    category_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return items_crud.create_item(db=db, item=item, category_id=category_id)