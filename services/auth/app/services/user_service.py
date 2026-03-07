from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class UserService:
    @staticmethod
    async def create_user(db: AsyncSession, data: UserCreate) -> User:

        user = User(
            email=data.email,
            hashed_password=hash_password(data.password),
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)

        return user

    @staticmethod
    async def get_by_email(db: AsyncSession, email: str):

        stmt = select(User).where(User.email == email)

        result = await db.execute(stmt)

        return result.scalar_one_or_none()
