from pydantic import BaseModel


class UserEmailUpdatedEvent(BaseModel):

    type: str = "user_email_updated"

    user_id: int

    email: str