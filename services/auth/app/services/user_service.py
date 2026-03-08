from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from services.auth.app.events.publisher import EventPublisher


class UserService:
    
    publisher = EventPublisher()
    
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
    
    

    @staticmethod
    async def update_email(
        db: AsyncSession,
        user_id: int,
        email: str,
    ):

        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(email=email)
            .returning(User)
        )

        result = await db.execute(stmt)

        user = result.scalar_one()

        await db.commit()

        await UserService.publisher.publish_user_email_updated(
            user.id,
            user.email,
        )

        return user
