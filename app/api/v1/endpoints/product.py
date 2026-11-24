from fastapi import APIRouter, HTTPException

from app.schemas.product import ProductUpdate, ProductCreate, ProductMovimentCreate
from app.models.product import Products, ProductsMoviments
from app.dependencies import ProductRepoDep

router = APIRouter()

@router.get("/", response_model=list[Products])
async def list_products(prod_repo: ProductRepoDep):
    return await prod_repo.list_products()

@router.post("/", response_model=Products)
async def add_product(prod_repo: ProductRepoDep,
                      prod: ProductCreate):
    product = await prod_repo.create_product(prod)

    if not product:
        raise HTTPException(status_code=404, detail="Product not created")

    return product

@router.get("/{product_id}", response_model=Products)
async def list_produt(prod_repo: ProductRepoDep,
                      product_id: int):
    product = await prod_repo.list_product(product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not created")

    return product

@router.delete("/{product_id}", status_code=204)
async def delete_product(prod_repo:ProductRepoDep,
                         product_id: int):
    product = await prod_repo.delete_product(product_id=product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not created")

    return product

@router.put("/{product_id}", response_model=Products)
async def update_product(prod_repo:ProductRepoDep,
                         product_id: int,
                         product: ProductUpdate):
    product = prod_repo.update_product(product, product_id)

    if not product:
        raise HTTPException(status_code=404, detail="Product not created")

    return product


@router.post("/{product_id}/movements", response_model=ProductsMoviments)
async def add_movement(prod_repo: ProductRepoDep,
                       product_id: int,
                       movements: ProductMovimentCreate):
    product = prod_repo.create_movement(product_id, movements)

    if not product:
        raise HTTPException(status_code=404, detail="Product not created")

    return product

@router.get("/{product_id}/movements", response_model=list[ProductsMoviments])
async def list_movements(prod_repo: ProductRepoDep):

    return await prod_repo.list_movements()

@router.patch("/{product_id}/quantity", response_model=ProductsMoviments)
async def patch_quantity(prod_repo: ProductRepoDep,
                         product_id: int,
                         qtd: ProductMovimentCreate):
    product = await prod_repo.patch_qtd(product_id, qtd)

    if not product:
        raise HTTPException(status_code=404, detail="Product not created")

    return product