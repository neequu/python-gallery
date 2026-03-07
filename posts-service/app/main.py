from app.api.routes_posts import router as posts_router
from fastapi import FastAPI

app = FastAPI(title="Posts Service")

app.include_router(posts_router)
