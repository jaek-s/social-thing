from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session, col, select

from app.dependencies import (
    get_db_session,
    get_post_from_path_param,
    get_active_post_from_path_param,
)
from app import models
from app.models import Comment, Post


router = APIRouter(tags=["Posts"])


@router.get("/posts", response_model=list[models.PostRead])
def get_post_list(
    db_session: Annotated[Session, Depends(get_db_session)],
    offset: int = Query(default=0),
    limit: int = Query(default=25, lte=100),
):
    return db_session.exec(
        select(Post)
        .where(col(Post.deleted) == None)
        .order_by(Post.submitted)
        .offset(offset)
        .limit(limit)
    ).all()


@router.post("/posts")
def create_post(
    new_post: models.PostCreate, db_session: Annotated[Session, Depends(get_db_session)]
):
    db_post = Post.from_orm(new_post)

    db_session.add(db_post)
    db_session.commit()
    db_session.refresh(db_post)

    return db_post


@router.get("/posts/{post_id}", response_model=models.PostReadWithComments)
def get_post(
    db_post: Annotated[Post, Depends(get_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    post_read_without_comments = models.PostRead.from_orm(db_post)
    post_read = models.PostReadWithComments.from_orm(post_read_without_comments)

    comment_list = db_session.exec(
        select(Comment)
        .where(col(Comment.deleted) == None, col(Comment.post_id == db_post.id))
        .order_by(Comment.submitted)
        .limit(20)
    ).all()

    post_read.comments = [
        models.CommentRead.from_orm(db_comment) for db_comment in comment_list
    ]

    return post_read


@router.patch("/posts/{post_id}", response_model=models.PostRead)
def edit_post(
    post_updates: models.PostUpdate,
    db_post: Annotated[Post, Depends(get_active_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    for key, value in post_updates.dict(exclude_unset=True).items():
        setattr(db_post, key, value)

    db_post.edited = datetime.now()

    db_session.add(db_post)
    db_session.commit()
    db_session.refresh(db_post)

    return db_post


@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    db_post: Annotated[Post, Depends(get_active_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    db_post.deleted = datetime.now()

    db_session.add(db_post)
    db_session.commit()
