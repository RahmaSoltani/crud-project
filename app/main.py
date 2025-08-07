
from fastapi import FastAPI
from app.core.database import Base, engine

from app.api.routes import  ingredient_types
from app.api.routes import  recipes , ingredients

#uvicorn app.main:app --reload
# Create the tables (optional here if already done in database.py)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe API")
app = FastAPI(debug=True)

# Include routers
app.include_router(recipes.router, prefix="/recipes", tags=["Recipes"])
app.include_router(ingredients.router, prefix="/ingredients", tags=["Ingredients"])
app.include_router(ingredient_types.router, prefix="/ingredient-types", tags=["Ingredient Types"])
