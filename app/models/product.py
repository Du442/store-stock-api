from sqlmodel import Field, SQLModel
from typing import Optional, Literal
from datetime import datetime, timezone

class Products(SQLModel, table=True):
    __tablename__="products"

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str
    desc: Optional[str] = None
    price: float
    stock: int = Field(default=0, ge=0)

class ProductsMoviments(SQLModel, table=True):
    __tablename__="products_movements"

    id: Optional[int] = Field(primary_key=True, default=None)
    product_id: int = Field(foreign_key="products.id")
    movement_type: str
    quantity: int = Field(gt=0)
    reason: Optional[str] = None
    created_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))