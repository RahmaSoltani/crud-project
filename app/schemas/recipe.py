from pydantic import BaseModel
from typing import List, Optional
from .ingredient import IngredientOut

class RecipeBase(BaseModel):
    name: str
    instructions: Optional[str] = None

class RecipeCreate(BaseModel):
    name: str
    instructions: Optional[str] = None
    ingredient_ids: List[int] = []

class RecipeUpdate(BaseModel):
    name: Optional[str] = None
    instructions: Optional[str] = None
    ingredient_ids: Optional[List[int]] = None

class RecipeOut(RecipeBase):
    id: int
    ingredients: List[IngredientOut] = []

    class Config:
        orm_mode = True