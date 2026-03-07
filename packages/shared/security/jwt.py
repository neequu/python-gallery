from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt

SECRET = "dev-secret"
ALGORITHM = "HS256"


def create_access_token(*, user_id: int) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=60
    )

    payload = {
        "sub": str(user_id),
        "exp": expire,
    }

    return jwt.encode(
        payload, SECRET, algorithm=ALGORITHM
    )


def decode_access_token(token: str) -> int:
    try:
        payload = jwt.decode(
            token, SECRET, algorithms=[ALGORITHM]
        )
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise ValueError("Missing subject")
        return int(user_id)
    except JWTError as exc:
        raise ValueError("Invalid token") from exc