from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.comment import Comment


class PostBase(SQLModel):
    title: str
    content: str
    author: str


class PostUpdate(SQLModel):
    title: str | None = None
    content: str | None = None
    author: str | None = None


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    created: datetime = datetime.now()
    edited: datetime | None = None
    deleted: datetime | None = None

    comments: list["Comment"] = Relationship(back_populates="post")


class Post(PostRead, table=True):
    id: int | None = Field(primary_key=True)
