from sqlmodel import SQLModel
from typing import Optional

class ProductBase(SQLModel):
    name: str
    desc: Optional[str] = None
    price: float
    quantity: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass