from sqlmodel import SQLModel, create_engine

# All table models need to be imported before `SQLModel.metadata.create_all` is called.
# We'll import everything here to be safe.
from app import models

# Models with circular references need to be updated. This is not DB specific per se,
# but needs to happen before anything else. This is the perfect spot since models
# need to be imported here anyways.
models.PostReadWithComments.update_forward_refs(CommentRead=models.CommentRead)

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def init_db():
    SQLModel.metadata.create_all(engine)
