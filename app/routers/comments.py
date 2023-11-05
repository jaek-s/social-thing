from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Query, HTTPException, status
from sqlmodel import Session, select, col

from app import models
from app.dependencies import get_db_session, get_post_from_path_param
from app.models import Comment, Post


def get_comment_from_path_params(
    comment_id: str,
    db_post: Annotated[Post, Depends(get_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    comment = db_session.exec(
        select(Comment)
        .where(Comment.id == comment_id, Comment.post_id == db_post.id)
        .limit(1)
    ).first()

    if comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )

    return comment


router = APIRouter(tags=["Comments"])


@router.get("/posts/{post_id}/comments", response_model=list[models.CommentRead])
def get_comment_list(
    db_post: Annotated[Post, Depends(get_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
    offset: int = Query(default=0),
    limit: int = Query(default=25, lte=100),
):
    return db_session.exec(
        select(Comment)
        .where(col(Comment.deleted) == None, col(Comment.post_id) == db_post.id)
        .order_by(Comment.submitted)
        .offset(offset)
        .limit(limit)
    ).all()


@router.post(
    "/posts/{post_id}/comments",
    response_model=models.CommentRead,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(
    new_comment: models.CommentCreate,
    db_post: Annotated[Post, Depends(get_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    db_comment = Comment.from_orm(new_comment)
    db_comment.post = db_post

    db_session.add(db_comment)
    db_session.commit()
    db_session.refresh(db_comment)

    return db_comment


@router.get("/posts/{post_id}/comments/{comment_id}", response_model=models.CommentRead)
def get_comment(db_comment: Annotated[Comment, Depends(get_comment_from_path_params)]):
    return db_comment


@router.delete(
    "/posts/{post_id}/comments/{comment_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_comment(
    db_comment: Annotated[Comment, Depends(get_comment_from_path_params)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    db_comment.deleted = datetime.now()

    db_session.add(db_comment)
    db_session.commit()


@router.patch("/posts/{post_id}/comments/{comment_id}")
def edit_comment(
    comment_updates: models.CommentUpdate,
    db_comment: Annotated[Comment, Depends(get_comment_from_path_params)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    for key, value in comment_updates.dict(exclude_unset=True).items():
        setattr(db_comment, key, value)

    db_comment.edited = datetime.now()

    db_session.add(db_comment)
    db_session.commit()
    db_session.refresh(db_comment)

    return db_comment
