from app.db.session import get_db
from app.schemas.post import PostCreate, PostResponse
from app.services.post_service import PostService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostResponse)
async def create_post(
    data: PostCreate,
    db: AsyncSession = Depends(get_db),
):
    return await PostService.create_post(db, data)


@router.get("/", response_model=list[PostResponse])
async def list_posts(
    db: AsyncSession = Depends(get_db),
):
    return await PostService.get_posts(db)
