from sqlmodel import Field, SQLModel
from typing import Optional

class Products(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    desc: Optional[str] = None
    price: float
    quantity: int