from app.models.post import Post
from app.schemas.post import PostCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class PostService:
    @staticmethod
    async def create_post(db: AsyncSession, data: PostCreate):

        post = Post(**data.model_dump())

        db.add(post)
        await db.commit()
        await db.refresh(post)

        return post

    @staticmethod
    async def get_posts(db: AsyncSession):

        stmt = select(Post)

        result = await db.execute(stmt)

        return result.scalars().all()
