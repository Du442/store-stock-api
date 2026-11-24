from sqlmodel import Session, create_engine, SQLModel
from dotenv import load_dotenv
from typing import Generator
import os

load_dotenv(override=True)

connect_args = {"check_same_thread": False} if "sqlite" in os.getenv("DATABASE_URL") else {}

engine = create_engine(url=os.getenv("DATABASE_URL"), echo=True, connect_args=connect_args)

def init_db() -> None:

    # Import models
    from app.models.product import Products, ProductsMoviments

    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session