from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship, Session, col, select

if TYPE_CHECKING:
    from app.models.comment import Comment, CommentRead


class PostBase(SQLModel):
    title: str
    content: str
    author: str


class PostUpdate(SQLModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int
    submitted: datetime
    edited: datetime | None = None


class PostReadWithComments(PostRead):
    comments: list["CommentRead"] = []


class Post(PostRead, table=True):
    id: int | None = Field(primary_key=True)
    submitted: datetime = datetime.now()
    edited: datetime | None = None
    deleted: datetime | None = None

    comments: list["Comment"] = Relationship(back_populates="post")
