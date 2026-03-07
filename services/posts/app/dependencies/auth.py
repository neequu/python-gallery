from fastapi import Header, HTTPException


async def get_current_user_id(x_user_id: str | None = Header(default=None)):

    if not x_user_id:
        raise HTTPException(status_code=401, detail="Missing user")

    return int(x_user_id)