from app.db.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(index=True)

    caption: Mapped[str] = mapped_column(String(500))

    image_url: Mapped[str] = mapped_column(String(500))
