from sqlmodel import Session, select, update
from app.models.product import Products
from app.schemas.product import ProductCreate, ProductUpdate

class ProductRepo:
    def __init__(self, session: Session):
        self.session = session

    def list_products(self):
        return self.session.exec(select(Products)).all()

    def list_product(self, product_id: int) -> Products | None:
        product = self.session.get(Products, product_id)
        if not product:
            return None
        return product

    def create_product(self, product: ProductCreate) -> Products:
        product_c = Products.model_validate(product)
        self.session.add(product_c)
        self.session.commit()
        self.session.refresh(product_c)
        return product_c

    def update_product(self, product: ProductUpdate, product_id: int) -> Products | None:
        product_s = self.session.get(Products, product_id)
        if not product_s:
            return None

        product_u = Products.model_validate(product)
        self.session.add(product_u)
        self.session.commit()
        self.session.refresh(product_u)
        return product_u

    def delete_product(self, product_id: int) -> bool | None:
        product = self.session.get(Products, product_id)
        if not product:
            return None

        self.session.delete(product)
        self.session.commit()
        return {"ok": True}

    def update_product_stock(self, product_id: int, stock: int) -> Products | None:
        product = self.session.get(Products, product_id)
        if not product:
            return None

        product_u = self.session.exec(update(product).values(stock=stock))
        self.session.add(product_u)
        self.session.commit()
        self.session.refresh(product_u)