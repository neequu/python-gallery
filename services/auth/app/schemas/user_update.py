from pydantic import BaseModel, EmailStr


class UserEmailUpdate(BaseModel):
    email: EmailStr