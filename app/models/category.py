from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models import *

from app.backend.db import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    slug = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    products = relationship('Product', back_populates='category')

