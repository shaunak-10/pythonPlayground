from .db import users, products, database_pg, database_mysql
from .schemas import UserCreate, ProductCreate

# Users (Postgres)
async def create_user(user: UserCreate):
    query = users.insert().values(name=user.name, email=user.email)
    id_ = await database_pg.execute(query)
    return {**user.dict(), "id": id_}

async def list_users():
    query = users.select()
    return await database_pg.fetch_all(query)

async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database_pg.fetch_one(query)

async def update_user(user_id: int, user: UserCreate):
    query = users.update().where(users.c.id == user_id).values(name=user.name, email=user.email)
    await database_pg.execute(query)
    return await get_user(user_id)

async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database_pg.execute(query)
    return {"deleted": user_id}

# Products (MySQL)
async def create_product(product: ProductCreate):
    query = products.insert().values(name=product.name, price=product.price)
    id_ = await database_mysql.execute(query)
    return {**product.dict(), "id": id_}

async def list_products():
    query = products.select()
    return await database_mysql.fetch_all(query)

async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    return await database_mysql.fetch_one(query)

async def update_product(product_id: int, product: ProductCreate):
    query = products.update().where(products.c.id == product_id).values(name=product.name, price=product.price)
    await database_mysql.execute(query)
    return await get_product(product_id)

async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    await database_mysql.execute(query)
    return {"deleted": product_id}
