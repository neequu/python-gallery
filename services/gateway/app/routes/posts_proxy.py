from fastapi import APIRouter, Request
from httpx import Response

from app.core.config import settings
from app.proxy.client import async_client

router = APIRouter(prefix="/posts")


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_posts(request: Request, path: str):

    url = f"{settings.posts_service_url}/posts/{path}"

    response: Response = await async_client.request(
        request.method,
        url,
        headers=request.headers.raw,
        content=await request.body(),
    )

    return response.json()