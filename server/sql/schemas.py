# schemas is synonym for pydantic models
from typing import Union
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: Union[str, None] = None
    quantity: int = None



class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    items: list[Item] = []

    class Config:
        orm_mode = True
