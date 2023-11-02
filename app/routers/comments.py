from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.dependencies import get_db_session, get_post_from_path_param
from app.models import Comment, CommentCreate, CommentRead, Post

router = APIRouter(tags=["Comments"])


@router.get("/posts/{post_id}/comments", response_model=list[CommentRead])
def get_comment_list(post_id: str):
    pass


@router.post("/posts/{post_id}/comments", response_model=CommentRead)
def create_comment(
    new_comment: CommentCreate,
    db_post: Annotated[Post, Depends(get_post_from_path_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    db_comment = Comment.model_validate(new_comment)
    db_comment.post = db_post

    db_session.add(db_comment)
    db_session.commit()
    db_session.refresh(db_comment)

    return db_comment


@router.get("/posts/{post_id}/comments/{comment_id}")
def get_comment(post_id: str, comment_id: str):
    pass


@router.patch("/posts/{post_id}/comments/{comment_id}")
def edit_comment(post_id: str, comment_id: str):
    pass


@router.delete("/posts/{post_id}/comments/{comment_id}")
def delete_comment(post_id: str, comment_id: str):
    pass
