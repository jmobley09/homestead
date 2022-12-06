from fastapi import FastAPI
from sql import models
from sql.database import engine
from routers import categories

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(categories.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
