from typing import Annotated
from fastapi import Depends
from sqlmodel import Session

from app.db.db_conn import get_session
from app.repositories.product import ProductRepo

def get_product_repository(session: Session = Depends(get_session)) -> ProductRepo:
    return ProductRepo(session)

ProductRepoDep = Annotated[ProductRepo, Depends(get_product_repository)]