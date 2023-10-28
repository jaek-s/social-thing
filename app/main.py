from contextlib import asynccontextmanager
from datetime import datetime
from typing import Annotated

from fastapi import (
    FastAPI,
    APIRouter,
    Depends,
    Query,
    HTTPException,
    HTTPException,
    status,
    Response,
)
from sqlmodel import Session, SQLModel, create_engine, select, col

from app.models.post import Post, PostRead, PostCreate, PostUpdate

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
main_router = APIRouter(prefix="/api")

# ---------------------------------------------------------------------------- #
#                                 Dependencies                                 #
# ---------------------------------------------------------------------------- #


def get_db_session():
    with Session(engine) as session:
        yield session


def get_post_from_url_param(
    post_id: int, db_session: Annotated[Session, Depends(get_db_session)]
):
    db_post = db_session.get(Post, post_id)
    if not db_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return db_post


def get_active_post_from_url_param(
    db_post: Annotated[Post, Depends(get_post_from_url_param)]
):
    """
    Get a post that is not deleted
    """
    if not db_post.deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return db_post


# ---------------------------------------------------------------------------- #
#                                     Posts                                    #
# ---------------------------------------------------------------------------- #

post_router = APIRouter(tags=["Posts"])


@post_router.get("/posts", response_model=list[PostRead])
def get_post_list(
    db_session: Annotated[Session, Depends(get_db_session)],
    offset: int = Query(default=0),
    limit: int = Query(default=25, lte=100),
):
    return db_session.exec(
        select(Post).where(col(Post.deleted) == None).offset(offset).limit(limit)
    ).all()


@post_router.post("/posts")
def create_post(
    new_post: PostCreate, db_session: Annotated[Session, Depends(get_db_session)]
):
    db_post = Post.model_validate(new_post)
    db_session.add(db_post)
    db_session.commit()
    db_session.refresh(db_post)

    return db_post


@post_router.get("/posts/{post_id}", response_model=PostRead)
def get_post(db_post: Annotated[Post, Depends(get_post_from_url_param)]):
    return db_post


@post_router.patch("/posts/{post_id}", response_model=PostRead)
def edit_post(
    post_updates: PostUpdate,
    db_post: Annotated[Post, Depends(get_active_post_from_url_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    # This works so long as the post model is not deeply nested.
    for key, value in post_updates.model_dump(exclude_unset=True).items():
        setattr(db_post, key, value)

    db_post.updated = datetime.now()

    db_session.add(db_post)
    db_session.commit()
    db_session.refresh(db_post)

    return db_post


@post_router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    db_post: Annotated[Post, Depends(get_active_post_from_url_param)],
    db_session: Annotated[Session, Depends(get_db_session)],
):
    db_post.deleted = datetime.now()

    db_session.add(db_post)
    db_session.commit()


main_router.include_router(post_router)

# ---------------------------------------------------------------------------- #
#                                   Comments                                   #
# ---------------------------------------------------------------------------- #

comment_router = APIRouter(tags=["Comments"])


@comment_router.get("/posts/{post_id}/comments")
def get_comment_list(post_id: str):
    pass


@comment_router.post("/posts/{post_id}/comments")
def create_comment(post_id: str):
    pass


@comment_router.get("/posts/{post_id}/comments/{comment_id}")
def get_comment(post_id: str, comment_id: str):
    pass


@comment_router.patch("/posts/{post_id}/comments/{comment_id}")
def edit_comment(post_id: str, comment_id: str):
    pass


@comment_router.delete("/posts/{post_id}/comments/{comment_id}")
def delete_comment(post_id: str, comment_id: str):
    pass


main_router.include_router(comment_router)

app.include_router(main_router)
