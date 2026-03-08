import asyncio

from app.api.routes_comments import router as comments_router
from app.events.consumer import start_event_consumer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Comments Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(comments_router)


@app.on_event("startup")
async def startup():

    asyncio.create_task(start_event_consumer())
