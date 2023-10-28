from datetime import datetime

from sqlmodel import SQLModel, Field


class CommentCreate(SQLModel):
    content: str
    author: str


class CommentRead(CommentCreate):
    id: int
    created: datetime
    deleted: datetime | None = None


class Comment(CommentRead, table=True):
    id: int | None = Field(primary_key=True)
