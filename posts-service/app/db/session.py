from app.core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

engine = create_async_engine(
    settings.database_url,
    echo=True,
)

AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
