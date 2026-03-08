from pydantic import BaseModel


class CommentCreate(BaseModel):

    post_id: int
    content: str


class CommentResponse(BaseModel):

    id: int
    post_id: int
    user_id: int
    user_email: str
    content: str

    model_config = {"from_attributes": True}