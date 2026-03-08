import asyncio
from fastapi import FastAPI

from app.api.routes_comments import router as comments_router
from app.events.consumer import start_event_consumer


app = FastAPI(title="Comments Service")

app.include_router(comments_router)


@app.on_event("startup")
async def startup():

    asyncio.create_task(start_event_consumer())