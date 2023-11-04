from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field, Relationship, Session, select, col

if TYPE_CHECKING:
    from app.models.post import Post


class CommentBase(SQLModel):
    content: str
    author: str


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    submitted: datetime = datetime.now()
    edited: datetime | None = None


class Comment(CommentRead, table=True):
    id: int | None = Field(primary_key=True)
    deleted: datetime | None = None

    post_id: int | None = Field(default=None, foreign_key="post.id")
    post: Optional["Post"] = Relationship(back_populates="comments")

    @classmethod
    def get_list(cls, db_session: Session, offset: int = 0, limit: int = 25):
        return db_session.exec(
            select(cls)
            .where(col(cls.deleted) == None)
            .order_by(cls.submitted)
            .limit(25)
        ).all()
