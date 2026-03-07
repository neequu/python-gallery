from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from shared.security.jwt import decode_access_token


PUBLIC_PATHS = [
    "/auth/login",
    "/auth/register",
]


class AuthMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        path = request.url.path

        if any(path.startswith(p) for p in PUBLIC_PATHS):
            return await call_next(request)

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            raise HTTPException(status_code=401, detail="Missing token")

        try:
            scheme, token = auth_header.split()
        except ValueError:
            raise HTTPException(status_code=401, detail="Invalid auth header")

        payload = decode_access_token(token)

        if not payload:
            raise HTTPException(status_code=401, detail="Invalid token")

        request.state.user_id = payload["sub"]

        response = await call_next(request)

        return response