from app.db.session import AsyncSessionLocal
from app.models.comment import Comment
from sqlalchemy import update


async def handle_event(event: dict):

    if event["type"] == "user_email_updated":
        async with AsyncSessionLocal() as db:
            stmt = (
                update(Comment)
                .where(Comment.user_id == event["user_id"])
                .values(user_email=event["email"])
            )

            await db.execute(stmt)

            await db.commit()
