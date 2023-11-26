from typing import Annotated

from fastapi import (
    Depends,
    HTTPException,
    HTTPException,
    status,
)
from sqlmodel import Session

from app.models.post import Post
from app.db import engine


def get_db_session():
    with Session(engine) as session:
        yield session


def get_post_from_path_param(
    post_id: int, db_session: Annotated[Session, Depends(get_db_session)]
):
    db_post = db_session.get(Post, post_id)
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return db_post


def get_active_post_from_path_param(
    db_post: Annotated[Post, Depends(get_post_from_path_param)]
):
    """
    Get a post that is not deleted
    """
    if not db_post.deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return db_post
