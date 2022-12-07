from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sql import models
from sql.database import engine
from routers import categories, items

origins = [
    "http://localhost",
    "http://localhost:3000",
]

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(categories.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
