from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

from shared.db.base import Base


class Comment(Base):

    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)

    post_id: Mapped[int] = mapped_column(index=True)

    user_id: Mapped[int] = mapped_column(index=True)

    user_email: Mapped[str] = mapped_column(String(255))

    content: Mapped[str] = mapped_column(String(500))