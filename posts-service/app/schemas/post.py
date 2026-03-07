from pydantic import BaseModel


class PostCreate(BaseModel):
    caption: str
    image_url: str
    user_id: int


class PostResponse(BaseModel):
    id: int
    caption: str
    image_url: str
    user_id: int

    model_config = {"from_attributes": True}
