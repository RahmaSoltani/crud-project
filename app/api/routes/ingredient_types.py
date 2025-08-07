from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.ingredient_type import IngredientTypeCreate, IngredientTypeOut, IngredientTypeUpdate
from app.crud.crud_ingredient_type import (
    get_all, get_by_id, create, update, delete
)
from app.api.deps import get_db

router = APIRouter(tags=["Ingredient Types"])

@router.get("/", response_model=list[IngredientTypeOut])
def read_ingredient_types(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{ingredient_type_id}", response_model=IngredientTypeOut)
def read_ingredient_type(ingredient_type_id: int, db: Session = Depends(get_db)):
    db_item = get_by_id(db, ingredient_type_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Ingredient type not found")
    return db_item

@router.post("/", response_model=IngredientTypeOut)
def create_ingredient_type(item: IngredientTypeCreate, db: Session = Depends(get_db)):
    return create(db, item)

@router.put("/{ingredient_type_id}", response_model=IngredientTypeOut)
def update_ingredient_type(ingredient_type_id: int, item: IngredientTypeUpdate, db: Session = Depends(get_db)):
    updated = update(db, ingredient_type_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Ingredient type not found")
    return updated

@router.delete("/{ingredient_type_id}")
def delete_ingredient_type(ingredient_type_id: int, db: Session = Depends(get_db)):
    deleted = delete(db, ingredient_type_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ingredient type not found")
    return {"detail": "Deleted successfully"}
