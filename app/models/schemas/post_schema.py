from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str

class UserInDB(PostBase):
    id: int
