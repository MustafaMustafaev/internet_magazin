from fastapi import FastAPI
from app.routers import category as category_router
from app.routers import products as products_router
from app.routers import auth
from app.routers import permission

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "My e-commerce app"}

app.include_router(category_router.router)
app.include_router(products_router.router)
app.include_router(auth.router)
app.include_router(permission.router)
