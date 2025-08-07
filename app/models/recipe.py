
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.ingredient import Ingredient  # import to avoid circular issues
from sqlalchemy.orm import relationship

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    instructions = Column(String)
    
    ingredients = relationship("Ingredient", secondary="recipe_ingredients", back_populates="recipes")

from sqlalchemy import Table, Column, Integer, ForeignKey
from app.core.database import Base

recipe_ingredients = Table(
    "recipe_ingredients",
    Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipes.id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredients.id"), primary_key=True)
)
