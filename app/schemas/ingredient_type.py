from pydantic import BaseModel

class IngredientTypeBase(BaseModel):
    name: str

class IngredientTypeCreate(IngredientTypeBase):
    pass

class IngredientTypeUpdate(IngredientTypeBase):
    pass

class IngredientTypeOut(IngredientTypeBase):
    id: int

    class Config:
        orm_mode = True
