# app/schemas/ingredient.py
from pydantic import BaseModel
from typing import Optional

class IngredientBase(BaseModel):
    name: str

class IngredientCreate(IngredientBase):
    ingredient_type_id: int

class IngredientUpdate(BaseModel):
    name: Optional[str] = None
    ingredient_type_id: Optional[int] = None

class IngredientOut(IngredientBase):
    id: int
    ingredient_type_id: int

    class Config:
        orm_mode = True