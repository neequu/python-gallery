from fastapi import Header, HTTPException


async def get_user_context(
    x_user_id: str | None = Header(default=None),
    x_user_email: str | None = Header(default=None),
):

    if not x_user_id or not x_user_email:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "user_id": int(x_user_id),
        "user_email": x_user_email,
    }