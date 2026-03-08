from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.comment import CommentCreate, CommentResponse
from app.services.comment_service import CommentService
from app.db.session import get_db
from app.dependencies.auth import get_user_context


router = APIRouter(prefix="/comments", tags=["comments"])


@router.post("/", response_model=CommentResponse)
async def create_comment(
    data: CommentCreate,
    user=Depends(get_user_context),
    db: AsyncSession = Depends(get_db),
):

    return await CommentService.create_comment(
        db,
        data,
        user["user_id"],
        user["user_email"],
    )


@router.get("/post/{post_id}", response_model=list[CommentResponse])
async def get_comments(
    post_id: int,
    db: AsyncSession = Depends(get_db),
):

    return await CommentService.get_post_comments(db, post_id)