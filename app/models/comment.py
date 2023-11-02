from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.post import Post


class CommentCreate(SQLModel):
    content: str
    author: str


class CommentRead(CommentCreate):
    id: int
    created: datetime = datetime.now()
    edited: datetime | None = None
    deleted: datetime | None = None

    post_id: int | None = Field(default=None, foreign_key="post.id")
    post: "Post | None" = Relationship(back_populates="comments")


class Comment(CommentRead, table=True):
    id: int | None = Field(primary_key=True)
