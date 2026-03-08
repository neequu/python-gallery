import json

import redis.asyncio as redis
from app.events.handlers import handle_event


async def start_event_consumer():

    r = redis.Redis(host="localhost", port=6379)

    pubsub = r.pubsub()

    await pubsub.subscribe("users")

    async for message in pubsub.listen():
        if message["type"] != "message":
            continue

        event = json.loads(message["data"])

        await handle_event(event)
