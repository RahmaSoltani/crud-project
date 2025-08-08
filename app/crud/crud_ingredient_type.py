from sqlalchemy.orm import Session
from app.models.ingredient_type import IngredientType
from app.schemas.ingredient_type import IngredientTypeCreate, IngredientTypeUpdate
from app.models.ingredient import Ingredient
from app.schemas.ingredient import IngredientCreate, IngredientUpdate
from app.crud import crud_ingredient  

def get_all(db: Session):
    return db.query(IngredientType).all()

def get_by_id(db: Session, ingredient_type_id: int):
    return db.query(IngredientType).filter(IngredientType.id == ingredient_type_id).first()

def create(db: Session, ingredient_type: IngredientTypeCreate):
    db_item = IngredientType(name=ingredient_type.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, ingredient_type_id: int, ingredient_type: IngredientTypeUpdate):
    db_item = db.query(IngredientType).filter(IngredientType.id == ingredient_type_id).first()
    if db_item:
        db_item.name = ingredient_type.name
        db.commit()
        db.refresh(db_item)
    return db_item


def delete(db: Session, ingredient_type_id: int):
    db_item = db.query(IngredientType).filter(IngredientType.id == ingredient_type_id).first()
    if db_item:
        ingredients = db.query(Ingredient).filter(Ingredient.ingredient_type_id == ingredient_type_id).all()
        for ingredient in ingredients:
            crud_ingredient.delete(db, ingredient.id)

        db.delete(db_item)
        db.commit()
    return db_item

