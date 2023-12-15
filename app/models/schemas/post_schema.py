from typing import Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    text: str

class PostBaseToUpdate(BaseModel):
    title: Optional[str] = None
    text:  Optional[str] = None

class UserInDB(PostBase):
    id: int
