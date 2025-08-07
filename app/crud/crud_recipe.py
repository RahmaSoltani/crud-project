from sqlalchemy.orm import Session
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate
from app.models.ingredient import Ingredient

def get_all(db: Session):
    return db.query(Recipe).all()

def get_by_id(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def create(db: Session, recipe: RecipeCreate):
    db_recipe = Recipe(name=recipe.name, instructions=recipe.instructions)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)

    # many-to-many
    db_recipe.ingredients = db.query(Ingredient).filter(Ingredient.id.in_(recipe.ingredient_ids)).all()
    db.commit()
    return db_recipe

def update(db: Session, recipe_id: int, recipe: RecipeUpdate):
    db_recipe = get_by_id(db, recipe_id)
    if db_recipe:
        # Only update fields that are not None
        if recipe.name is not None:
            db_recipe.name = recipe.name
        if recipe.instructions is not None:
            db_recipe.instructions = recipe.instructions
        if recipe.ingredient_ids is not None:
            db_recipe.ingredients = db.query(Ingredient).filter(Ingredient.id.in_(recipe.ingredient_ids)).all()
        
        db.commit()
        db.refresh(db_recipe)
    return db_recipe


def delete(db: Session, recipe_id: int):
    db_recipe = get_by_id(db, recipe_id)
    if db_recipe:
        db.delete(db_recipe)
        db.commit()
    return db_recipe
