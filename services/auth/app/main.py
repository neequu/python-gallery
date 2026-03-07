from app.api.routes_auth import router as auth_router
from fastapi import FastAPI

app = FastAPI(title="Auth Service")

app.include_router(auth_router)
