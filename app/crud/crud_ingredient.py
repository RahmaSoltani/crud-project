from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate, IngredientUpdate

def get_all(db: Session):
    return db.query(Ingredient).all()

def get_by_id(db: Session, ingredient_id: int):
    return db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()

def create(db: Session, ingredient: IngredientCreate):
    db_item = Ingredient(**ingredient.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, ingredient_id: int, ingredient: IngredientUpdate):
    db_item = get_by_id(db, ingredient_id)
    if db_item:
        for key, value in ingredient.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete(db: Session, ingredient_id: int):
    db_item = get_by_id(db, ingredient_id)
    if db_item:
        # Unlink from all associated recipes
        db_item.recipes.clear()
        db.commit()

        # Now delete the ingredient itself
        db.delete(db_item)
        db.commit()
    return db_item
