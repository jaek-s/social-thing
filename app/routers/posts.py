from datetime import datetime
from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session, col, select

from app.dependencies import (
    get_db_session,
    get_post_from_path_param,
    get_active_post_from_path_param,
)
from app.models import Post, PostCreate, PostRead, PostUpdate


router = APIRouter(tags=["Posts"])


@router.get("/posts", response_model=list[PostRead])
def get_post_list(
    db_session: Annotated[Session, Depends(get_db_session)],
    offset: int = Query(default=0),
    limit: int = Query(default=25, lte=100),
):
    return db_session.exec(
        select(Post).where(col(Post.deleted) == None).offset(offset).limit(limit)
    ).all()


@router.post("/posts")
def create_post(
    new_post: PostCreate, db_session: Annotated[Session, Depends(get_db_session)]
):
    db_post = Post.model_validate(new_post)

    db_session.add(db_post)
    db_session.commit()
    db_session.refresh(db_post)

    return db_post


@router.get("/posts/{post_id}", response_model=PostRead)
def get_post(db_post: Annotated[Post, Depends(get_post_from_path_param)]):
    return db_post


@router.patch("/posts/{post_id}", response_model=PostRead)
def edit_post(
    post_updates: PostUpdate,
    db_post: Annotated[Post, Depends(get_active_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    # This works so long as the post model is not deeply nested.
    for key, value in post_updates.model_dump(exclude_unset=True).items():
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
