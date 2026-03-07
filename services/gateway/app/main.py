from fastapi import FastAPI

from app.routes.auth_proxy import router as auth_router
from app.routes.posts_proxy import router as posts_router
from app.middleware.auth import AuthMiddleware


app = FastAPI(title="API Gateway")

app.add_middleware(AuthMiddleware)

app.include_router(auth_router)
app.include_router(posts_router)