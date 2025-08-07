from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.recipe import RecipeCreate, RecipeUpdate, RecipeOut
from app.crud.crud_recipe import get_all, get_by_id, create, update, delete
from app.api.deps import get_db

router = APIRouter(tags=["Recipes"])

@router.get("/", response_model=list[RecipeOut])
def read_recipes(db: Session = Depends(get_db)):
    return get_all(db)

@router.get("/{recipe_id}", response_model=RecipeOut)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    db_item = get_by_id(db, recipe_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return db_item

@router.post("/", response_model=RecipeOut)
def create_recipe(item: RecipeCreate, db: Session = Depends(get_db)):
    return create(db, item)

@router.put("/{recipe_id}", response_model=RecipeOut)
def update_recipe(recipe_id: int, item: RecipeUpdate, db: Session = Depends(get_db)):
    updated = update(db, recipe_id, item)
    if not updated:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    deleted = delete(db, recipe_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"detail": "Deleted successfully"}
