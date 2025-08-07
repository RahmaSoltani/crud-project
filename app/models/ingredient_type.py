from sqlalchemy import Column, Integer, String
from app.core.database import Base

from sqlalchemy.orm import relationship

class IngredientType(Base):
    __tablename__ = "ingredient_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
