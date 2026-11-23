from sqlmodel import SQLModel, Field
from typing import Optional, Literal
from datetime import datetime

class ProductBase(SQLModel):
    name: str
    desc: Optional[str] = None
    price: float = Field(gt=0)
    stock: int = Field(default=0, ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    desc: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)

class ProductMovimentCreate(SQLModel):
    movement_type: Literal["entry", "exit"]
    quantity: int = Field(gt=0)
    reason: Optional[str] = None