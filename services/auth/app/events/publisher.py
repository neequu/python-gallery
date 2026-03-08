import redis.asyncio as redis

from app.events.schemas import UserEmailUpdatedEvent


class EventPublisher:

    def __init__(self):

        self.redis = redis.Redis(
            host="localhost",
            port=6379,
            decode_responses=True,
        )

    async def publish_user_email_updated(
        self,
        user_id: int,
        email: str,
    ):

        event = UserEmailUpdatedEvent(
            user_id=user_id,
            email=email,
        )

        await self.redis.publish(
            "users",
            event.model_dump_json(),
        )