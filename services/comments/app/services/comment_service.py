from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.comment import Comment
from app.schemas.comment import CommentCreate


class CommentService:

    @staticmethod
    async def create_comment(
        db: AsyncSession,
        data: CommentCreate,
        user_id: int,
        user_email: str,
    ):

        comment = Comment(
            post_id=data.post_id,
            content=data.content,
            user_id=user_id,
            user_email=user_email,
        )

        db.add(comment)

        await db.commit()
        await db.refresh(comment)

        return comment

    @staticmethod
    async def get_post_comments(
        db: AsyncSession,
        post_id: int,
    ):

        stmt = select(Comment).where(Comment.post_id == post_id)

        result = await db.execute(stmt)

        return result.scalars().all()