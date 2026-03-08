from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user_update import UserEmailUpdate
from shared.security.jwt import create_access_token
from app.core.security import verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
async def register(
    data: UserCreate,
    db: AsyncSession = Depends(get_db),
):

    user = await UserService.create_user(db, data)

    return user

@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):

    user = await UserService.get_by_email(db, data.email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(user_id=user.id)

    return TokenResponse(access_token=token)


@router.put("/email/{user_id}")
async def update_email(
    user_id: int,
    data: UserEmailUpdate,
    db: AsyncSession = Depends(get_db),
):

    user = await UserService.update_email(
        db,
        user_id,
        data.email,
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "email": user.email
    }