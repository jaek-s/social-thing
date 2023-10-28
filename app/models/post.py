from datetime import datetime

from sqlmodel import SQLModel, Field


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
    updated: datetime | None = None
    deleted: datetime | None = None


class Post(PostRead, table=True):
    id: int | None = Field(primary_key=True)
