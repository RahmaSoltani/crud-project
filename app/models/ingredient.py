from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
class Ingredient(Base):
    __tablename__ = "ingredients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    ingredient_type_id = Column(Integer, ForeignKey("ingredient_types.id"))
    
    ingredient_type = relationship("IngredientType", backref="ingredients")
    recipes = relationship("Recipe", secondary="recipe_ingredients", back_populates="ingredients")  # <-- add this line 