from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.ingredient import IngredientCreate, IngredientUpdate, IngredientOut
from app.crud.crud_ingredient import get_all, get_by_id, create, update, delete
from app.api.deps import get_db

router = APIRouter(tags=["Ingredients"])

@router.get("/", response_model=list[IngredientOut])
def read_ingredients(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{ingredient_id}", response_model=IngredientOut)
def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    db_item = get_by_id(db, ingredient_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return db_item

@router.post("/", response_model=IngredientOut)
def create_ingredient(item: IngredientCreate, db: Session = Depends(get_db)):
    return create(db, item)

@router.put("/{ingredient_id}", response_model=IngredientOut)
def update_ingredient(ingredient_id: int, item: IngredientUpdate, db: Session = Depends(get_db)):
    updated = update(db, ingredient_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return updated

@router.delete("/{ingredient_id}")
def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    deleted = delete(db, ingredient_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return {"detail": "Deleted successfully"}
