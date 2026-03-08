from fastapi import APIRouter, Request
from httpx import Response

from app.core.config import settings
from app.proxy.client import async_client

router = APIRouter(prefix="/comments")


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_posts(request: Request, path: str):

    url = f"{settings.comments_service_url}/comments/{path}"

    headers = dict(request.headers)

    if hasattr(request.state, "user_id"):
        headers["X-User-ID"] = request.state.user_id

    response: Response = await async_client.request(
        request.method,
        url,
        headers=headers,
        content=await request.body(),
    )

    return response.json()
